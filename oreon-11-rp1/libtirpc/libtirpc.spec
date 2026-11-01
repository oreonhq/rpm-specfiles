%global source0_hash 8839959bfcc7a0f4c609d8e4f53f1c67ae33de23775ec35beb39ff15adf11920
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libtirpc
Version: 1.3.8
Release: 1%{?dist}
Summary: Transport-independent RPC library
License: BSD-3-Clause
URL: https://sourceforge.net/projects/libtirpc/
Source0: https://downloads.sourceforge.net/libtirpc/libtirpc-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: krb5-devel
BuildRequires: patchelf

%description
libtirpc is a port of the SunRPC transport-independent RPC library,
with IPv6 and GSS-API support.

%package devel
Summary: Development files for libtirpc
Requires: libtirpc%{?_isa} = %{version}-%{release}

%description devel
Headers, libraries and pkg-config files for building against libtirpc.

%prep
%oreon_sha256
%autosetup -n libtirpc-%{version} -p1

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
