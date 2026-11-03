%global source0_hash 98d35d11a78dc453aebb7d10c3748f3f73ff78c8267c0dc697b8631f67bf7e8f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: brotli
Version: 1.2.1
Release: 2%{?dist}
Summary: Lossless compression algorithm
License: MIT
URL: https://github.com/google/brotli
Source0: https://github.com/google/brotli/archive/v%{version}/brotli-%{version}.tar.gz
Requires: libbrotli%{?_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build

%description
Brotli is a generic-purpose lossless compression algorithm.

%package -n libbrotli
Summary: Brotli libraries

%description -n libbrotli
Shared brotli common, decoder and encoder libraries.

%package devel
Summary: Development files for brotli
Requires: libbrotli%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing against brotli.

%prep
%oreon_sha256
%autosetup -n brotli-%{version} -p1

%build
%oreon_cmake -DBROTLI_DISABLE_TESTS=ON
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%ldconfig_scriptlets -n libbrotli

%files
%license LICENSE
%{_bindir}/brotli
%{_mandir}/man1/brotli.1*

%files -n libbrotli
%license LICENSE
%{_libdir}/libbrotlicommon.so.1
%{_libdir}/libbrotlicommon.so.1.*
%{_libdir}/libbrotlidec.so.1
%{_libdir}/libbrotlidec.so.1.*
%{_libdir}/libbrotlienc.so.1
%{_libdir}/libbrotlienc.so.1.*

%files devel
%{_includedir}/brotli/
%{_libdir}/libbrotlicommon.so
%{_libdir}/libbrotlidec.so
%{_libdir}/libbrotlienc.so
%{_libdir}/pkgconfig/libbrotlicommon.pc
%{_libdir}/pkgconfig/libbrotlidec.pc
%{_libdir}/pkgconfig/libbrotlienc.pc
%{_mandir}/man3/constants.h.3*
%{_mandir}/man3/decode.h.3*
%{_mandir}/man3/encode.h.3*
%{_mandir}/man3/types.h.3*
