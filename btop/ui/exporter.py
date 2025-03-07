from pathlib import Path
import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import (
    Context,
    Operator,
    TOPBAR_MT_file_export,
)

from ..io import PBRTExporter

def export_pbrt(filepath: Path, context: Context) -> set[str]:
    try :
        exporter = PBRTExporter()
        exporter.export(filepath)
        return {"FINISHED"}
    except Exception as e:
        print('execute pbrt command failed:\n', e)
        return {"CANCELLED"}


class EXPORT_SCENE_OT_pbrt(Operator, ExportHelper):
    bl_idname = "export_scene.pbrt"
    bl_label = "Export pbrt"

    filename_ext = ".pbrt"

    def execute(self, context: Context) -> set[str]:
        if not self.filepath:
            return {"CANCELLED"}
        path = Path(self.filepath)
        return export_pbrt(path, context)


def menu_export(menu_op: Operator, _context: Context) -> None:
    pass


def register():
    TOPBAR_MT_file_export.append(menu_export)


def unregister():
    pass
