%global source0_hash bbc78c46217174655c2b32b138ad119f3ac15f50808b4d0b3a2677a4b1afc950
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libX11
Version: 1.8.14
Release: 1%{?dist}
Summary: X11 client library
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/lib/libX11-%{version}.tar.xz
Source1: libX11-%{version}.tar.xz.sig
Source2: libX11-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: xorgproto
BuildRequires: xtrans
BuildRequires: libXau-devel >= 1.0.12
BuildRequires: libxcb-devel >= 1.17.0
BuildRequires: pkgconf

%description
X11 client library

%package devel
Summary: X11 client library
Requires: libX11%{?_isa} = %{version}-%{release}

%description devel
X11 client library

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n libX11-1.8.12 -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
