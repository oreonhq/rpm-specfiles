%global source0_hash b3edec34150d97a63dcd1d6b0032570f673e38f4b521dc72e865d2013d4a39ae
Version: 1.18.5
Summary:        Universal Plug and Play (UPnP) SDK
Name: libupnp
Release:        1%{?dist}
License: BSD-3-Clause AND ISC AND MIT
URL: https://github.com/pupnp/pupnp
Source0:        https://github.com/pupnp/pupnp/archive/release-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The Universal Plug and Play (UPnP) SDK for Linux provides 
support for building UPnP-compliant control points, devices, 
and bridges on Linux.

%package devel
Summary: Include files needed for development with libupnp
Requires: libupnp%{?_isa} = %{version}-%{release}
%description devel
The libupnp-devel package contains the files necessary for development with
the UPnP SDK libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pupnp-release-%{version}
%oreon_prep
%build

autoreconf -vif
%configure \
  --enable-static=no \
  --enable-ipv6
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
%{__rm} %{buildroot}%{_libdir}/{libixml.la,libupnp.la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libupnp-devel -f %{oreon_filedir}/libupnp-devel.list

%changelog

%autochangelog

