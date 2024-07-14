<div align="center">

# T3D GN Presets

## A Versatile Collection of Useful node groups for Geometry Nodes - Blender 4.2 LTS

![T3D GN Presets (v1.5.1)](https://github.com/Tams3d/T3D-GN-Presets/assets/106262964/c3efe10c-5478-4ad7-954a-8a838cf1a0b1)

</div>

## 💡 Introduction

- [T3D GN Presets](https://github.com/Tams3d/T3D-GN-Presets/#t3d-gn-presets) is a versatile collection of useful node groups for Geometry Nodes.
- This is an essential component of an artist’s toolkit, containing node groups for deformers, fields, UV, utilities, and much more for **free!**
- It allows users to combine multiple nodes with endless possibilities in non-destructive workflows with existing Blender tools.

## 🪄 Release Notes

- **T3D-GN-Presets (v1.5.1)** for Blender 4.2 LTS is a `corrective release` primarily made to enhance user experience with nodes and minor changes.
- For Blender 4.1 & below, check out previous releases [here](https://github.com/Tams3d/T3D-GN-Presets/releases)

> [!TIP]
> Download from [Blender Extensions](https://extensions.blender.org/add-ons/t3d-gn-presets/) to get regular updates.

## ⚙️ Core

### Source Files

- Added [manifest](https://github.com/Tams3d/T3D-GN-Presets/blob/main/blender_manifest.toml) file containing required meta-data.

### Repository

- Updated [Feature Request Template](https://github.com/Tams3d/T3D-GN-Presets/commit/2e72d4c)

## 🎆 New Nodes, Features & Changes

### New Nodes

- **Vertex of Edge** outputs the index of the vertex that a edge is attached to. [(141cbff)](https://github.com/Tams3d/T3D-GN-Presets/commit/141cbff)

### Features & Changes

- **Extend Curve** now extends endpoints of curves along the tangent without extrusion. Supports multiple curves with individual endpoints extension.[(cf3bd9c)](https://github.com/Tams3d/T3D-GN-Presets/commit/cf3bd9c)
- **Center Elements** supports menu for Bound Center and Element Center.[(587f9a4)](https://github.com/Tams3d/T3D-GN-Presets/commit/587f9a4)
- **Set Geometry Size** supports menu for Proportional and Fit. Proportional is set by default; geometry size is determined by the maximum bounding box size scaled to the required size. Fit tries to scale geometry to fit into the required size.[(ec71d44)](https://github.com/Tams3d/T3D-GN-Presets/commit/ec71d44)
- **Point Honeycomb** Centers to Origin ignoring offsets. [(77278e8)](https://github.com/Tams3d/T3D-GN-Presets/commit/77278e8)
- Replaced deprecated nodes with suitable Rotation nodes.

### 🚨 Deprecated Features

- Instances are no longer internally supported. _Realize Instances_ must be explicitly used in case of **Instances**. This change is made to support _Depth_ in Realize Instances.
- Mesh can no longer be converted to Fields, depreciated **Mesh To Field**
- UV nodes requires mandatory UV input. Accesing Default UVMap attribute is no longer supported.
- **Vertex Slide** is deprecated due to its instability and unsuitable use cases.

> [!NOTE]  
> Nodes with geometry input only support **Mesh, Curves, Point Clouds**

## 🪛 Compatibility

- Make sure to have a supported **Blender** version and the corresponding addon version.
- Nodes with Menu, Rotation and Matrix sockets are _not_ compatible with Blender versions 4.1 and below.
- Changes in newer addon versions are not retained for files migrated from older versions to newer versions, as nodes are only appended, not [linked](https://github.com/Tams3d/T3D-GN-Presets/blob/main/__init__.py#L156).
- In case of any **missing data blocks**, raise an issue [here](https://github.com/Tams3d/T3D-GN-Presets/issues)

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

- Hey! I am **Tamil Selvan**, also known as **tams_3d**. I am a 17-year-old self-taught Blender artist from **India**.
- My vision is to create _free_ tools for Blender, which require complex setups provided in a simplified and effective way.
- I am currently developing presets for Geometry Nodes that are similar to tools and features of other 3D packages and some add-ons.
- I believe that my work contributes to a better world for 3D artists, game developers, and other artists who create incredible works.

## 🥂 Socials

Catch up with me here:

- [Behance](https://www.behance.net/tamilselvan3d)
- [Blender Extensions](https://extensions.blender.org/add-ons/t3d-gn-presets/)
- [GitHub](https://github.com/Tams3d)
- [X](https://x.com/Tams_3d)
