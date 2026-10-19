%global source0_hash 752e2c54c730d33e1fe10069bb20cb11c324594c051a2beeb2822b63534a588c
%global serverbin /usr/lib/
%bcond_with mdns
Name: pappl-retrofit
Version: 1.0b2
Release:        1%{?dist}
License: Apache-2.0 WITH LLVM-exception
Summary:        Library for common functions used in retrofitting printer applications
URL: https://github.com/OpenPrinting/pappl-retrofit/
Source0:        https://github.com/OpenPrinting/pappl-retrofit//releases/download/1.0b2/pappl-retrofit-1.0b2.tar.gz
Source1: legacy-printer-app.conf
Patch001: 0001-pappl-retrofit-private.h-Add-include-cups-sidechanne.patch
Patch002: 0001-Added-man-page-for-the-Legacy-Printer-Application.patch
Patch003: pappl-retrofit-use-after-free.patch
Patch004: 0001-Use-PAPPL-configuration-options-from-file.patch
Patch005: 0001-Fix-possible-unterminated-string.patch
Patch006: 0001-cups-backends.c-Ensure-read-string-is-NULL-terminate.patch
Patch007: 0001-Protect-_prASCII-from-negative-lengths.patch
Patch008: 0001-Fix-potential-memory-leaks.patch
Patch009: 0001-Fix-memory-leaks-from-compiled_re_list.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(libcupsfilters)
BuildRequires:  pkgconfig(libppd)
BuildRequires:  pkgconfig(pappl)
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This library together with PAPPL and cups-filters 2.x allows to convert classic
CUPS printer drivers into Printer Applications. This way the printer appears as
an emulated IPP printer and one can print on it from practically any operating
system, especially also mobile operating systems and IoT platforms,
without need any client-side driver.

%package devel
Summary: Development environment for pappl-retrofit
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the pappl-retrofit headers and development environment.

%package -n legacy-printer-app
Summary: Legacy printer application
Provides: /usr/bin/legacy-printer-app
%if %{with mdns}
Recommends: avahi
Recommends: nss-mdns
%endif
Recommends: cups
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: authselect-libs
Requires: cups-filesystem
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%description -n legacy-printer-app
Legacy printer application provides support for classic printer drivers
which are not part of official Linux repositories - it enables possibility
to set your printer with proprietary printer drivers from manufacturers,
so such printer will be seen by CUPS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --enable-legacy-printer-app-as-daemon\
  --enable-shared\
  --disable-static\
  --disable-silent-rules
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_docdir}/%{name}/{LICENSE,NOTICE,COPYING}
rm -f %{buildroot}/%{_libdir}/legacy-printer-app
ln -sf /usr/lib/cups %{buildroot}/%{serverbin}/legacy-printer-app
install -p -D -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/legacy-printer-app.conf
%oreon_autofiles legacy-printer-app usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%post -n legacy-printer-app

%systemd_post legacy-printer-app.service
%preun -n legacy-printer-app

%systemd_preun legacy-printer-app.service
%postun -n legacy-printer-app

%systemd_postun_with_restart legacy-printer-app.service
%files -f %{oreon_filedir}/main.list
%files -n pappl-retrofit-devel -f %{oreon_filedir}/pappl-retrofit-devel.list
%files -n legacy-printer-app -f %{oreon_filedir}/legacy-printer-app.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0b2-10
- Prepare for Oreon 11 (RP1)
