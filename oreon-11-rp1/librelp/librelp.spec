%global source0_hash 58e976e31795d7309cf2d9f37fdc93522daa4a322f5012d7879fed9ebfa40068
Summary:        The Reliable Event Logging Protocol library
Name: librelp
Version: 1.13.0
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://www.rsyslog.com/
Source0:        http://download.rsyslog.com/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnutls-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Librelp is an easy to use library for the RELP protocol. RELP (stands
for Reliable Event Logging Protocol) is a general-purpose, extensible
logging protocol.

%package devel
Summary: Development files for the %{name} package
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: gnutls-devel >= 1.4.0
BuildRequires: openssl-devel
%description devel
Librelp is an easy to use library for the RELP protocol. The
librelp-devel package contains the header files and libraries needed
to develop applications using librelp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
%configure --disable-static --enable-tls --enable-tls-openssl
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n librelp-devel -f %{oreon_filedir}/librelp-devel.list

%changelog

%autochangelog
