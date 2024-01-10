# geotiff_utils.py
import rasterio
from rasterio.transform import from_origin
from rasterio.warp import transform_geom, calculate_default_transform, transform, reproject
import sys

from PIL import Image


def is_tiff(file_path):
    try:
        # เปิดไฟล์รูปภาพ
        image = Image.open(file_path)

        # ตรวจสอบรูปแบบของไฟล์
        if not image.format == "TIFF":
            print(f"The file {file_path} is not a TIFF image.")
            sys.exit()
        return image.format == "TIFF"
    except Exception as e:
        # กรณีเกิดข้อผิดพลาด (ไม่สามารถเปิดไฟล์เป็นรูปภาพได้)
        print(f"Error: {e}")
        return False


def open_geotiff(file_path):
    """Open a GeoTIFF file and return the rasterio dataset."""
    if not is_tiff(file_path):
        return None
    return rasterio.open(file_path)


def get_geotiff_metadata(dataset):
    """Get metadata information from a GeoTIFF dataset."""
    return dataset.meta


def get_geotiff_crs(dataset):
    """Get CRS (Coordinate Reference System) from a GeoTIFF dataset."""
    return dataset.crs


def get_geotiff_crs_pixel(dataset):
    return {
        'width': dataset.width,
        'height': dataset.height
    }


def transform_pixel_to_geo(dataset, x_pixel, y_pixel):
    """Transform pixel coordinates to geographic coordinates."""
    transform = dataset.transform
    lon, lat = transform * (x_pixel, y_pixel)
    return lon, lat



def reproject_coordinates(dataset, x_pixel, y_pixel, target_crs='EPSG:4326'):
    """Reproject pixel coordinates to a target CRS."""
    transform = dataset.transform
    lon, lat = transform * (x_pixel, y_pixel)

    geom = {'type': 'Point', 'coordinates': (lon, lat)}
    reprojected_geom = transform_geom(dataset.crs, target_crs, geom)

    return reprojected_geom['coordinates']


def pixel_coordinates_to_latlon(dataset):
    x_pixel = dataset.width // 2
    y_pixel = dataset.height // 2

    """Transform pixel coordinates to latitude and longitude."""
    lon, lat = transform_pixel_to_geo(dataset, x_pixel, y_pixel)
    print(lon, lat)
    lon_convert_EPSG4326, lat_convert_EPSG4326 = reproject_coordinates(dataset, x_pixel, y_pixel)
    return {
        'latitude': lat,
        'longitude': lon,
        'lat_convert_EPSG4326': lat_convert_EPSG4326,
        'lon_convert_EPSG4326': lon_convert_EPSG4326

    }


def get_raster_data(dataset, band=1):
    """Get raster data from a specific band of a GeoTIFF dataset."""
    return dataset.read(band)


def create_geotiff(output_path, data, transform, crs, driver='GTiff'):
    """Create a new GeoTIFF file."""
    with rasterio.open(output_path, 'w', driver=driver, count=1, dtype=data.dtype, crs=crs, transform=transform) as dst:
        dst.write(data, 1)


def calculate_rectangle_coordinates_latlng_tif(dataset):
    # Open the TIFF file

    widthheight_pixel = get_geotiff_crs_pixel(dataset)
    # Get image size
    width_pixels = widthheight_pixel['width']
    height_pixels = widthheight_pixel['height']

    result_convert = pixel_coordinates_to_latlon(dataset)

    center_lat, center_lng = result_convert['lat_convert_EPSG4326'], result_convert['lon_convert_EPSG4326']

    # Adjust the scale factor based on your specific data and mapping system
    # scale_factor_lat = 0.00000025  # Adjust this value as needed
    # scale_factor_lng = 0.00000025  # Adjust this value as needed
    scale_factor_lat = 0.000005  # Adjust this value as needed
    scale_factor_lng = 0.000005  # Adjust this value as needed

    # Calculate the coordinates of the corners
    top_left_lat = center_lat - (height_pixels / 2) * scale_factor_lat
    top_left_lng = center_lng - (width_pixels / 2) * scale_factor_lng

    # top_right_lat = center_lat - (height_pixels / 2) * scale_factor_lat
    # top_right_lng = center_lng + (width_pixels / 2) * scale_factor_lng

    # bottom_left_lat = center_lat + (height_pixels / 2) * scale_factor_lat
    # bottom_left_lng = center_lng - (width_pixels / 2) * scale_factor_lng

    bottom_right_lat = center_lat + (height_pixels / 2) * scale_factor_lat
    bottom_right_lng = center_lng + (width_pixels / 2) * scale_factor_lng

    # 'top_left_latlng': (top_left_lat, top_left_lng),
    # 'top_right_latlng': (top_right_lat, top_right_lng),
    # 'bottom_left_latlng': (bottom_left_lat, bottom_left_lng),
    # 'bottom_right_latlng': (bottom_right_lat, bottom_right_lng)

    # "lon_min" : top_left_lng,
    # "lat_min" : top_left_lat,
    # "lon_max" : bottom_right_lng,
    # "lat_max" : bottom_right_lat

    return {
        "Coordinates": f"Coordinates: lon_min={top_left_lng:.5f}, lat_min={top_left_lat:.5f}, lon_max={bottom_right_lng:.5f}, lat_max={bottom_right_lat:.5f}",
        "Raw_Coordinates": f"{top_left_lng:.4f},{top_left_lat:.4f},{bottom_right_lng:.4f},{bottom_right_lat:.4f}"
    }




