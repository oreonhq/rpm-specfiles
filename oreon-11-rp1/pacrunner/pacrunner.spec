%global source0_hash d9778423e7ad20cea14232dfec97bb92213ab7e05c6aef817eb6d97a9437e7c5
Name:		pacrunner
Version:	0.19
Release:        1%{?dist}
Summary:        Proxy configuration dæmon
License:	GPL-2.0-only
URL:		http://connman.net/
Source0:        http://www.kernel.org/pub/linux/network/connman/pacrunner-%{version}.tar.xz
Provides:       bundled(duktape) = 2.4.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
