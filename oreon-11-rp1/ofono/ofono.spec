%global source0_hash 5ba2aeb73d30ce63bd5d19a166a44fbeeafad82c245d089e28b812008ead0966
Name:    ofono
Summary:        Open Source Telephony
Version: 2.19
Release:        1%{?dist}
License: GPL-2.0-only AND LGPL-2.1-or-later
URL:     http://www.ofono.org/
Source0:        https://git.kernel.org/pub/scm/network/ofono/ofono.git/snapshot/ofono-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libell-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_prep
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
mkdir -p %{buildroot}%{_libdir}/ofono/plugins
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%post

%systemd_post ofono.service
%preun

%systemd_preun ofono.service
%postun

%systemd_postun_with_restart ofono.service
%files -f %{oreon_filedir}/main.list
%files -n ofono-devel -f %{oreon_filedir}/ofono-devel.list

%changelog

%autochangelog
