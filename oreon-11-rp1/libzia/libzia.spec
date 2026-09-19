%global source0_hash eb1be2c8e7311980094c6d5b0abd674587d38e98952d0e1751d7d10af8f734f6

Name:		libzia
Version:	4.71
Release:	1%{?dist}
Summary:	Platform abstraction layer for the tucnak package
License:	GPL-2.0-only
URL:		http://tucnak.nagano.cz/
Source:		http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	SDL2-devel
BuildRequires:	libpng-devel
BuildRequires:	libftdi-devel
BuildRequires:	binutils-devel
BuildRequires:	gnutls-devel
BuildRequires:	gtk3-devel
# Used for direct control of display power saving features (via exec)
Requires:	xset
# This is to fulfill Fedora requirement - it marks the interface with
# version number 0. Upstream uses --release versioning in libtool.
# They do not support linking between different versions of tucnak and
# libzia, i.e. tucnak-4.18 needs to be linked to libzia-4.18.
Patch0:		libzia-4.26-soname-fix.patch

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

%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install

# drop .la
rm -f %{buildroot}%{_libdir}/libzia.la

# drop unneeded files
rm -f %{buildroot}%{_datadir}/libzia/doc/*
rm -f %{buildroot}%{_datadir}/libzia/settings
rm -f %{buildroot}%{_prefix}/lib/libzia/*
rmdir %{buildroot}%{_datadir}/libzia/doc/ %{buildroot}%{_datadir}/libzia %{buildroot}%{_prefix}/lib/libzia

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libzia-%{version}.so.0*

%files devel
%{_bindir}/zia-config
%{_includedir}/libzia
%{_libdir}/libzia.so
%{_libdir}/pkgconfig/libzia.pc

%changelog
%autochangelog
