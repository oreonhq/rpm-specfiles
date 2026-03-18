Name:           media-player-info
Version:        23
Release:        20%{?dist}
Summary:        Data files describing media player capabilities

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.freedesktop.org/wiki/Software/media-player-info
Source0:        http://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3
%if %{undefined flatpak}
Requires:       udev
%endif

%description
media-player-info is a repository of data files describing media player
(mostly USB Mass Storage ones) capabilities. These files contain information
about the directory layout to use to add music to these devices, about the
supported file formats, etc.

The package also installs a udev rule to identify media player devices.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%license COPYING
%doc README NEWS AUTHORS
%{_datadir}/media-player-info
/usr/lib/udev/rules.d/*
/usr/lib/udev/hwdb.d/20-usb-media-players.hwdb


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23-20
- Prepare for Oreon 11 (RP1)
