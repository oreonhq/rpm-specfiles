%global source0_hash 5ba2aeb73d30ce63bd5d19a166a44fbeeafad82c245d089e28b812008ead0966

Name:    ofono
Summary: Open Source Telephony
Version: 2.19
Release: 2%{?dist}

# oFono is GPL. This covers most of the source files.
# ProvisionDB is LGPL. This covers src/provisiondb.{c,h}
License: GPL-2.0-only AND LGPL-2.1-or-later
URL:     http://www.ofono.org/
Source0: https://git.kernel.org/pub/scm/network/ofono/ofono.git/snapshot/ofono-%{version}.tar.gz

BuildRequires: make
BuildRequires: libell-devel >= 0.79
BuildRequires: automake libtool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev) >= 145
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(mobile-broadband-provider-info)

BuildRequires: systemd-rpm-macros
BuildRequires: gcc
BuildRequires: m4

%description
oFono.org is a place to bring developers together around designing an
infrastructure for building mobile telephony (GSM/UMTS) applications.
oFono includes a high-level D-Bus API for use by telephony applications.
oFono also includes a low-level plug-in API for integrating with telephony
stacks, cellular modems and storage back-ends.

%package devel
Summary: Development files for oFono
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
if [ ! -f configure ]; then
./bootstrap
fi

%configure \
	--enable-external-ell \
	--with-systemdunitdir=%{_unitdir}
%make_build

%install
%make_install
# create/own this
mkdir -p %{buildroot}%{_libdir}/ofono/plugins

%check
make check

%post
%systemd_post ofono.service

%preun
%systemd_preun ofono.service

%postun
%systemd_postun_with_restart ofono.service

%files
%doc ChangeLog AUTHORS README
%license COPYING
%{_sysconfdir}/dbus-1/system.d/ofono.conf
%dir %{_sysconfdir}/ofono/
%config(noreplace) %{_sysconfdir}/ofono/phonesim.conf
%{_sbindir}/ofonod
%{_unitdir}/ofono.service
%{_mandir}/man8/ofonod.8*
%{_datadir}/ofono/
%dir %{_libdir}/ofono/
%dir %{_libdir}/ofono/plugins/

%files devel
%{_includedir}/ofono/
%{_libdir}/pkgconfig/ofono.pc

%changelog
%autochangelog
