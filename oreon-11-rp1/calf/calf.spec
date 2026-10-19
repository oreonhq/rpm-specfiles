%global source0_hash 2d304eed88e87438b2b8857a2f4480046bf4003bce2e17a042abdbbf7d59122f
%if %{defined flatpak_runtime}
%global _prefix /app/extensions/Plugins/Calf
%global __brp_check_rpaths %{nil}
%endif
Name:		calf
Version:	0.90.9
Release:        3%{?dist}
Summary:        Audio plugins pack
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
URL:		http://calf-studio-gear.org/
Source0:        http://github.com/calf-studio-gear/calf/archive/%{version}/calf-%{version}.tar.gz
Source1:	%{name}-dssi.desktop
Provides: ladspa-%{name}-plugins = %{version}-%{release}
Obsoletes: ladspa-%{name}-plugins < 0.90.3-13
%global common_desc \
The Calf project aims at providing a set of high quality open source audio\
plugins for musicians. All the included plugins are designed to be used with\
multitrack software, as software replacement for instruments and guitar stomp\
boxes.
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  expat-devel
BuildRequires:  fftw3-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  libglade2-devel
BuildRequires:  libtool
BuildRequires:  lv2-devel
BuildRequires:  make
# /oreon:deps
%description
%common_desc

The plugins are available in LV2, DSSI, Standalone JACK and LADSPA formats.
This package contains the common files and the Standalone JACK plugin.

%package -n lv2-%{name}-plugins
Summary:	Calf plugins in LV2 format
License:	GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:	%{name} = %{version}-%{release}
Requires:	lv2
%description -n lv2-%{name}-plugins
%common_desc

This package contains LV2 synthesizers and effects, MIDI I/O extension.

%package -n lv2-%{name}-plugins-gui
Summary:	Calf plugins in LV2 format
License:	GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Requires:	%{name} = %{version}-%{release}
Requires:	lv2-%{name}-plugins
Requires:	lv2
%description -n lv2-%{name}-plugins-gui
%common_desc

This package contains LV2 plugins GUI extension.

%package -n dssi-%{name}-plugins
Summary:	Calf plugins in DSSI format
License:	LGPL-2.0-or-later
Requires:	%{name} = %{version}-%{release}
Requires:	dssi
%description -n dssi-%{name}-plugins
%common_desc

This package contains DSSI synthesizers and effects, also GUI extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

echo "GenericName= Audio Effects" >> %{name}.desktop.in
mv configure.ac.deprecated configure.ac
./autogen.sh
sed -i 's|-O3||' configure
%configure \
	--with-dssi-dir=%{_libdir}/dssi/ \
	--with-lv2-dir=%{_libdir}/lv2 \
	--enable-experimental=yes \
%ifarch x86_64 %ix86
	--enable-sse \
%endif
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
	--remove-category="Application" \
	--remove-key="Version" \
	--add-category="X-Synthesis" \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
ln -s jack-dssi-host $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/*.a*
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/dssi
ln -s %{_libdir}/calf/calf.so $RPM_BUILD_ROOT/%{_libdir}/dssi/calf.so
%oreon_autofiles lv2-calf-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles lv2-calf-plugins-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dssi-calf-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lv2-calf-plugins -f %{oreon_filedir}/lv2-calf-plugins.list
%files -n lv2-calf-plugins-gui -f %{oreon_filedir}/lv2-calf-plugins-gui.list
%files -n dssi-calf-plugins -f %{oreon_filedir}/dssi-calf-plugins.list

%changelog

%autochangelog
