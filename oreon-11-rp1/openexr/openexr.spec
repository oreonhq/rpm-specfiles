%global source0_hash 61559d6d0657f228f8dd5e3165ed6b74437b95e81849ad41c6d3493c0c144c1d
%global sover 34
Name:           openexr
Version:        3.5.1
Release:        1%{?dist}
Summary:        Tools and libraries for ILM's OpenEXR high dynamic-range image format
License:        BSD-3-Clause
URL:            https://www.openexr.com/
Source0:        https://github.com/AcademySoftwareFoundation/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  imath-devel
BuildRequires:  libdeflate-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
OpenEXR runtime libraries, documentation, and simple image utilities.

%package        libs
Summary:        OpenEXR runtime libraries
%description    libs
Shared libraries for reading and writing OpenEXR images.

%package        devel
Summary:        Headers and CMake for OpenEXR
Requires:       openexr-libs%{?_isa} = %{version}-%{release}
%description    devel
Development files for OpenEXR 3.x.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir openexr-%{version}
%oreon_prep
%build

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF \
  -DOPENEXR_BUILD_TOOLS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n openexr-libs -f %{oreon_filedir}/openexr-libs.list
%files -n openexr-devel -f %{oreon_filedir}/openexr-devel.list

%changelog

%autochangelog
