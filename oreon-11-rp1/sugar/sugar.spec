%global source0_hash 10a25b262050ba0c44e551ac52e0297fea34d790d1852247b11cccb920e0a958
Name:    sugar
Version: 0.121
Release:        10%{?dist}
Summary:        Constructionist learning platform
URL:     http://sugarlabs.org/
License: GPL-2.0-or-later
Source0:        http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: activities.defaults
Requires: avahi-tools
Requires: dbus-x11
Requires: dconf
Requires: ethtool
Requires: gnome-keyring-pam
Requires: gstreamer-plugins-espeak
Requires: gtksourceview3
Requires: gvfs
Requires: libwnck3
Requires: libxklavier
Requires: metacity
Requires: NetworkManager
Requires: openssh
Requires: polkit
Requires: python3-gwebsockets
Requires: sugar-artwork
Requires: sugar-toolkit-gtk3
Requires: telepathy-glib
Requires: telepathy-mission-control
Requires: telepathy-gabble
Requires: telepathy-salut
Requires: upower
Requires: webkit2gtk4.1
Requires: libsoup3
Requires: xdg-user-dirs
Obsoletes: sugar-base < 0.9.8-18
Provides: sugar-base
BuildArch: noarch
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  automake
BuildRequires:  dconf-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-empy
# /oreon:deps
%description
Sugar provides simple yet powerful means of engaging young children in the 
world of learning that is opened up by computers and the Internet. With Sugar,
even the youngest learner will quickly become proficient in using the 
computer as a tool to engage in authentic problem-solving.  Sugar promotes 
sharing, collaborative learning, and reflection, developing skills that help 
them in all aspects of life. 

Sugar is also the learning environment for the One Laptop Per Child project. 
See http://www.laptop.org for more information on this project.

%package cp-all
Summary: All control panel modules 
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cp-background %{name}-cp-backup %{name}-cp-datetime 
Requires: %{name}-cp-frame %{name}-cp-language %{name}-cp-modemconfiguration
Requires: %{name}-cp-network %{name}-cp-keyboard %{name}-cp-webaccount 
Requires: %{name}-cp-updater
%description cp-all
This is a meta package to install all Sugar Control Panel modules

%package cp-background
Summary: Sugar Background control panel
Requires: %{name} = %{version}-%{release}
%description cp-background
This is the Sugar control panel to change the background

%package cp-backup
Summary: Sugar Backup control panel
Requires: %{name} = %{version}-%{release}
%description cp-backup
This is the Sugar control panel to backup and restore the Journal

%package cp-datetime
Summary: Sugar Date and Time control panel
Requires: %{name} = %{version}-%{release}
%description cp-datetime
This is the Sugar Date and Time settings control panel

%package cp-frame
Summary: Sugar Frame control panel
Requires: %{name} = %{version}-%{release}
%description cp-frame
This is the Sugar Frame settings control panel

%package cp-keyboard
Summary: Sugar Keyboard control panel
Requires: %{name} = %{version}-%{release}
%description cp-keyboard
This is the Sugar Keyboard settings control panel

%package cp-language
Summary: Sugar Language control panel
Requires: %{name} = %{version}-%{release}
%description cp-language
This is the Sugar Language settings control panel

%package cp-modemconfiguration
Summary: Sugar Modem configuration control panel
Requires: %{name} = %{version}-%{release}
Requires: mobile-broadband-provider-info
%description cp-modemconfiguration
This is the Sugar Modem configuration control panel

%package cp-network
Summary: Sugar Network control panel
Requires: %{name} = %{version}-%{release}
%description cp-network
This is the Sugar Network settings control panel

%package cp-power
Summary: Sugar Power control panel
Requires: %{name} = %{version}-%{release}
%description cp-power
This is the Sugar Power settings control panel

%package cp-updater
Summary: Sugar Activity Update control panel
Requires: %{name} = %{version}-%{release}
%description cp-updater
This is the Sugar Activity Updates control panel

%package cp-webaccount
Summary: Sugar Web Account control panel
Requires: %{name} = %{version}-%{release}
%description cp-webaccount
This is the Sugar Web Account control panel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf
ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done
%configure
%make_build
%install
%make_install
mkdir %{buildroot}/%{_datadir}/sugar/activities
rm -rf %{buildroot}/%{_datadir}/sugar/extensions/cpsection/__pycache__/
install -p %{SOURCE1} %{buildroot}%{_datadir}/sugar/data/activities.defaults
%py_byte_compile %{python3} %{buildroot}%{_datadir}/sugar/
%py_byte_compile %{python3} %{buildroot}%{python3_sitelib}/jarabe/
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sugar-cp-all -f %{oreon_filedir}/sugar-cp-all.list
%files -n sugar-cp-background -f %{oreon_filedir}/sugar-cp-background.list
%files -n sugar-cp-backup -f %{oreon_filedir}/sugar-cp-backup.list
%files -n sugar-cp-datetime -f %{oreon_filedir}/sugar-cp-datetime.list
%files -n sugar-cp-frame -f %{oreon_filedir}/sugar-cp-frame.list
%files -n sugar-cp-keyboard -f %{oreon_filedir}/sugar-cp-keyboard.list
%files -n sugar-cp-language -f %{oreon_filedir}/sugar-cp-language.list
%files -n sugar-cp-modemconfiguration -f %{oreon_filedir}/sugar-cp-modemconfiguration.list
%files -n sugar-cp-network -f %{oreon_filedir}/sugar-cp-network.list
%files -n sugar-cp-power -f %{oreon_filedir}/sugar-cp-power.list
%files -n sugar-cp-updater -f %{oreon_filedir}/sugar-cp-updater.list
%files -n sugar-cp-webaccount -f %{oreon_filedir}/sugar-cp-webaccount.list

%changelog

%autochangelog
