%global source0_hash b3e3d5d8f1b4aab6f3d896a4c67c2beb3edf058ce1724e240bac6e6a486e4b9b

# Status: active
# Tag: Sf2, Editor
# Type: Standalone
# Category: Audio, Tool

Name: swami
Version: 2.2.2
Release: 26%{?dist}
Summary: MIDI instrument and sound editor
License: GPL-2.0-only
URL: http://www.swamiproject.org/
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/swami/swami/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: swami-0001-fix-missing-header.patch

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: fftw-devel
BuildRequires: fluidsynth-devel
BuildRequires: libglade2-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libinstpatch-devel
BuildRequires: librsvg2-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
The Swami Project - Sampled Waveforms And Musical Instruments - is a collection
of free software for editing and sharing MIDI instruments and sounds. Swami
aims to provide an instrument editing and sharing software for instrument
formats such as SoundFont, DLS and GigaSampler.

%package libs
Summary: MIDI instrument and sound editor library

%description libs
Shared libraries for The Swami Project - Sampled Waveforms And Musical
Instruments.

%package devel
Summary: MIDI instrument and sound editor development files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for The Swami Project - Sampled Waveforms And
Musical Instruments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
       -DLIB_SUFFIX="" \
       -DPLUGINS_DIR=%{_lib}/swami/
%cmake_build

%install

%cmake_install

desktop-file-install                                    \
    --add-category="AudioVideo"                         \
    --add-category="X-Jack"                             \
    --remove-category="Application"                     \
    --remove-key="Encoding"                             \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog NEWS README.md HACKERS
%license COPYING
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml

%files libs
%{_libdir}/lib%{name}*.so.*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}/

%changelog
%autochangelog
