# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ae498e10fadeba0c2e7aa86c71cc9989c4d895201cd26b8b72061c76cfde4edf
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit a7d4c2175630e1ea5b6f8dd00ab96fed0b97b96d
%global snapdate 20261009

%bcond stb_include 0
%bcond stb_image_resize 1
%bcond stb_sprintf %[ %{defined fc45} || %{defined fc44} || %{defined fc43} || %{defined el10} || %{defined oreon} ]
%bcond doc %[ %{defined fc45} || %{defined fc44} || %{defined fc43} || %{defined el10} || %{defined oreon} ]
%bcond devel_metapackage %[ %{defined fc45} || %{defined fc44} || %{defined fc43} || %{defined el10} || %{defined oreon} ]
%bcond mlpack_arched_dep %[ %{defined fc45} || %{defined fc44} || %{defined fc43} || %{defined el9} || %{defined oreon} ]

Name:           stb
%global snapinfo ^%{snapdate}.%{sub %{commit} 1 7}
Version:        0%{snapinfo}
Release:        %{autorelease}
Summary:        Single-file public domain libraries for C/C++

%global main_license MIT OR Unlicense
%global stb_include_license LicenseRef-Fedora-Public-Domain
%global stb_herringbone_wang_tile_license %{shrink:
    LicenseRef-Fedora-Public-Domain OR LicenseRef-Fedora-UltraPermissive
    }
License:        (%{main_license}) %{shrink:
    %{?with_stb_include:AND %{stb_include_license}}
    AND (%{stb_herringbone_wang_tile_license})
    }
SourceLicense:  (%{main_license}) %{shrink:
    AND %{stb_include_license}
    AND MIT
    AND (%{stb_herringbone_wang_tile_license})
    }
URL:            https://github.com/nothings/stb
Source0:        %{url}/archive/%{commit}/stb-%{commit}.tar.gz

Patch:          1194.patch
Patch:          1195.patch
Patch:          1196.patch
Patch:          1198.patch
Patch:          1236.patch
Patch:          1454.patch
Patch:          1530.patch
Patch:          1532.patch
Patch:          1534.patch
Patch:          1539.patch
Patch:          1541.patch
Patch:          1543.patch
Patch:          0001-Fix-double-free-in-stbi__load_gif_main_outofmem.patch

Patch:          0002-Fix-possible-double-free-or-memory-leak-in-stbi__loa.patch

Patch:          0001-Fix-Null-pointer-dereference-because-of-an-uninitial.patch

Patch:          1553.patch
Patch: fix-riscv64-compile-uintptr.patch

Patch:          1559.patch
Patch:          1736.patch
Patch:          pr-1862.patch

Patch:          1863.patch
Patch:          issue-1929.patch

Patch:          cve-2026-79516.patch

%global stb_c_lexer_version 0.12
%global stb_connected_components_version 0.96
%global stb_divide_version 0.94
%global stb_ds_version 0.67
%global stb_dxt_version 1.12
%global stb_easy_font_version 1.1
%global stb_herringbone_wang_tile_version 0.7
%global stb_hexwave_version 0.5
%global stb_image_version 2.30
%if %{with stb_image_resize}
%global stb_image_resize_version 0.97
%endif
%global stb_image_write_version 1.16
%if %{with stb_include}
%global stb_include_version 0.2
%endif
%global stb_leakcheck_version 0.6
%global stb_perlin_version 0.5
%global stb_rect_pack_version 1.1
%if %{with stb_sprintf}
%global stb_sprintf_version 1.10
%endif
%global stb_textedit_version 1.14
%global stb_tilemap_editor_version 0.42
%global stb_truetype_version 1.26
%global stb_vorbis_version 1.22
%global stb_voxel_render_version 0.89

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  make

BuildRequires:  /usr/bin/convert

%global debug_package %{nil}

%description
%{summary}.

%if %{with devel_metapackage}
%package devel
Summary:        Development files for stb

BuildArch:      noarch

Provides:       stb-static = %{version}-%{release}

Requires:       stb_c_lexer-devel = %{stb_c_lexer_version}%{snapinfo}-%{release}
Requires:       stb_c_lexer-static = %{stb_c_lexer_version}%{snapinfo}-%{release}
Requires:       stb_connected_components-devel = %{stb_connected_components_version}%{snapinfo}-%{release}
Requires:       stb_connected_components-static = %{stb_connected_components_version}%{snapinfo}-%{release}
Requires:       stb_divide-devel = %{stb_divide_version}%{snapinfo}-%{release}
Requires:       stb_divide-static = %{stb_divide_version}%{snapinfo}-%{release}
Requires:       stb_ds-devel = %{stb_ds_version}%{snapinfo}-%{release}
Requires:       stb_ds-static = %{stb_ds_version}%{snapinfo}-%{release}
Requires:       stb_dxt-devel = %{stb_dxt_version}%{snapinfo}-%{release}
Requires:       stb_dxt-static = %{stb_dxt_version}%{snapinfo}-%{release}
Requires:       stb_easy_font-devel = %{stb_easy_font_version}%{snapinfo}-%{release}
Requires:       stb_easy_font-static = %{stb_easy_font_version}%{snapinfo}-%{release}
Requires:       stb_herringbone_wang_tile-devel = %{stb_herringbone_wang_tile_version}%{snapinfo}-%{release}
Requires:       stb_herringbone_wang_tile-static = %{stb_herringbone_wang_tile_version}%{snapinfo}-%{release}
Requires:       stb_hexwave-devel = %{stb_hexwave_version}%{snapinfo}-%{release}
Requires:       stb_hexwave-static = %{stb_hexwave_version}%{snapinfo}-%{release}
Requires:       stb_image-devel = %{stb_image_version}%{snapinfo}-%{release}
Requires:       stb_image-static = %{stb_image_version}%{snapinfo}-%{release}
%if %{with stb_image_resize} && %{defined el9}
Requires:       stb_image_resize-devel = %{stb_image_resize_version}%{snapinfo}-%{release}
Requires:       stb_image_resize-static = %{stb_image_resize_version}%{snapinfo}-%{release}
%endif
Requires:       stb_image_resize2-devel
Requires:       stb_image_resize2-static
Requires:       stb_image_write-devel = %{stb_image_write_version}%{snapinfo}-%{release}
Requires:       stb_image_write-static = %{stb_image_write_version}%{snapinfo}-%{release}
%if %{with stb_include}
Requires:       stb_include-devel = %{stb_include_version}%{snapinfo}-%{release}
Requires:       stb_include-static = %{stb_include_version}%{snapinfo}-%{release}
%endif
Requires:       stb_leakcheck-devel = %{stb_leakcheck_version}%{snapinfo}-%{release}
Requires:       stb_leakcheck-static = %{stb_leakcheck_version}%{snapinfo}-%{release}
Requires:       stb_perlin-devel = %{stb_perlin_version}%{snapinfo}-%{release}
Requires:       stb_perlin-static = %{stb_perlin_version}%{snapinfo}-%{release}
Requires:       stb_rect_pack-devel = %{stb_rect_pack_version}%{snapinfo}-%{release}
Requires:       stb_rect_pack-static = %{stb_rect_pack_version}%{snapinfo}-%{release}
%if %{with stb_sprintf}
Requires:       stb_sprintf-devel = %{stb_sprintf_version}%{snapinfo}-%{release}
Requires:       stb_sprintf-static = %{stb_sprintf_version}%{snapinfo}-%{release}
%endif
Requires:       stb_textedit-devel = %{stb_textedit_version}%{snapinfo}-%{release}
Requires:       stb_textedit-static = %{stb_textedit_version}%{snapinfo}-%{release}
Requires:       stb_tilemap_editor-devel = %{stb_tilemap_editor_version}%{snapinfo}-%{release}
Requires:       stb_tilemap_editor-static = %{stb_tilemap_editor_version}%{snapinfo}-%{release}
Requires:       stb_truetype-devel = %{stb_truetype_version}%{snapinfo}-%{release}
Requires:       stb_truetype-static = %{stb_truetype_version}%{snapinfo}-%{release}
Requires:       stb_vorbis-devel = %{stb_vorbis_version}%{snapinfo}-%{release}
Requires:       stb_vorbis-static = %{stb_vorbis_version}%{snapinfo}-%{release}
Requires:       stb_voxel_render-devel = %{stb_voxel_render_version}%{snapinfo}-%{release}
Requires:       stb_voxel_render-static = %{stb_voxel_render_version}%{snapinfo}-%{release}

%description devel
The stb-devel package contains libraries and header files for developing
applications that use stb.

This is a metapackage that requires the -devel packages for all stb libraries.
%endif

%package -n stb_c_lexer-devel
Summary:        Simplify writing parsers for C-like languages
Version:        %{stb_c_lexer_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_c_lexer-static = %{stb_c_lexer_version}%{snapinfo}-%{release}

%description -n stb_c_lexer-devel
Lexer for making little C-like languages with recursive-descent parsers.

%package -n stb_connected_components-devel
Summary:        Incrementally compute reachability on grids
Version:        %{stb_connected_components_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_connected_components-static = %{stb_connected_components_version}%{snapinfo}-%{release}

%description -n stb_connected_components-devel
Finds connected components on 2D grids for testing reachability between two
points, with fast updates when changing reachability (e.g. on one machine it
was typically 0.2ms w/ 1024x1024 grid). Each grid square must be “open” or
“closed” (traversable or untraversable), and grid squares are only connected to
their orthogonal neighbors, not diagonally.

%package -n stb_divide-devel
Summary:        More useful 32-bit modulus e.g. “Euclidean divide”
Version:        %{stb_divide_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_divide-static = %{stb_divide_version}%{snapinfo}-%{release}

%description -n stb_divide-devel
This file provides three different consistent divide/mod pairs
implemented on top of arbitrary C/C++ division, including correct
handling of overflow of intermediate calculations:

    trunc:   a/b truncates to 0,           a%b has same sign as a
    floor:   a/b truncates to -inf,        a%b has same sign as b
    eucl:    a/b truncates to sign(b)*inf, a%b is non-negative

%package -n stb_ds-devel
Summary:        Typesafe dynamic array and hash tables for C, will compile in C++
Version:        %{stb_ds_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_ds-static = %{stb_ds_version}%{snapinfo}-%{release}

%description -n stb_ds-devel
This is a single-header-file library that provides easy-to-use dynamic arrays
and hash tables for C (also works in C++).

For a gentle introduction: https://nothings.org/stb_ds

%package -n stb_dxt-devel
Summary:        Fabian “ryg” Giesen’s real-time DXT compressor
Version:        %{stb_dxt_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_dxt-static = %{stb_dxt_version}%{snapinfo}-%{release}

%description -n stb_dxt-devel
DXT1/DXT5 compressor.

%package -n stb_easy_font-devel
Summary:        Quick-and-dirty easy-to-deploy bitmap font for printing frame rate, etc
Version:        %{stb_easy_font_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_easy_font-static = %{stb_easy_font_version}%{snapinfo}-%{release}

%description -n stb_easy_font-devel
   Easy-to-deploy,
   reasonably compact,
   extremely inefficient performance-wise,
   crappy-looking,
   ASCII-only,
   bitmap font for use in 3D APIs.

Intended for when you just want to get some text displaying in a 3D app as
quickly as possible.

Doesn’t use any textures, instead builds characters out of quads.

%package -n stb_herringbone_wang_tile-devel
Summary:        Herringbone Wang tile map generator
Version:        %{stb_herringbone_wang_tile_version}%{snapinfo}
License:        %{stb_herringbone_wang_tile_license}

BuildArch:      noarch

Provides:       stb_herringbone_wang_tile-static = %{stb_herringbone_wang_tile_version}%{snapinfo}-%{release}

%description -n stb_herringbone_wang_tile-devel
This library is an SDK for Herringbone Wang Tile generation:

     http://nothings.org/gamedev/herringbone

The core design is that you use this library offline to generate a “template”
of the tiles you’ll create. You then edit those tiles, then load the created
tile image file back into this library and use it at runtime to generate
“maps”.

You cannot load arbitrary tile image files with this library; it is only
designed to load image files made from the template it created. It stores a
binary description of the tile sizes & constraints in a few pixels, and uses
those to recover the rules, rather than trying to parse the tiles themselves.

You *can* use this library to generate from arbitrary tile sets, but only by
loading the tile set and specifying the constraints explicitly yourself.

%package -n stb_hexwave-devel
Summary:        Audio waveform synthesizer
Version:        %{stb_hexwave_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_hexwave-static = %{stb_hexwave_version}%{snapinfo}-%{release}

%description -n stb_hexwave-devel
A flexible anti-aliased (bandlimited) digital audio oscillator.

This library generates waveforms of a variety of shapes made of line segments.
It does not do envelopes, LFO effects, etc.; it merely tries to solve the
problem of generating an artifact-free morphable digital waveform with a
variety of spectra, and leaves it to the user to rescale the waveform and mix
multiple voices, etc.

%package -n stb_image-devel
Summary:        Image loading/decoding from file/memory: JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC
Version:        %{stb_image_version}%{snapinfo}
License:        %{main_license}

%if %{without mlpack_arched_dep}
BuildArch:      noarch
%endif

Provides:       stb_image-static = %{stb_image_version}%{snapinfo}-%{release}

%description -n stb_image-devel
%{summary}.

Primarily of interest to game developers and other people who can avoid
problematic images and only need the trivial interface.

%if %{with stb_image_resize}
%package -n stb_image_resize-devel
Summary:        Resize images larger/smaller with good quality (original version)
Version:        %{stb_image_resize_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_image_resize-static = %{stb_image_resize_version}%{snapinfo}-%{release}

%description -n stb_image_resize-devel
Image resizing.

Written with emphasis on usability, portability, and efficiency. (No SIMD or
threads, so it be easily outperformed by libs that use those.) Only scaling and
translation is supported, no rotations or shears. Easy API downsamples
w/Mitchell filter, upsamples w/cubic interpolation.

This is the original version of the stb_image_resize library. It has been
deprecated by its developer; consider porting to stb_image_resize2 instead.
%endif

%package -n stb_image_write-devel
Summary:        Image writing to disk: PNG, TGA, BMP
Version:        %{stb_image_write_version}%{snapinfo}
License:        %{main_license}

%if %{without mlpack_arched_dep}
BuildArch:      noarch
%endif

Provides:       stb_image_write-static = %{stb_image_write_version}%{snapinfo}-%{release}

%description -n stb_image_write-devel
This header file is a library for writing images to C stdio or a callback.

The PNG output is not optimal; it is 20-50%% larger than the file written by a
decent optimizing implementation; though providing a custom zlib compress
function (see STBIW_ZLIB_COMPRESS) can mitigate that. This library is designed
for source code compactness and simplicity, not optimal image file size or
run-time performance.

%if %{with stb_include}
%package -n stb_include-devel
Summary:        Implement recursive #include support, particularly for GLSL
Version:        %{stb_include_version}%{snapinfo}
License:        %{stb_include_license}

BuildArch:      noarch

Provides:       stb_include-static = %{stb_include_version}%{snapinfo}-%{release}

%description -n stb_include-devel
This program parses a string and replaces lines of the form
with the contents of a file named "foo". It also embeds the appropriate #line
directives. Note that all include files must reside in the location specified
in the path passed to the API; it does not check multiple directories.

If the string contains a line of the form
then it will be replaced with the contents of the string ‘inject’ passed to the
API.
%endif

%package -n stb_leakcheck-devel
Summary:        Quick-and-dirty malloc/free leak-checking
Version:        %{stb_leakcheck_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_leakcheck-static = %{stb_leakcheck_version}%{snapinfo}-%{release}

%description -n stb_leakcheck-devel
%{summary}.

%package -n stb_perlin-devel
Summary:        Perlin’s revised simplex noise w/ different seeds
Version:        %{stb_perlin_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_perlin-static = %{stb_perlin_version}%{snapinfo}-%{release}

%description -n stb_perlin-devel
%{summary}.

%package -n stb_rect_pack-devel
Summary:        Simple 2D rectangle packer with decent quality
Version:        %{stb_rect_pack_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_rect_pack-static = %{stb_rect_pack_version}%{snapinfo}-%{release}

%description -n stb_rect_pack-devel
Useful for e.g. packing rectangular textures into an atlas. Does not do
rotation.

Not necessarily the awesomest packing method, but better than the totally naive
one in stb_truetype (which is primarily what this is meant to replace).

No memory allocations; uses qsort() and assert() from stdlib. Can override
those by defining STBRP_SORT and STBRP_ASSERT.

This library currently uses the Skyline Bottom-Left algorithm.

Please note: better rectangle packers are welcome! Please implement them to the
same API, but with a different init function.

%if %{with stb_sprintf}
%package -n stb_sprintf-devel
Summary:        Fast sprintf, snprintf for C/C++
Version:        %{stb_sprintf_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_sprintf-static = %{stb_sprintf_version}%{snapinfo}-%{release}

%description -n stb_sprintf-devel
This is a full sprintf replacement that supports everything that the C runtime
sprintfs support, including float/double, 64-bit integers, hex floats, field
parameters (%%*.*d stuff), length reads backs, etc.

Why would you need this if sprintf already exists? Well, first off, it’s *much*
faster (see below). It’s also much smaller than the CRT versions
code-space-wise. We’ve also added some simple improvements that are super handy
(commas in thousands, callbacks at buffer full, for example). Finally, the
format strings for MSVC and GCC differ for 64-bit integers (among other small
things), so this lets you use the same format strings in cross platform code.

It uses the standard single file trick of being both the header file and the
source itself. If you just include it normally, you just get the header file
function definitions. To get the code, you include it from a C or C++ file and
define STB_SPRINTF_IMPLEMENTATION first.

It only uses va_args macros from the C runtime to do its work. It does cast
doubles to S64s and shifts and divides U64s, which does drag in CRT code on
most platforms.

It compiles to roughly 8K with float support, and 4K without. As a comparison,
when using MSVC static libs, calling sprintf drags in 16K.
%endif

%package -n stb_textedit-devel
Summary:        Guts of a text editor for games etc., implementing them from scratch
Version:        %{stb_textedit_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_textedit-static = %{stb_textedit_version}%{snapinfo}-%{release}

%description -n stb_textedit-devel
This C header file implements the guts of a multi-line text-editing widget; you
implement display, word-wrapping, and low-level string insertion/deletion, and
stb_textedit will map user inputs into insertions & deletions, plus updates to
the cursor position, selection state, and undo state.

It is intended for use in games and other systems that need to build their own
custom widgets and which do not have heavy text-editing requirements (this
library is not recommended for use for editing large texts, as its performance
does not scale and it has limited undo).

Non-trivial behaviors are modeled after Windows text controls.

%package -n stb_tilemap_editor-devel
Summary:        Embeddable tilemap editor
Version:        %{stb_tilemap_editor_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_tilemap_editor-static = %{stb_tilemap_editor_version}%{snapinfo}-%{release}

%description -n stb_tilemap_editor-devel
Embeddable tilemap editor for C/C++.

%package -n stb_truetype-devel
Summary:        Parse, decode, and rasterize characters from TrueType fonts
Version:        %{stb_truetype_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_truetype-static = %{stb_truetype_version}%{snapinfo}-%{release}

%description -n stb_truetype-devel
%{summary}.
=======================================================================

   NO SECURITY GUARANTEE -- DO NOT USE THIS ON UNTRUSTED FONT FILES

This library does no range checking of the offsets found in the file,
meaning an attacker can use it to read arbitrary memory.

=======================================================================

This library processes TrueType files:
  • parse files
  • extract glyph metrics
  • extract glyph shapes
  • render glyphs to one-channel bitmaps with antialiasing (box filter)
  • render glyphs to one-channel SDF bitmaps (signed-distance field/function)

%package -n stb_vorbis-devel
Summary:        Decode Ogg Vorbis files from file/memory to float/16-bit signed output
Version:        %{stb_vorbis_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_vorbis-static = %{stb_vorbis_version}%{snapinfo}-%{release}

%description -n stb_vorbis-devel
Ogg Vorbis audio decoder.

%package -n stb_voxel_render-devel
Summary:        Helps render large-scale “voxel” worlds for games
Version:        %{stb_voxel_render_version}%{snapinfo}
License:        %{main_license}

BuildArch:      noarch

Provides:       stb_voxel_render-static = %{stb_voxel_render_version}%{snapinfo}-%{release}

%description -n stb_voxel_render-devel
This library helps render large-scale “voxel” worlds for games, in this case,
one with blocks that can have textures and that can also be a few shapes other
than cubes.

   Video introduction:
      http://www.youtube.com/watch?v=2vnTtiLrV1w

   Minecraft-viewer sample app (not very simple though):
      http://github.com/nothings/stb/tree/master/tests/caveview

It works by creating triangle meshes. The library includes

   - converter from dense 3D arrays of block info to vertex mesh
   - vertex & fragment shaders for the vertex mesh
   - assistance in setting up shader state

For portability, none of the library code actually accesses the 3D graphics
API. (At the moment, it’s not actually portable since the shaders are GLSL
only, but patches are welcome.)

You have to do all the caching and tracking of vertex buffers yourself.
However, you could also try making a game with a small enough world that it’s
fully loaded rather than streaming. Currently the preferred vertex format is 20
bytes per quad. There are designs to allow much more compact formats with a
slight reduction in shader features, but no roadmap for actually implementing
them.

%if %{with doc}
%package doc
Summary:        Documentation for stb
License:        %{main_license}

BuildArch:      noarch

%description doc
Documentation for stb.
%endif

%prep
%oreon_sha256
%autosetup -n stb-%{commit} -p1

sed --regexp-extended --in-place \
    --expression='s/([[:alpha:]]+FLAGS[[:blank:]]*)=/\1+=/' \
    --expression='s/(\$\(CC\))(.*)-std=[^[:blank:]]+/\$\(CXX\)\2/' \
    --expression='s/CPPFLAGS/CXXFLAGS/' \
    tests/Makefile

printf '%s\n' 'int main(int, char *[]) { return 0; }' \
    >> tests/test_cpp_compilation.cpp

find . -type f -name '*.exe' -print -delete

rm --recursive --verbose tests/caveview
find deprecated -type f \
     ! -name stb_image_resize.h \
     ! -name stb_image_resize2.h \
     ! -name stb_sprintf.h \
     -print -delete

%if %{without stb_include}
sed --regexp-extended --in-place \
    '/#include[[:blank:]]+"stb_include.h"/d' tests/test_c_compilation.c
%endif

%build
%make_build --directory=tests INCLUDES='-I.. -I../deprecated'

%install
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}/stb' stb_*.h stb_*.c
%if %{without stb_include}
rm '%{buildroot}%{_includedir}/stb/stb_include.h'
%endif
%if %{with stb_image_resize}
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}/stb' deprecated/stb_image_resize.h
%endif
%if %{with stb_sprintf}
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}/stb' deprecated/stb_sprintf.h
%endif
pushd '%{buildroot}%{_includedir}'
ln --symbolic --verbose stb/stb_*.? .
popd

%check

rm --verbose --force output
mkdir output
./tests/image_write_test
for img in wr6x5_flip.bmp wr6x5_flip.jpg wr6x5_flip.tga wr6x5_regular.hdr \
    wr6x5_regular.png wr6x5_flip.hdr wr6x5_flip.png wr6x5_regular.bmp \
    wr6x5_regular.jpg wr6x5_regular.tga
do
  convert "output/${img}" 'output/dummy.bmp'
done

while read -r version header
do
  %{?!with_stb_include:if [ "${header}" = 'stb_include.h' ]; then continue; fi}
  grep --extended-regexp "$(
    printf '%s\n' "${version}" |
    sed -r 's/([[:digit:]]+)\.([[:digit:]]+)/\\bv\1\\.0*\2\\b/'
  )" "%{buildroot}%{_includedir}/${header}" >/dev/null
done <<'EOF'
%{stb_c_lexer_version} stb_c_lexer.h
%{stb_connected_components_version} stb_connected_components.h
%{stb_divide_version} stb_divide.h
%{stb_ds_version} stb_ds.h
%{stb_dxt_version} stb_dxt.h
%{stb_easy_font_version} stb_easy_font.h
%{stb_herringbone_wang_tile_version} stb_herringbone_wang_tile.h
%{stb_hexwave_version} stb_hexwave.h
%{stb_image_version} stb_image.h
%if %{with stb_image_resize}
%{stb_image_resize_version} stb_image_resize.h
%endif
%{stb_image_write_version} stb_image_write.h
%if %{with stb_include}
%{stb_include_version} stb_include.h
%endif
%{stb_leakcheck_version} stb_leakcheck.h
%{stb_perlin_version} stb_perlin.h
%{stb_rect_pack_version} stb_rect_pack.h
%if %{with stb_sprintf}
%{stb_sprintf_version} stb_sprintf.h
%endif
%{stb_textedit_version} stb_textedit.h
%{stb_tilemap_editor_version} stb_tilemap_editor.h
%{stb_truetype_version} stb_truetype.h
%{stb_vorbis_version} stb_vorbis.c
%{stb_voxel_render_version} stb_voxel_render.h
EOF

%if %{with devel_metapackage}
%files devel
%endif

%if %{with doc}
%files doc
%license LICENSE
%doc docs
%doc README.md
%doc tests/tilemap_editor_integration_example.c
%endif

%files -n stb_c_lexer-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_c_lexer.h
%{_includedir}/stb_c_lexer.h

%files -n stb_connected_components-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_connected_components.h
%{_includedir}/stb_connected_components.h

%files -n stb_divide-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_divide.h
%{_includedir}/stb_divide.h

%files -n stb_ds-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_ds.h
%{_includedir}/stb_ds.h

%files -n stb_dxt-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_dxt.h
%{_includedir}/stb_dxt.h

%files -n stb_easy_font-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_easy_font.h
%{_includedir}/stb_easy_font.h

%files -n stb_herringbone_wang_tile-devel
%dir %{_includedir}/stb
%{_includedir}/stb/stb_herringbone_wang_tile.h
%{_includedir}/stb_herringbone_wang_tile.h

%files -n stb_hexwave-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_hexwave.h
%{_includedir}/stb_hexwave.h

%files -n stb_image-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_image.h
%{_includedir}/stb_image.h

%if %{with stb_image_resize}
%files -n stb_image_resize-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_image_resize.h
%{_includedir}/stb_image_resize.h
%endif

%files -n stb_image_write-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_image_write.h
%{_includedir}/stb_image_write.h

%if %{with stb_include}
%files -n stb_include-devel
%dir %{_includedir}/stb
%{_includedir}/stb/stb_include.h
%{_includedir}/stb_include.h
%endif

%files -n stb_leakcheck-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_leakcheck.h
%{_includedir}/stb_leakcheck.h

%files -n stb_perlin-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_perlin.h
%{_includedir}/stb_perlin.h

%files -n stb_rect_pack-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_rect_pack.h
%{_includedir}/stb_rect_pack.h

%if %{with stb_sprintf}
%files -n stb_sprintf-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_sprintf.h
%{_includedir}/stb_sprintf.h
%endif

%files -n stb_textedit-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_textedit.h
%{_includedir}/stb_textedit.h

%files -n stb_tilemap_editor-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_tilemap_editor.h
%{_includedir}/stb_tilemap_editor.h

%files -n stb_truetype-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_truetype.h
%{_includedir}/stb_truetype.h

%files -n stb_vorbis-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_vorbis.c
%{_includedir}/stb_vorbis.c

%files -n stb_voxel_render-devel
%license LICENSE
%dir %{_includedir}/stb
%{_includedir}/stb/stb_voxel_render.h
%{_includedir}/stb_voxel_render.h

%changelog
%autochangelog
