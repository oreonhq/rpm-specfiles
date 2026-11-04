%global source0_hash fc51ca7196f1a3f5fdf6ffd3864b50f4f9c02333be28be4eeca057e103c0dd18
%global source1_hash a4f9813fe769cd82a67e0be94296a9eafe14e0c3ca1dd198331e3ee6db25c1a1

%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
Name: libnl3
Version:        3.12.0
Release:        1%{?dist}
Summary: Convenience library for kernel netlink sockets
License: LGPL-2.1-only
URL: http://www.infradead.org/~tgr/libnl/

%global version_path libnl%(echo %{version} | tr . _)

# Disable python3 build by default
%bcond_with python3

Source0: https://github.com/thom311/libnl/releases/download/%{version_path}/libnl-%{version}.tar.gz
Source1:        https://github.com/thom311/libnl/releases/download/libnl3_12_0/libnl-doc-%{version}.tar.gz

#Patch1: some.patch


BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: flex
BuildRequires: libtool
BuildRequires: swig
BuildRequires:  oreon-rpm-macros


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



%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -

%autosetup -p1 -n libnl-%{version}

tar -xzf %SOURCE1

%build
autoreconf -vif
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la -delete


%check
make check


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


