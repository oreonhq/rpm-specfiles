%global source0_hash d787b4a45b3a38513f1e80e025c4059918f1390b815944c6a541bd07eeb0ccae

Name:           persepolis
Version:        5.1.1
Release:        7%{?dist}
Summary:        A powerful graphical download manager

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://persepolisdm.github.io/
Source0:        https://github.com/persepolisdm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  meson ninja-build
BuildRequires:  libappstream-glib
Requires:       sound-theme-freedesktop
Requires:       python3-pysocks python3-urllib3 python3-requests
Requires:       python3-setproctitle python3-psutil
%if 0%{?fedora} >= 41
Requires:       python3-pyside6 qt6-qtsvg
%else
Requires:       python3-qt5 qt5-qtsvg
%endif
Recommends:     yt-dlp ffmpeg-free python3-dasbus

%description
Persepolis is a Download Manager written in Python.
 - Multi segment downloading
 - Scheduling downloads
 - Download queuing
 - Finding and downloading video from Youtube, Vimeo, DailyMotion, ...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm 'persepolis/Persepolis Download Manager.py'
find -type f -exec \
   sed -i '1s=^#!/usr/bin/\(python\|env python.*\)$=#!%{__python3}=' {} \;

%build
%meson
%meson_build

%install
%meson_install
chmod a+x %{buildroot}/%{python3_sitelib}/persepolis/__main__.py

%check
# No valid tests available
#%{__python3} setup.py test
desktop-file-validate %{buildroot}/%{_datadir}/applications/*persepolis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}
%{_datadir}/metainfo/com.github.persepolisdm.persepolis.appdata.xml

%changelog
%autochangelog
