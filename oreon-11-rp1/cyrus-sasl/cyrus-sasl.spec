%global source0_hash 7ccfc6abd01ed67c1a0924b353e526f1b766b21f42d4562ee635a8ebfc5bb38c

Name: cyrus-sasl
Version: 2.1.28
Release: 1%{?dist}
Summary: Cyrus SASL authentication library
License: BSD-3-Clause
URL: https://www.cyrusimap.org/sasl/
Source0: https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-%{version}/cyrus-sasl-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: oreon-rpm-macros

%description
The SASL library and the plugins OpenLDAP and other clients load.

%package devel
Summary: Development files for Cyrus SASL
Requires: cyrus-sasl%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkgconfig file for Cyrus SASL.

%prep
%autosetup -n cyrus-sasl-%{version} -p1
%oreon_sha256

%build
%oreon_configure --disable-static --with-openssl --enable-gssapi
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
