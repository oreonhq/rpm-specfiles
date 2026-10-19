%global source0_hash dd816df79765f87a0838b1568fbc40c3e8bdb4aef0e77712c85623afe34a29ad
Name:    redshift
Version: 1.12
Release:        1%{?dist}
Summary:        Adjusts the color temperature of your screen according to time of day
License: GPL-3.0-or-later
URL:     http://jonls.dk/redshift/
Source0:        https://github.com/jonls/redshift/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:      geoclue2
%{?systemd_requires}
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  geoclue2-devel
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libXrandr-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd
# /oreon:deps
%description
Redshift adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in
front of the screen at night.

The color temperature is set according to the position of the sun. A
different color temperature is set during night and daytime. During
twilight and early morning, the color temperature transitions smoothly
from night to daytime temperature to allow your eyes to slowly
adapt.

This package provides the base program.

%package -n %{name}-gtk
Summary:       GTK integration for Redshift
BuildRequires: desktop-file-utils
BuildRequires: python3-devel >= 3.2
Requires:      python3-gobject
Requires:      python3-pyxdg
Requires:      %{name} = %{version}-%{release}
Obsoletes:      gtk-%{name} < 1.7-7
%description -n %{name}-gtk
This package provides GTK integration for Redshift, a screen color
temperature adjustment program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{name}-%{version}
autopoint -f && AUTOPOINT="intltoolize --automake --copy" autoreconf -f -i

%build

%configure --with-systemduserunitdir=%{_userunitdir}
%make_build V=1
%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/redshift.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/redshift-gtk.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_user_post %{name}-gtk.service
%preun

%systemd_user_preun %{name}-gtk.service
%files -f %{oreon_filedir}/main.list
%files -n redshift-gtk -f %{oreon_filedir}/redshift-gtk.list

%changelog

%autochangelog
