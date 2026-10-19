%global source0_hash c64cfe2a7b9c90848e737df8d6c4aba9acb08c470373df85bddaf4ce7d59ecf0
Summary:        Free Music Instrument Tuner
Name:          fmit
Version:       1.4.6
Release:        1%{?dist}
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://gillesdegottex.github.io/fmit/
Source0:        https://github.com/gillesdegottex/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw3-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  portaudio-devel
BuildRequires:  qt5-linguist
# /oreon:deps
%description
%{name} is a graphical utility for tuning musical instruments, with
error and volume history and advanced features like waveform shape,
harmonics ratio (formants), and micro-tonal tuning.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# disable acs_qt capture system on linux
sed -i 's/^\(CONFIG += acs_qt\)/# \1/g' fmit.pro

%build

%{qmake_qt5} PREFIX=%{_prefix} CONFIG+="acs_alsa acs_jack acs_portaudio"
lrelease-qt5 %{name}.pro
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/icons/hicolor/128x128
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/%{name}/tr/
cp -a tr/*.qm %{buildroot}%{_datadir}/%{name}/tr/
rm -f %{buildroot}%{_datadir}/%{name}/tr/*.ts
%find_lang %{name} --with-qt --without-mo
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
