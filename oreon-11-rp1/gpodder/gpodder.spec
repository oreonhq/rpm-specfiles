%global source0_hash 247254d8c752e9ee3db05d33761920908e018f744b4eb015ccf3ceebb63b6618

Name:           gpodder
Version:        3.11.5
Release:        8%{?dist}
Summary:        Podcast receiver/catcher written in Python
# Mostly GPL-3.0-or-later, but some files use something different
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND ISC
URL:            http://gpodder.org
Source0:        https://github.com/gpodder/gpodder/archive/%{version}/gpodder-%{version}.tar.gz
# Rename the appdata file to comply with Fedora Packaging Guidelines
Patch:          rename-appdata.patch
Patch:          disable-auto-update-check.patch
Patch:          disable-coverage-report.patch
BuildArch:      noarch
BuildRequires:  python3-devel, python3-feedparser, python3-build, python3-installer
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  libappstream-glib
# Test tools
BuildRequires:  pytest
BuildRequires:  python3-minimock
BuildRequires:  python3-pytest-httpserver
# Runtime dependencies needed in tests
BuildRequires:  python3-podcastparser
BuildRequires:  python3-mygpoclient
BuildRequires:  python3-requests
#Requires:       python-gpod, python-eyed3 #re-enable once Python 3 support exists.
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-podcastparser
Requires:       python3-imaging
Requires:       python3-mygpoclient
Requires:       python3-requests
# Can be removed once Python 3.12 support is available in a release:
# https://github.com/gpodder/gpodder/pull/1571
Requires:       python3-zombie-imp
Requires:       hicolor-icon-theme
Requires:       /usr/bin/xdg-open
Recommends:     python3-html5lib
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp
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

%generate_buildrequires
%pyproject_buildrequires

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

%files -f %{name}.lang
%doc COPYING README.md
%{_bindir}/%{name}
%{_bindir}/gpo
%{_bindir}/%{name}-migrate2tres
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gpodder.service
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.dist-info

%changelog
%autochangelog
