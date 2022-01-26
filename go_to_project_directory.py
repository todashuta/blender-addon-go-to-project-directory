# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy


bl_info = {
    "name": "Go to Project Directory (//)",
    "author": "todashuta",
    "version": (1, 1, 0),
    "blender": (2, 80, 0),
    "location": "File Browser",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "File Browser"
}


class GO_TO_PROJECT_DIRECTORY_OT_main(bpy.types.Operator):
    bl_idname = "file.go_to_project_directory"
    bl_label = "Go to Project Directory (//)"
    bl_description = "Go to Project Directory (//)"

    @classmethod
    def poll(cls, context):
        return (isinstance(context.space_data, bpy.types.SpaceFileBrowser)
                and bpy.data.filepath != "")

    def execute(self, context):
        context.space_data.params.directory = b"//"
        return {"FINISHED"}


classes = [
        GO_TO_PROJECT_DIRECTORY_OT_main,
]


def button_func(self, context):
    row = self.layout.row()
    row.operator(GO_TO_PROJECT_DIRECTORY_OT_main.bl_idname, icon="BLENDER", text="Go to //")


addon_keymaps = []


def register_shortcut():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="File Browser", space_type="FILE_BROWSER")
        kmi = km.keymap_items.new(
                idname=GO_TO_PROJECT_DIRECTORY_OT_main.bl_idname,
                type="HOME",
                value="PRESS",
                shift=False,
                ctrl=False,
                alt=False,
        )
        addon_keymaps.append((km, kmi))


def unregister_shortcut():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.FILEBROWSER_PT_directory_path.append(button_func)
    register_shortcut()


def unregister():
    unregister_shortcut()
    bpy.types.FILEBROWSER_PT_directory_path.remove(button_func)
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
