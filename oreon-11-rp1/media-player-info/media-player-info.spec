Name:           media-player-info
Version:        23
Release:        20%{?dist}
Summary:        Data files describing media player capabilities

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.freedesktop.org/wiki/Software/media-player-info
Source0:        http://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a9ab6de0b497f6e13efc2cbe45a4fe06982145d786674c24274c3ed909ecc8cb
%global source0_file media-player-info-23.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/media-player-info-23.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a9ab6de0b497f6e13efc2cbe45a4fe06982145d786674c24274c3ed909ecc8cb" || { echo "oreon: Source0 SHA256 mismatch for media-player-info-23.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
