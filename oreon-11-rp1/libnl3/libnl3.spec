%global source0_hash none
%global source1_hash none

Name: libnl3
Version: 3.12.0
Release: 3%{?dist}
Summary: Convenience library for kernel netlink sockets
License: LGPL-2.1-only
URL: http://www.infradead.org/~tgr/libnl/

%global version_path libnl%(echo %{version} | tr . _)

%if 0%{?rhel} > 8 || 0%{?fedora} > 43
# Disable python3 build by default
%bcond_with python3
%else
%bcond_without python3
%endif

Source0: https://github.com/thom311/libnl/releases/download/%{version_path}/libnl-%{version}.tar.gz
Source1: https://github.com/thom311/libnl/releases/download/%{version_path}/libnl-doc-%{version}.tar.gz

#Patch1: some.patch


BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: flex
BuildRequires: libtool
BuildRequires: swig


%description
This package contains a convenience library to simplify
using the Linux kernel's netlink sockets interface for
network manipulation


%package devel
Summary: Libraries and headers for using libnl3
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cli = %{version}-%{release}
Requires: kernel-headers

%description devel
This package contains various headers for using libnl3


%package cli
Summary: Command line interface utils for libnl3
Requires: %{name} = %{version}-%{release}

%description cli
This package contains various libnl3 utils and additional
libraries on which they depend


%package doc
Summary: API documentation for libnl3
Requires: %{name} = %{version}-%{release}

%description doc
This package contains libnl3 API documentation


%if %{with python3}
%package -n python3-libnl3
Summary: libnl3 binding for Python 3
%{?python_provide:%python_provide python3-libnl3}
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: make
Requires: %{name} = %{version}-%{release}

%description -n python3-libnl3
Python 3 bindings for libnl3
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n libnl-%{version}

tar -xzf %SOURCE1

%build
autoreconf -vif
%configure
make %{?_smp_mflags}

%if %{with python3}
pushd ./python/
# build twice, otherwise capi.py is not copied to the build directory.
CFLAGS="$RPM_OPT_FLAGS" %pyproject_wheel
CFLAGS="$RPM_OPT_FLAGS" %pyproject_wheel
popd
%endif

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la -delete

%if %{with python3}
pushd ./python/
%pyproject_install
popd
%endif

%check
make check

%if %{with python3}
pushd ./python/
%{__python3} setup.py check
popd
%endif

%ldconfig_scriptlets
%ldconfig_scriptlets cli

%files
%license COPYING
%exclude %{_libdir}/libnl-cli*.so.*
%exclude %{_libdir}/libnl*-3.a
%{_libdir}/libnl-*.so.*
%config(noreplace) %{_sysconfdir}/*

%files devel
%license COPYING
%{_includedir}/libnl3/netlink/
%dir %{_includedir}/libnl3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files cli
%license COPYING
%{_libdir}/libnl-cli*.so.*
%{_libdir}/libnl/
%{_bindir}/*
%{_mandir}/man8/*

%files doc
%license COPYING
%doc libnl-doc-%{version}/*.html
%doc libnl-doc-%{version}/*.css
%doc libnl-doc-%{version}/stylesheets/*
%doc libnl-doc-%{version}/images/*
%doc libnl-doc-%{version}/images/icons/*
%doc libnl-doc-%{version}/images/icons/callouts/*
%doc libnl-doc-%{version}/api/*

%if %{with python3}
%files -n python3-libnl3
%{python3_sitearch}/netlink
%{python3_sitearch}/netlink-*.dist-info
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.0-3
- Prepare for Oreon 11 (RP1)
