Name:           jxrlib
Version:        1.2
Release:        0.5.git20170615%{?dist}
Summary:        JPEG XR reference library
License:        BSD-2-Clause
URL:            https://git.debian.org/git/phototools/jxrlib.git
# Reproducible upstream snapshot used by Debian
Source0:        https://deb.debian.org/debian/pool/main/j/jxrlib/jxrlib_1.2~git20170615.f752187.orig.tar.xz
# CMake build from Debian (upstream tarball is Makefile-only at top level)
Source1:        jxrlib-CMakeLists.txt
Patch0:         jxrlib-01-linux-portability.patch
# oreon url source checksums begin
%global source0_sha256 3e3c9d3752b0bbf018ed9ce01b43dcd4be866521dc2370dc9221520b5bd440d4
%global source0_file jxrlib_1.2~git20170615.f752187.orig.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jxrlib_1.2~git20170615.f752187.orig.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3e3c9d3752b0bbf018ed9ce01b43dcd4be866521dc2370dc9221520b5bd440d4" || { echo "oreon: Source0 SHA256 mismatch for jxrlib_1.2~git20170615.f752187.orig.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n jxrlib-1.2~git20170615.f752187
# CRLF in a few sources breaks unified diffs
sed -i 's/\r$//' jxrgluelib/JXRGlueJxr.c jxrencoderdecoder/JxrEncApp.c jxrencoderdecoder/JxrDecApp.c
%patch 0 -p1
install -m0644 %{SOURCE1} CMakeLists.txt


%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS=ON \
  -DJXRLIB_INSTALL_LIB_DIR=%{_lib} \
  -DJXRLIB_INSTALL_BIN_DIR=bin \
  -DJXRLIB_INSTALL_INCLUDE_DIR=include/jxrlib
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
