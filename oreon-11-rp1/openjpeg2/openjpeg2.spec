%global source0_hash 368fe0468228e767433c9ebdea82ad9d801a3ad1e4234421f352c8b06e7aa707

Name:           openjpeg2
Version:        2.5.3
Release:        6%{?dist}
Summary:        JPEG 2000 codec library
License:        BSD-2-Clause
URL:            https://www.openjpeg.org/
Source0:        https://github.com/uclouvain/openjpeg/archive/v2.5.3/openjpeg-2.5.3.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  ninja-build
BuildRequires:  zlib-devel

%description
OpenJPEG is an open-source JPEG 2000 codec released under the BSD license.


%package        libs
Summary:        OpenJPEG runtime libraries

%description    libs
Shared libraries for JPEG 2000.

%package        devel
Summary:        Development files for OpenJPEG
Requires:       openjpeg2-libs%{?_isa} = %{version}-%{release}

%description    devel
Headers and CMake files for OpenJPEG 2.x.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n openjpeg-%{version} -p1


%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF
%cmake_build


%install
%cmake_install


%files
%{_bindir}/opj_*

%files libs
# Upstream may expose either SONAME branch (2.x) or API revision (7); list both
%{_libdir}/libopenjp2.so.2*
%{_libdir}/libopenjp2.so.7*

%files devel
%{_includedir}/openjpeg-2.5/
%{_libdir}/libopenjp2.so
%{_libdir}/libopenjp2.a
%{_libdir}/cmake/openjpeg-2.5/
%{_libdir}/pkgconfig/libopenjp2.pc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.3-2
- Add OpenJPEG2 for PDF and imaging stacks
