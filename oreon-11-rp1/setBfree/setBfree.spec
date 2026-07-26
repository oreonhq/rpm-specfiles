%global source0_hash 1765929dd1eb4a51975990749b58dabc0abba99bc0bdb72dcae60366e3f61f00

%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global fontfile %{_datadir}/fonts/bitstream-vera-sans-fonts/VeraBd.ttf
%else
%global fontfile %{_datadir}/fonts/bitstream-vera/VeraBd.ttf
%endif

Name:           setBfree
Version:        0.8.13
Release:        6%{?dist}
Summary:        A DSP Tonewheel Organ emulator

# Automatically converted from old format: GPLv2+ and GPLv3+ and ISC - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND ISC
URL:            https://setbfree.org
# Not present in releases, but tagged on GitHub
Source0:        https://github.com/pantherb/setBfree/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        x42-whirl.desktop
Source3:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  ftgl-devel
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cairo-devel
BuildRequires:  pango-devel

Requires:       bitstream-vera-sans-fonts
Requires:       hicolor-icon-theme

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

%autosetup -p 1

%build

# This package does not build on all arches with upstream build flags,
# so upstream build flags are split.
# This is a realtime app, so we need the fastest possible math,
# flags for x86_64 are set to be compatible with most AMD and Intel CPUs,
# and to use the best possible SIMD instruction set.
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

# install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
 %{SOURCE1} %{SOURCE2}

# install appdata file
install -d -m755 %{buildroot}%{_metainfodir}
install -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}

# validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# install icon file
install -d -m755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m644 doc/%{name}.png doc/x42-whirl.png \
 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps

# install man pages
install -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 doc/jboverdrive.1 doc/setBfree.1 doc/setBfreeUI.1 doc/x42-whirl.1 \
 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/x42-whirl.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/x42-whirl.png
%{_metainfodir}/*
%doc AUTHORS ChangeLog README.md
%license COPYING

%files -n lv2-setBfree-plugins
%{_libdir}/lv2/*
%doc AUTHORS ChangeLog README.md
%license COPYING

%changelog
%autochangelog
