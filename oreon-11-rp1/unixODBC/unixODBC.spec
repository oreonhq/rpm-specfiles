%global source0_hash f210501445ce21bf607ba51ef8c125e10e22dffdffec377646462df5f01915ec

Name: unixODBC
Version: 2.3.12
Release: 1%{?dist}
Summary: ODBC driver manager
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://www.unixodbc.org/
Source0: https://www.unixodbc.org/unixODBC-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: libtool
BuildRequires: readline-devel
BuildRequires: oreon-rpm-macros

%description
The ODBC driver manager and the libraries OpenLDAP's ODBC backend loads.

%package devel
Summary: Development files for unixODBC
Requires: unixODBC%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkgconfig file for unixODBC.

%prep
%autosetup -n unixODBC-%{version} -p1
%oreon_sha256

%build
%oreon_configure --disable-static --disable-gui
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
