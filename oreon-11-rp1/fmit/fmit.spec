%global source0_hash 8dc123c84c19d6a9a62b303015255718705d5b0b8448a330d3815dd7f9688b02

Summary:       Free Music Instrument Tuner
Name:          fmit
Version:       1.2.14
Release:       14%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://gillesdegottex.github.io/fmit/
Source0:       https://github.com/gillesdegottex/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: qt5-linguist
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: freeglut-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: fftw3-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: desktop-file-utils
BuildRequires: make

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

# we use svg icon
rm -rf %{buildroot}%{_datadir}/icons/hicolor/128x128

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/%{name}/tr/
cp -a tr/*.qm %{buildroot}%{_datadir}/%{name}/tr/
rm -f %{buildroot}%{_datadir}/%{name}/tr/*.ts
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%license COPYING_GPL.txt COPYING_LGPL.txt
%doc INSTALL.txt README.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tr
%dir %{_datadir}/%{name}/scales
%{_datadir}/%{name}/scales/*.scl
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg

%changelog
%autochangelog
