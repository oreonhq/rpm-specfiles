%global source0_hash 59c12500b7c2fc426e89667b3e4f3fdc2ff05a75cc12001a22c5f58fb1cdf592
Name:           thorvg
Version:        1.1.1
Release:        1%{?dist}
Summary:        Lightweight vector-based scenes and animation drawing library
License:        MIT
URL:            https://www.thorvg.org/
Source0:        https://github.com/thorvg/thorvg/archive/v%{version}/thorvg-%{version}.tar.gz
Patch:          binarynameconflicts.patch
Provides: bundled(rapidjson)
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sdl2)
# /oreon:deps
%description
ThorVG is an open-source graphics library designed for creating vector-based
scenes and animations. It combines immense power with remarkable lightweight
efficiency, as Thor embodies a dual meaning—symbolizing both thunderous
strength and lightning-fast agility. Embracing the philosophy of simpler is
better, the ThorVG project provides intuitive, user-friendly interfaces while
maintaining a compact footprint and minimal overhead.

The following list shows primitives that are supported by ThorVG:
- Lines & Shapes: rectangles, circles, and paths with coordinate control
- Filling: solid colors, linear & radial gradients, and path clipping
- Stroking: stroke width, joins, caps, dash patterns, and trimming
- Scene Management: retainable scene graph and object transformations
- Composition: various blending and masking
- Text: unicode characters with horizontal text layout using scalable fonts (TTF)
- Images: SVG, JPG, PNG, WebP, and raw bitmaps
- Effects: blur, drop shadow, fill, tint, tritone and color replacement
- Animations: Lottie

%package devel
Summary: Development headres and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and libraries for ThorVG.

%package doc
Summary: Documentation
BuildArch:  noarch
%description doc
Docbook documentation for ThorVG.

%prep

%autosetup -n thorvg-%{version} -p1
# Generate docbook documentation
sed -i "s/GENERATE_DOCBOOK       = NO/GENERATE_DOCBOOK       = YES/g" docs/Doxyfile
sed -i "s/# DOCBOOK_PROGRAMLISTING = NO/ DOCBOOK_PROGRAMLISTING = YES/g" docs/Doxyfile
sed -i "s/GENERATE_HTML          = YES/GENERATE_HTML          = NO/g" docs/Doxyfile

%build

%meson -Dengines=all \
       -Dexamples=true \
       -Dloaders=all \
       -Dsavers=all \
       -Dbindings=capi \
       -Dtools=all \
       -Dstrip=false \
       -Dtests=true
%meson_build
pushd docs
doxygen
popd
%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/help/en/ThorVG
for file in docs/docbook/*.*
do
  install -m644 $file  %{buildroot}%{_datadir}/help/en/ThorVG
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n thorvg-devel -f %{oreon_filedir}/thorvg-devel.list
%files -n thorvg-doc -f %{oreon_filedir}/thorvg-doc.list

%changelog

%autochangelog
