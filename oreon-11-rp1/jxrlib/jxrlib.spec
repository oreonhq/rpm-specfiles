Name:           jxrlib
Version:        1.2
Release:        0.2.git20170615%{?dist}
Summary:        JPEG XR reference library
License:        BSD-2-Clause
URL:            https://git.debian.org/git/phototools/jxrlib.git
# Reproducible upstream snapshot used by Debian
Source0:        https://snapshot.debian.org/archive/debian-archive/20221221T204908Z/debian/pool/main/j/jxrlib/jxrlib_1.2~git20170615.f752187.orig.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build

%description
libjpegxr and libjxrglue implement the JPEG XR still image format.


%package        libs
Summary:        JPEG XR shared libraries

%description    libs
Runtime libraries for JPEG XR.

%package        devel
Summary:        Development files for jxrlib
Requires:       jxrlib-libs%{?_isa} = %{version}-%{release}

%description    devel
Headers for building against jxrlib.


%prep
%autosetup -p1 -n jxrlib-1.2~git20170615.f752187


%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS=ON
%cmake_build


%install
%cmake_install


%files
%{_bindir}/JxrEncApp
%{_bindir}/JxrDecApp

%files libs
%{_libdir}/libjpegxr.so.*
%{_libdir}/libjxrglue.so.*

%files devel
%{_includedir}/jxrlib/
%{_libdir}/libjpegxr.so
%{_libdir}/libjxrglue.so


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-0.2.git20170615
- Add jxrlib snapshot for legacy JPEG XR media
