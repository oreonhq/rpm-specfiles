%global source0_hash 92e6de1be9ec176428fd2367677e61ceffc2ee1cb119035037a27d346b0403bb

Name: libevent
Version: 2.1.12
Release: 1%{?dist}
Summary: Event notification library
License: BSD-3-Clause
URL: https://libevent.org/
Source0: https://github.com/libevent/libevent/releases/download/release-%{version}-stable/libevent-%{version}-stable.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: oreon-rpm-macros

%description
An event loop library used by OpenLDAP and libverto.

%package devel
Summary: Development files for libevent
Requires: libevent%{?_isa} = %{version}-%{release}
Requires: openssl-devel

%description devel
Headers and the pkgconfig files for libevent.

%prep
%autosetup -n libevent-%{version}-stable -p1
%oreon_sha256

%build
%oreon_configure --disable-static --enable-openssl
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
