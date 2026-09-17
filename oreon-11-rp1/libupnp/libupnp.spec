%global source0_hash none

Version: 1.18.5
Summary: Universal Plug and Play (UPnP) SDK
Name: libupnp
Release: 1%{?dist}
License: BSD-3-Clause AND ISC AND MIT
URL: https://github.com/pupnp/pupnp
Source: %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libtool


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

%autosetup -p1 -n pupnp-release-%{version}


%build
autoreconf -vif
%configure \
  --enable-static=no \
  --enable-ipv6

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

%{__rm} %{buildroot}%{_libdir}/{libixml.la,libupnp.la}

%files
%license COPYING
%doc THANKS
%{_libdir}/libixml.so.11*
%{_libdir}/libupnp.so.20*

%files devel
%{_includedir}/upnp/
%{_libdir}/libixml.so
%{_libdir}/libupnp.so
%{_libdir}/pkgconfig/libupnp.pc

%changelog
%autochangelog

