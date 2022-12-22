import open3d as o3d

import numpy as np
import open3d as o3d


class PointCloud(object):
    def __init__(self, array):
        self.cloud = self.__create_pcd(array)
        
    @staticmethod
    def __create_pcd(array):
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(array)
        return pcd
        
    def draw_cloud(self, array:np.ndarray, colors:np.ndarray=None):
        count, dim = array.shape
        try: 
            if dim != 3:
                raise ValueError(f'Expected 3 dimensions but got {dim}')
            
            # Visualize point cloud from array
            print(f'Displaying 3D data for {count:,} data points')
            pcd = self.create_pcd(array)
            if colors is not None:
                pcd.colors = o3d.utility.Vector3dVector(colors)
                
            o3d.visualization.draw_geometries([pcd])
            
        except Exception as e:
            print(f'Failed to draw point cloud: {e}')
        
    def export_cloud(self, cloud, out:str):
        try: 
            o3d.io.write_point_cloud(f'./{out}', cloud)
            print("Saved PLY file.")
            
        except Exception as e:
            print(f'Failed to export point cloud: {e}')

    def draw_voxels(self, array):
        try: 
            N = 1000
            pcd = self.__create_pcd(array)
            pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()), center=pcd.get_center())
            pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
            voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.01)
            o3d.visualization.draw([voxel_grid])

        except Exception as e:
            print(f'Failed to draw voxel grid: {e}')
    