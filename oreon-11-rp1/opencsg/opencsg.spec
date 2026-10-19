%global source0_hash 5ac5df73b1ad3340dd6705ff90e009f1a946bb9536c21c2263a6f974265664c0
Name:           opencsg
Version:        1.8.2
Release:        1%{?dist}
Summary:        Library for Constructive Solid Geometry using OpenGL
License:        GPL-2.0-or-later AND MIT-Khronos-old AND WTFPL AND Apache-2.0
URL:            https://www.opencsg.org/
Source0:        https://www.opencsg.org/OpenCSG-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.

CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by
taking the union of them, by intersecting them, or by subtracting one shape
of the other. The most basic shapes, which are not result of such a CSG
operation, are called primitives. Primitives must be solid, i.e., they must
have a clearly defined interior and exterior. By construction, a CSG shape is
also solid then.

Image-based CSG rendering (also z-buffer CSG rendering) is a term that denotes
algorithms for rendering CSG shapes without an explicit calculation of the
geometric boundary of a CSG shape. Such algorithms use frame-buffer settings
of the graphics hardware, e.g., the depth and stencil buffer, to compose CSG
shapes. OpenCSG implements a variety of those algorithms, namely the
Goldfeather algorithm and the SCS algorithm, both of them in several variants.

%package devel
Summary: OpenCSG development files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for OpenCSG.

%package doc
Summary: OpenCSG documentation
BuildArch: noarch
%description doc
Documentation for OpenCSG.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n OpenCSG-%{version}

# Encoding
iconv --from=ISO-8859-1 --to=UTF-8 changelog.txt > changelog.txt.new && \
touch -r changelog.txt changelog.txt.new && \
mv changelog.txt.new changelog.txt

%build

%cmake -DBUILD_EXAMPLE=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n opencsg-devel -f %{oreon_filedir}/opencsg-devel.list
%files -n opencsg-doc -f %{oreon_filedir}/opencsg-doc.list

%changelog

%autochangelog
