%global source0_hash 1765929dd1eb4a51975990749b58dabc0abba99bc0bdb72dcae60366e3f61f00
%global fontfile %{_datadir}/fonts/bitstream-vera/VeraBd.ttf
Name:           setBfree
Version:        0.8.13
Release:        1%{?dist}
Summary:        A DSP Tonewheel Organ emulator
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND ISC
URL:            https://setbfree.org
Source0:        https://github.com/pantherb/setBfree/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        x42-whirl.desktop
Source3:        %{name}.appdata.xml
Requires:       bitstream-vera-sans-fonts
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  lv2-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pango-devel
# /oreon:deps
%package -n lv2-setBfree-plugins
Summary:        A DSP Tonewheel Organ emulator. LV2 version
Requires:       lv2 >= 1.8.1
Requires:       bitstream-vera-sans-fonts
%description
setBfree is a MIDI-controlled, software synthesizer designed to imitate the
sound and properties of the electromechanical organs and sound modification
devices that brought world-wide fame to the names and products of Laurens
Hammond and Don Leslie.
This is the Jack version.

%description -n lv2-setBfree-plugins
setBfree is a MIDI-controlled, software synthesizer designed to imitate the
sound and properties of the electromechanical organs and sound modification
devices that brought world-wide fame to the names and products of Laurens
Hammond and Don Leslie.
This is the LV2 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

flags=" -ffast-math -fno-finite-math-only"
%ifarch %{ix86}
flags+=" -msse -mfpmath=sse"
%endif
%ifarch x86_64
flags+=" -msse2 -mfpmath=sse"
%endif
CC=gcc; export CC
%set_build_flags
%make_build OPTIMIZATIONS="%{optflags} ${flags}" \
 PREFIX=%{_prefix} FONTFILE=%{fontfile} \
 lv2dir=%{_libdir}/lv2
%install
%make_install PREFIX=%{_prefix} \
 FONTFILE=%{fontfile} lv2dir=%{_libdir}/lv2
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
 %{SOURCE1} %{SOURCE2}
install -d -m755 %{buildroot}%{_metainfodir}
install -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
install -d -m755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m644 doc/%{name}.png doc/x42-whirl.png \
 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 doc/jboverdrive.1 doc/setBfree.1 doc/setBfreeUI.1 doc/x42-whirl.1 \
 %{buildroot}%{_mandir}/man1
%oreon_autofiles lv2-setBfree-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lv2-setBfree-plugins -f %{oreon_filedir}/lv2-setBfree-plugins.list

%changelog

%autochangelog
