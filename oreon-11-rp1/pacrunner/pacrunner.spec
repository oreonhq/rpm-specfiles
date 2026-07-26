%global source0_hash 707c201e74c2706eda96be89e55c6b4e0b8acbe35601b70df67fea0b43d624f1

Name:		pacrunner
Version:	0.16
Release:	16%{?dist}
Summary:	Proxy configuration dæmon
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://connman.net/

Source0:	http://www.kernel.org/pub/linux/network/connman/pacrunner-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:	pkgconfig(glib-2.0) pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libcurl) pkgconfig(cunit)

Provides:       bundled(duktape) = 2.4.0

%description
PacRunner provides a dæmon for processing proxy configuration
and providing information to clients over D-Bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# The silly way the bundled duktape.c is generated confuses debuginfo
# generator
sed '/#line/d' -i duktape/duktape.c

%build
%configure --disable-libproxy --enable-debug --enable-duktape \
	   --enable-curl --enable-datafiles
make %{?_smp_mflags} V=99

%install
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/pacrunner
make install DESTDIR=$RPM_BUILD_ROOT testdir=%{_libexecdir}/pacrunner

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_sbindir}/pacrunner
%{_libexecdir}/pacrunner
%{_datadir}/dbus-1/system-services/org.pacrunner.service
%{_sysconfdir}/dbus-1/system.d/pacrunner.conf

%changelog
%autochangelog
