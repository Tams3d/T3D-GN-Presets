<div align="center">

# T3D GN Presets

## A Versatile Collection of Useful node groups for Geometry Nodes - Blender 4.4 & Above

![T3D GN Presets (v1.6.0)](https://github.com/Tams3d/T3D-GN-Presets/assets/106262964/c3efe10c-5478-4ad7-954a-8a838cf1a0b1)

</div>

## 💡 Introduction

- [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/#t3d-gn-presets) is a versatile collection of useful node groups for Geometry Nodes.
- This is an essential component of an artist’s toolkit, containing node groups for deformers, fields, UV, utilities, and much more for **free!**
- It allows users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.

## 🪄 Release Notes

- **T3D-GN-Presets (v1.6.0)** for Blender 4.4 brings several changes to the user experience with the extension.
- For Blender 4.3 & below, check out previous releases [here](https://github.com/Tams3d/T3D-GN-Presets/releases)

> [!TIP]
> Download from [Blender Extensions](https://extensions.blender.org/add-ons/t3d-gn-presets/) for regular updates

## ⚙️ Core

### Source Files

- Node options are hidden by default [(4f0a415)](https://github.com/Tams3d/T3D-GN-Presets/commit/4f0a4154cae52a2e8dc3e30aec9c0004bb506a56)

- Use " - " to split name and tooltip [(5f9ee44)](https://github.com/Tams3d/T3D-GN-Presets/commit/5f9ee44)

- Updated [manifest](https://github.com/Tams3d/T3D-GN-Presets/blob/main/blender_manifest.toml) file containing required meta-data.

### Repository

- Updated [Feature Request Template](https://github.com/Tams3d/T3D-GN-Presets/commit/2e72d4c)

## 🎆 New Nodes, Features & Changes

### Changes

- Node options are now hidden by default [(4f0a415)](https://github.com/Tams3d/T3D-GN-Presets/commit/4f0a415)
- Better Easing nodes [(dc33d97)](https://github.com/Tams3d/T3D-GN-Presets/commit/dc33d97)
- **Is Inside Volume** now works at origin [(2d2d8de)](https://github.com/Tams3d/T3D-GN-Presets/commit/2d2d8de)
- New evaluation method in **Sweep Curve**, outputs UVs [(35aeabe)](https://github.com/Tams3d/T3D-GN-Presets/commit/35aeabe)
- Exposed selection socket in supported nodes.
- Fixed Selection Socket links [(27d988a)](https://github.com/Tams3d/T3D-GN-Presets/commit/27d988a)

### New Nodes

- **Is Vector Coplanar** - check if vectors lie on the same plane [(79df0cc)](https://github.com/Tams3d/T3D-GN-Presets/commit/79df0cc)
- **Stretch** - stretches or scale geometry in multiple axes [(7f2f71a)](https://github.com/Tams3d/T3D-GN-Presets/commit/7f2f71a)

### Matrix Nodes

- **Scalar Matrix** - takes a float value and outputs a scalar matrix
- **Diagonal Matrix** - converts input Matrix to output only elements in principal diagonal
- **Trace Matrix** - computes sum of elements in principal diagonal
- **Triangular Matrix** - converts input Matrix to output only elements in Upper/Lower Diagonal
- **Is Symmetric Matrix** - Checks if the matrix is symmetric
- **Matrix Viewer** - outputs elements as instances

> [!NOTE]
> Nodes with geometry input only support **Mesh, Curves, Point Clouds**

## 🪛 Compatibility

- Make sure to have a supported **Blender** version and the corresponding addon version.
- Nodes with Menu, Rotation and Matrix sockets are _not_ compatible with Blender versions 4.1 and below.
- Changes in newer addon versions are not retained for files migrated from older versions to newer versions, as nodes are only appended, not [linked](https://github.com/Tams3d/T3D-GN-Presets/blob/main/__init__.py#L156).

## 🎯 Development

- Developments are happening regularly to provide support for every upcoming [Blender Release](https://www.blender.org/download/releases/)
- **🧩 Community contributions are always welcomed!**

### 👻 Bug Reports

- Bug reports are always welcomed in the form of reports or requests.
- Submit bug reports and feature requests [here](https://github.com/Tams3d/T3D-GN-Presets/issues)

## 📂 Access to Files

- [`_init_.py`](https://github.com/Tams3d/T3D-GN-Presets/blob/main/__init__.py) defines the addon followed by [t3d_nodegroups.json](https://github.com/Tams3d/T3D-GN-Presets/blob/main/t3d_nodegroups.json), which contains a list of categories with nodes.
- [t3d_nodes.blend](https://github.com/Tams3d/T3D-GN-Presets/blob/main/t3d_nodes.blend) contains all the Node-groups which are displayed under `T3D GN Presets`

## 🦄 About

- Hey! I am **Tamil Selvan**, also known as **tams_3d**. I am a 18-year-old self-taught Blender artist from **India**.
- My vision is to create _free_ tools for Blender, which require complex setups provided in a simplified and effective way.
- I am currently developing presets for Geometry Nodes that are similar to tools and features of other 3D packages and some add-ons.
- I believe that my work contributes to a better world for 3D artists, game developers, and other artists who create incredible works.

## 🥂 Socials

Catch up with me here:

- [Behance](https://www.behance.net/tamilselvan3d)
- [Blender Extensions](https://extensions.blender.org/add-ons/t3d-gn-presets/)
- [GitHub](https://github.com/Tams3d)
- [X](https://x.com/Tams_3d)
