%global source0_hash 2c187055e2206e62cef4559845e7c2ec6ec5a07ce1e0a6044e4342e0c5d7771d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: zchunk
Version: 1.5.1
Release: 1%{?dist}
Summary: Compressed file format library
License: BSD-2-Clause
URL: https://github.com/zchunk/zchunk
Source0: https://github.com/zchunk/zchunk/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: libzstd-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: pkgconf
BuildRequires: patchelf
%endif

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
