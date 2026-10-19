%global source0_hash c09de56290589f5d66592d79acdfb8b70e76deab6df590715e4556c6d2d2068c
Name:           gpodder
Version:        3.11.5
Release:        1%{?dist}
Summary:        Podcast receiver/catcher written in Python
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND ISC
URL:            http://gpodder.org
Source0:        https://github.com/gpodder/gpodder/archive/%{version}/gpodder-%{version}.tar.gz
Patch:          rename-appdata.patch
Patch:          disable-auto-update-check.patch
Patch:          disable-coverage-report.patch
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-podcastparser
Requires:       python3-imaging
Requires:       python3-mygpoclient
Requires:       python3-requests
Requires:       python3-zombie-imp
Requires:       hicolor-icon-theme
Requires:       /usr/bin/xdg-open
Recommends:     python3-html5lib
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-gpodder = %{version}-%{release}
# /oreon:deps
%package -n       python3-gpodder+gui
Summary:        Metapackage for python3-gpodder gui extras
Requires:       python3-gpodder = %{version}-%{release}
Provides:       python3dist(gpodder[gui]) = %{version}-%{release}

%description -n python3-gpodder+gui
Metapackage for python3-gpodder gui extras.

%description
gPodder is a Podcast receiver/catcher written in Python, using GTK. 
It manages podcast feeds for you and automatically downloads all 
podcasts from as many feeds as you like.
It also optionally supports syncing with ipods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Drop unused tools that complicate licensing
rm -rf tools/max-osx
rm -rf tools/win_installer

#drop examples for now
rm -rf share/gpodder/examples

%build

make messages
%check

make unittest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}
desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                 \
  --remove-key Miniicon --add-category Application              \
  --remove-category FileTransfer --remove-category News         \
  --remove-category Network                                     \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files

%changelog

%autochangelog
