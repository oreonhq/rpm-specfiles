%global source0_hash b4e5d438f5d3f5d236a49f3fcb433ca4fa489d7d5995961a5d967950bbb6c102

Name: cozy
%global rtld_name com.github.geigi.cozy

Summary: Modern audiobook player
License: GPL-3.0-or-later

Version: 1.3.0
Release: 13%{?dist}

URL: https://cozy.geigi.de
Source0: https://github.com/geigi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Source99: find-unpatched-imports.sh

# Unbundle python-inject
Patch0: 0000--unbundle-inject.patch

# The appdata XML file does not pass validation
Patch1: 0001-fix-appdata-file.patch

BuildArch: noarch

%global req_adwaita 1.4.0
%global req_py_inject 4.3.1
%global req_py_peewee 3.9.6

BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: libappstream-glib
BuildRequires: libadwaita-devel >= %{req_adwaita}
BuildRequires: meson >= 0.59.0
BuildRequires: python3-devel

%global with_tests 1

%if 0%{?with_tests}
BuildRequires: gstreamer1-plugins-base

BuildRequires: python3dist(distro)
BuildRequires: python3dist(inject) >= %{req_py_inject}
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(peewee) >= %{req_py_peewee}
BuildRequires: python3dist(pygobject)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytz)
BuildRequires: python3dist(requests)
%endif

Requires: file
Requires: glib2
Requires: libadwaita >= %{req_adwaita}
Requires: gstreamer1-plugins-bad-free
Requires: gstreamer1-plugins-good
Requires: hicolor-icon-theme

# For whatever reason, the Python dependency generator doesn't seem to work
# for this RPM, so we'll just copy-paste the BuildRequires list
Requires: python3dist(distro)
Requires: python3dist(inject) >= %{req_py_inject}
Requires: python3dist(mutagen)
Requires: python3dist(peewee) >= %{req_py_peewee}
Requires: python3dist(pygobject)
Requires: python3dist(pytz)
Requires: python3dist(requests)

# Not available in official Fedora repos
# Requires: gstreamer1-libav

%description
Cozy is a modern audiobook player for Linux.

Here are some of the current features:
- Import your audiobooks into Cozy to browse them comfortably
- Sort your audio books by author, reader & name
- Remembers your playback position
- Sleep timer
- Playback speed control
- Search your library
- Offline Mode! This allows you to keep an audio book on your internal storage
  if you store your audiobooks on an external or network drive.
  Perfect for listening on the go!
- Add mulitple storage locations
- Drag & Drop to import new audio books
- Support for DRM free mp3, m4a (aac, ALAC, …), flac, ogg, opus, wav files
- Mpris integration (Media keys & playback info for desktop environment)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Unbundle inject
%patch 0 -p1
rm -rf cozy/ext/inject

# Run the "find unpatched imports" script
"%{SOURCE99}" "$(pwd)"

# Apply other patches
%patch 1 -p1

%build
%meson
%meson_build
%meson_build com.github.geigi.cozy-update-po
%meson_build extra-update-po

%install
%meson_install
%find_lang %{rtld_name}

# Move "actions" icons out of /usr/share/icons/ to avoid conflicts with other packages
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2120689
#      https://github.com/geigi/cozy/issues/710
COZY_ICON_DIR="%{buildroot}%{_datadir}/%{rtld_name}/icons/hicolor/scalable"
install -m 755 -d "${COZY_ICON_DIR}"
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/actions "${COZY_ICON_DIR}/actions"

# Remove the "devel" icon
rm %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{rtld_name}.Devel.svg

%check
%if 0%{?with_tests}
%pytest
%endif

appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/%{rtld_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop

%files -f %{rtld_name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{rtld_name}
%{_datadir}/%{rtld_name}/
%{_datadir}/applications/%{rtld_name}.desktop
%{_datadir}/glib-2.0/schemas/%{rtld_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{rtld_name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{rtld_name}-symbolic.svg
%{_metainfodir}/%{rtld_name}.appdata.xml
%{python3_sitelib}/%{name}/

%changelog
%autochangelog
