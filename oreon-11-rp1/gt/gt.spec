# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e63db94354856f858806ff09ed14bd8d6ebce38200adbbccd51628b3a3ae0010
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           gt
Version:        0.4
Release:        1%{?dist}
Summary:        Modified Timidity which supportes enhanced gus format patches
License:        GPL-2.0-or-later
URL:            http://alsa.opensrc.org/GusSoundfont
Source0:        %{name}-%{version}-clean.tar.gz
Patch0:         gt-0.4-noac3.patch
Patch1:         gt-0.4-compile-fix.patch
Patch2:         gt-0.4-optflags.patch
Patch3:         gt-0.4-config-default-velocity-layer.patch
Patch4:         gt-0.4-ppc-compile-fix.patch
Patch5:         gt-0.4-unsf-bigendian-fix.patch
Patch6:         gt-0.4-unsf-tremolo.patch
Patch7:         gt-0.4-gcc10.patch
Patch8:         gt-0.4-std23.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flex
BuildRequires:  make
Requires:       timidity++-patches

%description
Modified timidity midi player which supportes enhanced gus format patches and
surround audio output.

%package -n soundfont-utils
Summary:        Utilities for converting from / to various soundfont formats

%description -n soundfont-utils
Utilities for converting from / to various soundfont formats and a midi file
disassembler.

%prep
%oreon_sha256
%autosetup -p1
cp -p src/README README.timidity
sed -i -e "s#\$(TIMID_DIR)#%{_sysconfdir}#" src/Makefile.in

%build
%global build_type_safety_c 0
%configure
make

%install
%make_install
mv $RPM_BUILD_ROOT%{_bindir}/dim $RPM_BUILD_ROOT%{_bindir}/midi-disasm
mv $RPM_BUILD_ROOT%{_mandir}/man1/dim.1 \
   $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
sed -i 's/dim/midi-disasm/g' $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
touch -r utils/midifile.c $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
 

%files
%doc AUTHORS ChangeLog FEATURES NEWS README*
%license COPYING
%{_bindir}/gt
%{_mandir}/man1/gt.1*

%files -n soundfont-utils
%doc COPYING utils/README* utils/GUSSF2-SPEC
%{_bindir}/*
%exclude %{_bindir}/gt
%{_mandir}/man1/*
%exclude %{_mandir}/man1/gt.1*

%changelog
%autochangelog
