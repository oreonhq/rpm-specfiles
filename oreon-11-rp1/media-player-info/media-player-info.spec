%global source0_hash e6cf46db0b503e9929407ec6aa3fcd2becc9e2ca945b4ff787c98c8db63a1134

Name:           media-player-info
Version:        24
Release:        1%{?dist}
Summary:        Data files describing media player capabilities

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.freedesktop.org/wiki/Software/media-player-info
Source0:        https://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Fri Sep 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 24-1
- Update to 24

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23-20
- Prepare for Oreon 11 (RP1)
