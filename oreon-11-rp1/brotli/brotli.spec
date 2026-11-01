%global source0_hash 98d35d11a78dc453aebb7d10c3748f3f73ff78c8267c0dc697b8631f67bf7e8f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: brotli
Version: 1.2.1
Release: 1%{?dist}
Summary: Lossless compression algorithm
License: MIT
URL: https://github.com/google/brotli
Source0: https://github.com/google/brotli/archive/v%{version}/brotli-%{version}.tar.gz
Provides: libbrotli = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
%endif

%description
Brotli is a generic-purpose lossless compression algorithm.

%package devel
Summary: Development files for brotli
Requires: brotli%{?_isa} = %{version}-%{release}
Provides: libbrotli-devel = %{version}-%{release}
Provides: pkgconfig(libbrotlicommon)
Provides: pkgconfig(libbrotlidec)
Provides: pkgconfig(libbrotlienc)

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
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
