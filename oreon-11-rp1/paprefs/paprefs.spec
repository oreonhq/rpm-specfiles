%global source0_hash b3f21e40dc3936d15e3ffc910fb0c07c14b88e8c287715b456a948c17638f633

Name:           paprefs
Version:        1.2
Release:        %autorelease
Summary:        Management tool for PulseAudio

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://freedesktop.org/software/pulseaudio/%{name}
Source0:        http://freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtkmm30-devel
BuildRequires:  lynx
BuildRequires:  meson
BuildRequires:  pulseaudio-libs-devel

Requires:       pulseaudio-module-gsettings
Suggests:       PackageKit-session-service
Suggests:       gnome-packagekit-common

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog
for the PulseAudio sound server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dlynx=true
%meson_build

%install
%meson_install

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc %{_vpath_builddir}/doc/README
%{_bindir}/paprefs
%dir %{_datadir}/paprefs
%{_datadir}/paprefs/paprefs.glade
%{_datadir}/applications/paprefs.desktop

%changelog
%autochangelog
