%global source0_hash 700f6c7b246a9d132fdc061f167df20b87312bc6d9bc2fc68034b1ad7cd24307

%global commit abcd277ea45e9098bed752cf9c6875b533c0892f

Name:		nanosvg
# This thing has no version so we'll use the last commit date
Version:	20221221
Release:	9%{?dist}
License:	Zlib
# Technically, this is a fork, but the upstream is unmaintained and this one has some fixes
URL:		https://github.com/fltk/nanosvg
Source0:	https://github.com/fltk/nanosvg/archive/%{commit}.tar.gz
# https://github.com/memononen/nanosvg/pull/246
Patch0:		nanosvg-sover.patch
# Idea taken from here, but their implementation didn't work
# https://github.com/memononen/nanosvg/pull/245
# using LIB_INSTALL_DIR seems to work better
Patch1:		nanosvg-lib64.patch
# Inspired by
# https://github.com/memononen/nanosvg/pull/216
# Modified slightly to work without an installed nanosvg instance
Patch2:		nanosvg-build-examples.patch
Summary:	Simple stupid SVG parser
BuildRequires:	cmake, gcc
# Needed for example1
BuildRequires:	libglvnd-devel, glfw-devel >= 3

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
# Note: We do not install the examples, they are not really useful outside of a testing context.

# Use example2 as a smoke test
%check
pushd example
../%{__cmake_builddir}/example/example2
popd

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libnanosvg.so.*
%{_libdir}/libnanosvgrast.so.*

%files devel
%{_includedir}/nanosvg/
%{_libdir}/cmake/NanoSVG
%{_libdir}/libnanosvg.so
%{_libdir}/libnanosvgrast.so

%changelog
%autochangelog
