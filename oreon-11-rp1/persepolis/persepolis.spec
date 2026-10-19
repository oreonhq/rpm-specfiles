%global source0_hash 8d002e369955fd77e5353714185ce3edb98463b7117a26583b72f4db4e51b2c8
Name:           persepolis
Version:        5.2.0
Release:        1%{?dist}
Summary:        A powerful graphical download manager
License:        GPL-3.0-or-later
URL:            https://persepolisdm.github.io/
Source0:        https://github.com/persepolisdm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       sound-theme-freedesktop
Requires:       python3-pysocks python3-urllib3 python3-requests
Requires:       python3-setproctitle python3-psutil
Requires:       python3-qt5 qt5-qtsvg
Recommends:     yt-dlp ffmpeg-free python3-dasbus
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/*persepolis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
