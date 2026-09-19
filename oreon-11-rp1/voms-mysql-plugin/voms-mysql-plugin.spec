%global source0_hash 0f1856307daa1fc937db4b1f6dd7cf7645cd30684f577a99ab3fbc01cca57e80

Name:		voms-mysql-plugin
Version:	3.1.7
Release:	26%{?dist}
Summary:	VOMS server plugin for MySQL

License:	Apache-2.0
URL:		https://italiangrid.github.io/voms/
Source:		https://github.com/italiangrid/%{name}/archive/v%{version}.tar.gz

Provides:	voms-mysql = %{version}-%{release}
Obsoletes:	voms-mysql < 3.1.6
Requires:	voms-server%{?_isa}

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	libtool
%if %{?fedora}%{!?fedora:0} >= 28 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	mariadb-connector-c-devel
%else
BuildRequires:	mysql-devel
%endif
BuildRequires:	openssl-devel

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package offers the MySQL implementation for the VOMS server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
./autogen.sh

%build
%configure --libdir=%{_libdir}/voms --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/voms/libvomsmysql.la

%files
%{_datadir}/voms/voms-mysql.data
%{_datadir}/voms/voms-mysql-compat.data
%dir %{_libdir}/voms
%{_libdir}/voms/libvomsmysql.so

%changelog
%autochangelog
