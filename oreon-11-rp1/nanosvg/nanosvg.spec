%global source0_hash 700f6c7b246a9d132fdc061f167df20b87312bc6d9bc2fc68034b1ad7cd24307
%global commit abcd277ea45e9098bed752cf9c6875b533c0892f
Name:		nanosvg
Version:	20221221
Release:        9%{?dist}
License:	Zlib
URL:		https://github.com/fltk/nanosvg
Source0:        https://github.com/fltk/%{name}/archive/%{commit}.tar.gz
Patch0:		nanosvg-sover.patch
Patch1:		nanosvg-lib64.patch
Patch2:		nanosvg-build-examples.patch
Summary:        Simple stupid SVG parser
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glfw-devel
BuildRequires:  libglvnd-devel
# /oreon:deps
%description
NanoSVG is a simple stupid single-header-file SVG parse. The output of the
parser is a list of cubic bezier shapes. The library suits well for
anything from rendering scalable icons in your editor application to
prototyping a game.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for nanosvg
%description devel
Development files for nanosvg.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .sover
%patch -P1 -p1 -b .lib64
%patch -P2 -p1 -b .build-examples

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd example
../%{__cmake_builddir}/example/example2
popd
%files -f %{oreon_filedir}/main.list
%files -n nanosvg-devel -f %{oreon_filedir}/nanosvg-devel.list

%changelog

%autochangelog
