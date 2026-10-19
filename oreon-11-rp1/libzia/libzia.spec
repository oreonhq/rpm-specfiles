%global source0_hash eb1be2c8e7311980094c6d5b0abd674587d38e98952d0e1751d7d10af8f734f6
Name:		libzia
Version:	4.71
Release:        1%{?dist}
Summary:        Platform abstraction layer for the tucnak package
License:	GPL-2.0-only
URL:		http://tucnak.nagano.cz/
Source0:        http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
Requires:	xset
Patch0:		libzia-4.26-soname-fix.patch
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libftdi-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Platform abstraction layer for the tucnak package.

%package devel
Summary:	Development files for libzia
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL2-devel
Requires:	gtk2-devel
Requires:	libftdi-devel
Requires:	pkgconf-pkg-config
%description devel
Development files for libzia

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libzia.la
rm -f %{buildroot}%{_datadir}/libzia/doc/*
rm -f %{buildroot}%{_datadir}/libzia/settings
rm -f %{buildroot}%{_prefix}/lib/libzia/*
rmdir %{buildroot}%{_datadir}/libzia/doc/ %{buildroot}%{_datadir}/libzia %{buildroot}%{_prefix}/lib/libzia
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libzia-devel -f %{oreon_filedir}/libzia-devel.list

%changelog

%autochangelog
