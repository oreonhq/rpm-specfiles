%global source0_hash cbd160778f6cf147f9b0487719edc5197a1404f46d7c7bfd89e153f0d8ce71ae

Summary:        Real-time software synthesizer
Name:           zynaddsubfx
Version:        3.0.6
Release:        13%{?dist}
# Source is a collective work, distributed by
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            http://zynaddsubfx.sourceforge.net
Source0:        http://download.sf.net/sourceforge/zynaddsubfx/zynaddsubfx-%{version}.tar.bz2
# We cannot build this from source since Fedora's texlive is too old
Patch0:         zynaddsubfx-buildflags.patch
# Do not ask for cortex-a9 which conflicts with the armv7a baseline
Patch1:         zynaddsubfx-cortex.patch
Patch2:         %{name}-missing-cstdint.patch

Requires:       hicolor-icon-theme
Requires:       %{name}-common = %{version}-%{release}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  fftw3-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  non-ntk-devel
BuildRequires:  ImageMagick
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  mxml-devel
BuildRequires:  portaudio-devel
BuildRequires:  zlib-devel
BuildRequires:  liblo-devel
BuildRequires:  libXpm-devel

# Build dumps core on i686
# Bug 2297277
ExcludeArch:	i686

%description
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the standalone implementation of the synthesizer.

%package common
Summary:        Common files for ZynAddSubFX synthesizers
BuildArch:      noarch

%description common
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the common files needed by the implementations of the
synthesizer.

%package dssi
Summary:        Real-time software synthesizer for DSSI
Requires:       %{name}-common = %{version}-%{release}
Requires:       dssi

%description dssi
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the DSSI implementation of the synthesizer.

%package lv2
Summary:        %{name} LV2 plugins
Requires:       %{name}-common = %{version}-%{release}
Requires:       lv2

%description lv2
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the LV2 implementation of the synthesizer.

%package vst
Summary:        %{name} VST plugins
Requires:       %{name}-common = %{version}-%{release}

%description vst
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the VST implementation of the synthesizer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Fix encoding
for i in AUTHORS.txt; do
   iconv -f iso8859-1 -t utf8 $i -o tmpfile
   touch -r $i tmpfile
   mv -f tmpfile $i
done

%build
# TODO: Please submit an issue to upstream (rhbz#2381655)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DDefaultOutput=jack -DPluginLibDir=%{_libdir} \
  -DBASHCOMP_PKG_PATH=%{_datadir}/bash-completion/completions \
%ifarch %{ix86} x86_64
  -DX86Build=ON \
%endif
  %{nil}

%cmake_build

# build external programs
%make_build -C ExternalPrograms/Controller
%make_build -C ExternalPrograms/Spliter

%install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%cmake_install

mkdir -p %{buildroot}%{_datadir}/%{name}

cp -rp instruments/examples instruments/banks %{buildroot}%{_datadir}/%{name}

# install external programs
pushd ExternalPrograms
   install -m 0755 Controller/controller %{buildroot}%{_bindir}/zynaddsubfx-controller
   install -m 0755 Spliter/spliter %{buildroot}%{_bindir}/zynaddsubfx-spliter
popd

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop

# We are including these in the common package below
rm -fr %{buildroot}%{_datadir}/doc/%{name}/
install -d -m 0755 %{buildroot}%{_libdir}/%{name}

%files
%{_bindir}/*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/zynaddsubfx.svg
%{_datadir}/pixmaps/zynaddsubfx.png
%{_datadir}/bash-completion/completions/%{name}

%files common
%doc AUTHORS.txt
%license COPYING
%{_datadir}/%{name}/

%files dssi
%{_libdir}/dssi/*.so

%files lv2
%{_libdir}/lv2/*

%files vst
%{_libdir}/vst/*.so

%changelog
%autochangelog
