%global source0_hash 5c9e470b232a7acd3433491ac5221b4832f0c71318618dc6aa04dd05ffcd8fd9
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libnsl2
Version: 2.0.1
Release: 1%{?dist}
Summary: Public client interface for NIS and NIS+
License: LGPL-2.1-or-later
URL: https://github.com/thkukuk/libnsl
Source0: https://github.com/thkukuk/libnsl/releases/download/v%{version}/libnsl-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: libtirpc-devel
BuildRequires: pkgconf
BuildRequires: patchelf
%endif

%description
libnsl provides the NIS and NIS+ client interface that used to ship
with glibc.

%package devel
Summary: Development files for libnsl2
Requires: libnsl2%{?_isa} = %{version}-%{release}

%description devel
Headers, libraries and pkg-config files for building against libnsl2.

%prep
%oreon_sha256
%autosetup -n libnsl-%{version} -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
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
