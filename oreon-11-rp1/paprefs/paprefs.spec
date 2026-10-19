%global source0_hash b3f21e40dc3936d15e3ffc910fb0c07c14b88e8c287715b456a948c17638f633
Name:           paprefs
Version:        1.2
Release:        1%{?dist}
Summary:        Management tool for PulseAudio
License:        GPL-2.0-or-later
URL:            http://freedesktop.org/software/pulseaudio/%{name}
Source0:        http://freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz
Requires:       pulseaudio-module-gsettings
Suggests:       PackageKit-session-service
Suggests:       gnome-packagekit-common
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtkmm30-devel
BuildRequires:  lynx
BuildRequires:  meson
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog
for the PulseAudio sound server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dlynx=true
%meson_build
%install
%meson_install
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
