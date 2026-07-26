%global source0_hash 22a86288030a200e864b82caa88a0661b1c4cc5a06c625b40dcc69c2bc4825dc

Name:		blueman
Summary:	GTK+ Bluetooth Manager
License:	GPL-2.0-or-later

Epoch:		1
Version:	2.4.6
Release:	6%{?dist}

URL:		https://github.com/blueman-project/blueman
Source0:	%{URL}/archive/refs/tags/%{version}/blueman-%{version}.tar.gz

# The configure script checks if some python packages
# are present during build, but they aren't really required,
# and in Fedora, some of them are not available on all architectures.
Patch0:		0000-less-buildrequires.patch

# The value for each of these should be either "yes" or "no"
%global enable_caja_sendto	yes
%global enable_nautilus_sendto	yes
%global enable_nemo_sendto	yes
# blueman-sendto for Thunar is shipped by the Thunar package.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2103326
%global enable_thunar_sendto	no

BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iproute
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	marshalparser
BuildRequires:	python3-Cython >= 0.21
BuildRequires:	python3-cairo-devel
BuildRequires:	python3-dbus
BuildRequires:	systemd

%{?systemd_requires}

# Based on upstream's Dependencies.md file
Requires:	bluez >= 5.48
Requires:	bluez-obexd
Requires:	dbus >= 1.9.18
Requires:	dconf
Requires:	desktop-notification-daemon
Requires:	gdk-pixbuf2
Requires:	glib2 >= 2.32
Requires:	gtk3 >= 3.24
Requires:	iproute
Requires:	NetworkManager-libnm

Requires:	python3dist(dbus-python)
Requires:	python3dist(pycairo)

# python3-gobject is split into python3-gobject and python3-gobject-base.
# Out of these two, only -base provides python3dist(pygobject).
#
# At the same time, the description for -base says:
# > This package provides the non-cairo specific bits of the GObject
# > Introspection library.
#
# Since blueman requires the "cairo-specific bits", we specify the dependency
# using the rpm package name instead of using "python3dist(pygobject)".
#
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2354051
Requires:	python3-gobject >= 3.27.2

Requires:	pulseaudio-libs-glib2
Requires:	(pulseaudio-module-bluetooth if pulseaudio)

Provides:	dbus-bluez-pin-helper

%description
Blueman is a tool to use Bluetooth devices. It is designed to provide simple,
yet effective means for controlling BlueZ API and simplifying bluetooth tasks
such as:
- Connecting to 3G/EDGE/GPRS via dial-up
- Connecting to/Creating bluetooth networks
- Connecting to input devices
- Connecting to audio devices
- Sending/Receiving files via OBEX
- Pairing

# -- Subpackages start
# -- Caja

%if "yes" == "%{enable_caja_sendto}"
%package caja
Summary:	Blueman integration for Caja
Supplements:	(caja and %{name})

Requires:	python3-caja
BuildArch:	noarch

%description caja
%{summary}.
%endif

# -- Nautilus

%if "yes" == "%{enable_nautilus_sendto}"
%package nautilus
Summary:	Blueman integration for Nautilus
Supplements:	(nautilus and %{name})

Requires:	nautilus-python
BuildArch:	noarch

%description nautilus
%{summary}.
%endif

# -- Nemo

%if "yes" == "%{enable_nemo_sendto}"
%package nemo
Summary:	Blueman integration for Nemo
Supplements:	(nemo and %{name})

Requires:	nemo-python
BuildArch:	noarch

%description nemo
%{summary}.
%endif

# -- Thunar

%if "yes" == "%{enable_thunar_sendto}"
%package thunar
Summary:	Blueman integration for Thunar
Supplements:	(Thunar and %{name})

BuildArch:	noarch

%description thunar
%{summary}.
%endif

# -- Subpackages end

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export PYTHON=%{_bindir}/python3

NOCONFIGURE="yes" ./autogen.sh
%configure \
	--enable-maintainer-mode \
	--disable-runtime-deps-check \
	--enable-caja-sendto=%{enable_caja_sendto} \
	--enable-nautilus-sendto=%{enable_nautilus_sendto} \
	--enable-nemo-sendto=%{enable_nemo_sendto} \
	--enable-thunar-sendto=%{enable_thunar_sendto} \
	--disable-static \
	--disable-schemas-compile
%make_build

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc/blueman/

# Run the python interpreter in "don't load code from user-controlled directories" mode
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2207684
%global py3_shbang_opts %{py3_shbang_opts}E
%py3_shebang_fix %{buildroot}%{_bindir}/blueman-* %{buildroot}%{_libexecdir}/blueman-*

%find_lang blueman

# we need to own this, not only because of SELinux
mkdir -p %{buildroot}%{_sharedstatedir}/blueman
touch %{buildroot}%{_sharedstatedir}/blueman/network.state

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/blueman.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/blueman-*.desktop

%if "yes" == "%{enable_thunar_sendto}"
desktop-file-validate %{buildroot}%{_datadir}/Thunar/sendto/*blueman*.desktop
%endif

%post
%systemd_post blueman-mechanism.service
%systemd_user_post blueman-applet.service

%postun
%systemd_postun_with_restart blueman-mechanism.service

%preun
%systemd_preun blueman-mechanism.service
%systemd_user_preun blueman-applet.service

%files -f blueman.lang
%doc CHANGELOG.md FAQ README.md
%license COPYING
%{_bindir}/blueman-*
%{python3_sitelib}/blueman/
%{python3_sitearch}/*.so
%{_libexecdir}/blueman-*
%{_sysconfdir}/xdg/autostart/blueman.desktop
%{_datadir}/applications/blueman-*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/blueman/
%{_datadir}/dbus-1/services/org.blueman.*.service
%{_datadir}/dbus-1/system.d/org.blueman.*.conf
%{_datadir}/dbus-1/system-services/org.blueman.*.service
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/polkit-1/actions/org.blueman.policy
%{_datadir}/polkit-1/rules.d/blueman.rules
%{_mandir}/man1/*
%{_unitdir}/blueman-*.service
%{_userunitdir}/blueman-*.service
%dir %{_sharedstatedir}/blueman
%ghost %attr(0644,root,root) %{_sharedstatedir}/blueman/network.state

%if "yes" == "%{enable_caja_sendto}"
%files caja
%{_datadir}/caja-python/extensions/*blueman*
%endif

%if "yes" == "%{enable_nautilus_sendto}"
%files nautilus
%{_datadir}/nautilus-python/extensions/*blueman*
%endif

%if "yes" == "%{enable_nemo_sendto}"
%files nemo
%{_datadir}/nemo-python/extensions/*blueman*
%endif

%if "yes" == "%{enable_thunar_sendto}"
%files thunar
%{_datadir}/Thunar/sendto/*blueman*
%endif

%changelog
%autochangelog
