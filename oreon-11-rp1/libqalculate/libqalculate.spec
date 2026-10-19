%global source0_hash f3dfdcf97d5a9e3a5bc0ebe66afd184721b606276eee3ba0ada8c92a5e71d44c
%global srcnm Qalculate
%global libversion 23
%global libsymlink 3.10
Summary:        Multi-purpose calculator library
Name:		libqalculate
Version:	5.12.0
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://qalculate.github.io/
Source0:        https://github.com/%{srcnm}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cln-devel
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(XML::Parser)
BuildRequires:  readline-devel
# /oreon:deps
%description
This library underpins the Qalculate! multi-purpose desktop calculator for
GNU/Linux

%package	devel
Summary:	Development tools for the Qalculate calculator library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel
Requires:	libxml2-devel
Requires:	cln-devel
Requires:	mpfr-devel
%description	devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%package -n	qalculate
Summary:	Multi-purpose calculator, text mode interface
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Provides:	qalc
%description -n	qalculate
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides the text-mode interface for Qalculate! The GTK and QT
frontends are provided by qalculate-gtk and qalculate-kde packages resp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -fiv
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles qalculate usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libqalculate-devel -f %{oreon_filedir}/libqalculate-devel.list
%files -n qalculate -f %{oreon_filedir}/qalculate.list

%changelog

%autochangelog
