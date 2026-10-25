%global source0_hash 2c3379eb76597dcab50911449b013e2697c4bffcc716dbbf0d9b0e8fbbb46fb4
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cryptsetup
Version: 2.8.1
Release: 1%{?dist}
Summary: Disk encryption library
License: GPL-2.0-or-later
URL: https://gitlab.com/cryptsetup/cryptsetup
Source0: https://www.kernel.org/pub/linux/utils/cryptsetup/v2.8/cryptsetup-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: openssl-devel
BuildRequires: json-c-devel
BuildRequires: popt-devel
BuildRequires: device-mapper-devel
BuildRequires: libblkid-devel
BuildRequires: pkgconf
%endif

%description
Disk encryption library

%package devel
Summary: Disk encryption library
Requires: cryptsetup%{?_isa} = %{version}-%{release}

%description devel
Disk encryption library

%prep
%oreon_sha256
%autosetup -n cryptsetup-2.8.1 -p1

%build
%oreon_configure --disable-static --with-crypto_backend=openssl --disable-asciidoc --disable-ssh-token
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
