%global source0_hash none

Summary:       Simple portable interface to lowlevel networking routines
Name:          libdnet
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD

%global forgeurl https://github.com/ofalk/%{name}
Version:       1.18.0
%global tag libdnet-%{version}
%forgemeta

Release:       9%{?dist}
URL:           %{forgeurl}
Source:        %{forgesource}

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: check-devel
BuildRequires: python3-Cython
BuildRequires: python3-setuptools

%description
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling (IP filter, ipfw, ipchains,
pf, ...), network interface lookup and manipulation, raw IP
packet and Ethernet frame, and data transmission.

%package devel
Summary:       Header files for libdnet library
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package progs
Summary:       Sample applications to use with libdnet
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description progs
%{summary}.

%package -n python%{python3_pkgversion}-libdnet
%{?python_provide:%python_provide python%{python3_pkgversion}-libdnet}
# Remove before F30
Provides:      %{name}-python = %{version}-%{release}
Provides:      %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes:     %{name}-python < %{version}-%{release}
Summary:       Python bindings for libdnet
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-libdnet
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgeautosetup

%build
autoreconf -i
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

pushd python
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd

%ldconfig_scriptlets

%files
%license LICENSE
%doc THANKS TODO
%{_libdir}/*.so.*

%files devel
%{_bindir}/dnet-config
%{_libdir}/libdnet.so
%{_includedir}/dnet.h
%{_includedir}/dnet/
%{_mandir}/man3/dnet.3*

%files progs
%{_sbindir}/dnet
%{_mandir}/man8/dnet.8*

%files -n python%{python3_pkgversion}-libdnet
%{python3_sitearch}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.18.0-9
- Import
