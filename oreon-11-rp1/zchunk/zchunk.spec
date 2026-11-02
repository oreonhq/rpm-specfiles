%global source0_hash 2ab8ef54475aa2b2c0120fc6ae6d0788e0c3d4d4b671985edc6a19c8096a02cc
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: zchunk
Version: 1.5.5
Release: 1%{?dist}
Summary: Compressed file format library
License: BSD-2-Clause
URL: https://github.com/zchunk/zchunk
Source0: https://github.com/zchunk/zchunk/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: libzstd-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: pkgconf
BuildRequires: patchelf

%description
zchunk is a compressed file format.

%package devel
Summary: Compressed file format library
Requires: zchunk%{?_isa} = %{version}-%{release}

%description devel
zchunk is a compressed file format.

%prep
%oreon_sha256
%autosetup -n zchunk-%{version} -p1

%build
%oreon_meson -Dwith-zstd=enabled
%oreon_meson_build

%install
%oreon_meson_install
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
