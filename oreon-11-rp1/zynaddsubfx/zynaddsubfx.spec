%global source0_hash cbd160778f6cf147f9b0487719edc5197a1404f46d7c7bfd89e153f0d8ce71ae
Summary:        Real-time software synthesizer
Name:           zynaddsubfx
Version:        3.0.6
Release:        13%{?dist}
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            http://zynaddsubfx.sourceforge.net
Source0:        http://download.sf.net/sourceforge/zynaddsubfx/zynaddsubfx-%{version}.tar.bz2
Patch0:         zynaddsubfx-buildflags.patch
Patch1:         zynaddsubfx-cortex.patch
Patch2:         %{name}-missing-cstdint.patch
Requires:       hicolor-icon-theme
Requires:       %{name}-common = %{version}-%{release}
ExcludeArch:	i686
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  fftw3-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  libXpm-devel
BuildRequires:  liblo-devel
BuildRequires:  make
BuildRequires:  mxml-devel
BuildRequires:  non-ntk-devel
BuildRequires:  portaudio-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DDefaultOutput=jack -DPluginLibDir=%{_libdir} \
  -DBASHCOMP_PKG_PATH=%{_datadir}/bash-completion/completions \
%ifarch %{ix86} x86_64
  -DX86Build=ON \
%endif
  %{nil}
%cmake_build
%make_build -C ExternalPrograms/Controller
%make_build -C ExternalPrograms/Spliter
%install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -rp instruments/examples instruments/banks %{buildroot}%{_datadir}/%{name}
pushd ExternalPrograms
   install -m 0755 Controller/controller %{buildroot}%{_bindir}/zynaddsubfx-controller
   install -m 0755 Spliter/spliter %{buildroot}%{_bindir}/zynaddsubfx-spliter
popd
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop
rm -fr %{buildroot}%{_datadir}/doc/%{name}/
install -d -m 0755 %{buildroot}%{_libdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n zynaddsubfx-common -f %{oreon_filedir}/zynaddsubfx-common.list
%files -n zynaddsubfx-dssi -f %{oreon_filedir}/zynaddsubfx-dssi.list
%files -n zynaddsubfx-lv2 -f %{oreon_filedir}/zynaddsubfx-lv2.list
%files -n zynaddsubfx-vst -f %{oreon_filedir}/zynaddsubfx-vst.list

%changelog

%autochangelog
