Name:           pavucontrol
Version:        6.1
Release:        %autorelease
Summary:        Volume control for PulseAudio

License:        GPL-2.0-or-later
URL:            https://www.freedesktop.org/software/pulseaudio/%{name}
Source0:        https://www.freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 0dce61c1088eafa04c270e1fb79eb7aff47e98567f7d28c65a7bee6cd24e415d
%global source0_file pavucontrol-6.1.tar.xz
# oreon url source checksums end

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  meson >= 0.59.0
BuildRequires:  lynx
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(sigc++-3.0)

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume control
tool ("mixer") for the PulseAudio sound server. In contrast to classic mixer
tools this one allows you to control both the volume of hardware devices and
of each playback stream separately.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pavucontrol-6.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0dce61c1088eafa04c270e1fb79eb7aff47e98567f7d28c65a7bee6cd24e415d" || { echo "oreon: Source0 SHA256 mismatch for pavucontrol-6.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/README.html
rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/style.css

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.pulseaudio.pavucontrol.metainfo.xml

%files -f %{name}.lang
%license LICENSE
%doc doc/README
%{_bindir}/pavucontrol
%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop
%{_metainfodir}/org.pulseaudio.pavucontrol.metainfo.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.1-1
- Prepare for Oreon 11 (RP1)
