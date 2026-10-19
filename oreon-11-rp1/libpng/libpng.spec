%global source0_hash 2540302a1844ad2b2b501977abecfa850f265f97b78f065a712ab4074a89f5b5
Summary:        A library of functions for manipulating PNG image format files
Name:          libpng
Epoch:         2
Version:       1.6.59
Release:        1%{?dist}
License:       zlib
URL:           http://www.libpng.org/pub/png/
Source0:        https://github.com/glennrp/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       pngusr.dfa
Patch0:        libpng-multilib.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  zlib-devel
# /oreon:deps
%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package devel
Summary:       Development tools for programs to manipulate PNG image format files
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      zlib-devel%{?_isa} pkgconfig
%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  You'll also need to install
the libpng package.

%package static
Summary:       Static PNG image format file library
Requires:      %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
%description static
The libpng-static package contains the statically linkable version of libpng.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%package tools
Summary:       Tools for PNG image format file library
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description tools
The libpng-tools package contains tools used by the authors of libpng.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
# Provide pngusr.dfa for build.
cp -p %{SOURCE1} .

%patch -P0 -p1

%build

%cmake -DDFA_XTRA=pngusr.dfa
%cmake_build
%install
%cmake_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%ctest
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libpng-devel -f %{oreon_filedir}/libpng-devel.list
%files -n libpng-static -f %{oreon_filedir}/libpng-static.list
%files -n libpng-tools -f %{oreon_filedir}/libpng-tools.list

%changelog

%autochangelog
