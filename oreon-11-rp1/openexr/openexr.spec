%global source0_hash 0ffbd842a7ee2128d44affdea30f42294b4061293cde3aa75b61a53573413d1e

Name:           openexr
Version:        3.3.3
Release:        6%{?dist}
Summary:        Tools and libraries for ILM's OpenEXR high dynamic-range image format
License:        BSD-3-Clause
URL:            https://www.openexr.com/
Source0:        https://github.com/AcademySoftwareFoundation/openexr/archive/v3.3.3/openexr-3.3.3.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  imath-devel
BuildRequires:  libdeflate-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zlib)

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n openexr-%{version} -p1


%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF \
  -DOPENEXR_BUILD_TOOLS=ON
%cmake_build


%install
%cmake_install


%files
%{_bindir}/*

%files libs
# libOpenEXR* would also match libOpenEXRCore / libOpenEXRUtil and double-list files
%{_libdir}/libIex-3_3.so.*
%{_libdir}/libIlmThread-3_3.so.*
%{_libdir}/libOpenEXR-3_3.so.*
%{_libdir}/libOpenEXRCore-3_3.so.*
%{_libdir}/libOpenEXRUtil-3_3.so.*

%files devel
%{_includedir}/OpenEXR
%{_libdir}/libIex.so
%{_libdir}/libIex-3_3.so
%{_libdir}/libIlmThread.so
%{_libdir}/libIlmThread-3_3.so
%{_libdir}/libOpenEXR.so
%{_libdir}/libOpenEXR-3_3.so
%{_libdir}/libOpenEXRCore.so
%{_libdir}/libOpenEXRCore-3_3.so
%{_libdir}/libOpenEXRUtil.so
%{_libdir}/libOpenEXRUtil-3_3.so
%{_libdir}/cmake/OpenEXR
%{_libdir}/pkgconfig/OpenEXR.pc
%{_docdir}/OpenEXR/examples


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.3-2
- Add OpenEXR 3 for HDR imaging
