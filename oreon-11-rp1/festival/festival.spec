# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4c9007426b125290599d931df410e2def51e68a8aeebd89b4a61c7c96c09a4b4
%global source100_hash e7c6e3642dbd5b0d64942bc015a986fdd6244a79e51ec2e8309e63d569e49ea3
%global source101_hash c19430919bca45d5368cd4c82af6153fbcc96a487ebd30b78b5f3c08718b7c07
%global source200_hash 809c4ab5ed9e4df4a658b58d5c56fe35055723f00d81a238168f5a1ebdaed08c
%global source202_hash ecd14b77c528e94dfb076e44050102fe8fba57e5fe813acf78a66629317f52a5
%global source220_hash b2adbdfeda0cba289bb4da68dd14114d3eb3e7f72049cc8d2cbdfb2df39f6934
%global source221_hash 1dc6792af9e2c1660a46fe499aa67af4affa665a0bdc08207cc11719baa62f6d
%global source222_hash 11c82d1c18ce3db6fb11ca788cc5d84f69f9346aff77c7495f50005d6b042148
%global source223_hash 711db388bc500331cfda86a46a72193ca1e2c9dc7d5ef16dfc86827e499946f2
%global source224_hash 3167afa3a6ffb5bbc305c94a1e6b671e40783a87a49372fce04c54942872c421
%global source225_hash 78cb93e361ab016fd23833c56853ddf21e2f1356310f54eed1c09a9755ce9f43
%global source230_hash 7429be02cc73408b1846447e2a269372c5f756589455c4ab8a534be78eff4514
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: festival
Summary: Speech synthesis and text-to-speech system
Version: 2.5.0
Release:        %{autorelease}

URL: http://www.cstr.ed.ac.uk/projects/festival/
License: MIT AND GPL-1.0-or-later AND TCL AND BSD-3-Clause

Obsoletes: festival-lib
Obsoletes: festival-speechtools-libs
Obsoletes: festival-speechtools-libs-devel
Obsoletes: festival-speechtools-utils

%global baseURL  http://festvox.org/packed/festival/2.5
Source0: %{baseURL}/festival-%{version}-release.tar.gz

Source100: %{baseURL}/festlex_POSLEX.tar.gz
Source101: %{baseURL}/festlex_CMU.tar.gz

%global diphoneversion 0.19990610
Source200: %{baseURL}/voices/festvox_kallpc16k.tar.gz
Source202: %{baseURL}/voices/festvox_rablpc16k.tar.gz

Source220: %{baseURL}/voices/festvox_cmu_us_awb_cg.tar.gz
Source221: %{baseURL}/voices/festvox_cmu_us_bdl_cg.tar.gz
Source222: %{baseURL}/voices/festvox_cmu_us_clb_cg.tar.gz
Source223: %{baseURL}/voices/festvox_cmu_us_jmk_cg.tar.gz
Source224: %{baseURL}/voices/festvox_cmu_us_rms_cg.tar.gz
Source225: %{baseURL}/voices/festvox_cmu_us_slt_cg.tar.gz

Source230: festival.service

Patch100: festival-2.5.0-pulseaudio.patch
Patch101: festival-2.5.0-use-system-speech-tools.patch
Patch102: festival-2.5.0-use-system-libs.patch
Patch103: festival-2.5.0-filesystem-standard.patch
Patch104: festival-2.5.0-siteinit.patch
Patch105: festival-configure-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: texi2html
BuildRequires: ncurses-devel
BuildRequires: speech-tools-libs-devel
BuildRequires: speech-tools-libs-static
BuildRequires: systemd
BuildRequires: make
%{?systemd_requires}

Requires: festvox-slt-arctic-hts

Requires:  pulseaudio-utils

Requires: festival-data = %{version}-%{release}
Requires: speech-tools-libs

%package -n festvox-kal-diphone
Summary: American English male speaker "Kevin" for Festival
Version: %{diphoneversion}
Provides: festival-voice
Provides: festvox-kallpc16k
BuildArch: noarch

%package -n festvox-rab-diphone
Summary: American English male speaker "Kurt" for Festival
Version: %{diphoneversion}
Requires: festival
Provides: festival-voice
Provides: festvox-rablpc16k
BuildArch: noarch

%package -n festvox-awb-arctic-hts
Summary: Scottish-accent US English male speaker "AWB" for Festival
Requires: festival
Provides: festival-voice
BuildArch: noarch

%package -n festvox-bdl-arctic-hts
Summary: US English male speaker "BDL" for Festival
Requires: festival
Provides: festival-voice
BuildArch: noarch

%package -n festvox-clb-arctic-hts
Summary: US English female speaker "CLB" for Festival
Requires: festival
Provides: festival-voice
BuildArch: noarch

%package -n festvox-jmk-arctic-hts
Summary: Canadian-accent US English male speaker "JMK" for Festival
Requires: festival
Provides: festival-voice
BuildArch: noarch

%package -n festvox-rms-arctic-hts
Summary: US English male speaker "RMS" for Festival
Requires: festival
Provides: festival-voice
BuildArch: noarch

%package -n festvox-slt-arctic-hts
Summary: US English female speaker "SLT" for Festival
Requires: festival
Provides: festival-voice
BuildArch: noarch

%package data
Summary: Data files for the Festival speech synthesis system
BuildArch: noarch

%package devel
Summary: Development files for the Festival speech synthesis system
Requires: speech-tools-libs-devel
Provides: festival-static = %{version}-%{release}

%description
Festival is a general multi-lingual speech synthesis system developed
at CSTR. It offers a full text to speech system with various APIs, as
well as an environment for development and research of speech synthesis
techniques. It is written in C++ with a Scheme-based command interpreter
for general control.

%description -n festvox-kal-diphone
American English male speaker ("Kevin") for Festival.

This voice provides an American English male voice using a residual excited
LPC diphone synthesis method. It uses the CMU Lexicon pronunciations.
Prosodic phrasing is provided by a statistically trained model using part of
speech and local distribution of breaks. Intonation is provided by a CART
tree predicting ToBI accents and an F0 contour generated from a model
trained from natural speech. The duration model is also trained from data
using a CART tree.

%description -n festvox-rab-diphone
British English male speaker ("RAB") for Festival.

This voice provides a British English male voice using a residual excited
LPC diphone synthesis method. It uses the CMU Lexicon for pronunciations.
Prosodic phrasing is provided by a statistically trained model using part of
speech and local distribution of breaks. Intonation is provided by a CART
tree predicting ToBI accents and an F0 contour generated from a model
trained from natural speech. The duration model is also trained from data
using a CART tree.

%description -n festvox-awb-arctic-hts
US English male speaker ("AWB") for Festival. AWB is a native Scottish
English speaker, but the voice uses the US English front end.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1138 utterances spoken by a Scottish English male speaker. The
speaker is very experienced in building synthetic voices and matched
prompted US English, though his vowels are very different from US English
vowels. Scottish English speakers will probably find synthesizers based on
this voice strange. Unlike the other CMU_ARCTIC databases this was recorded
in 16 bit 16KHz mono without EGG, on a Dell Laptop in a quiet office. The
database was automatically labelled using CMU Sphinx using the FestVox
labelling scripts. No hand correction has been made.

%description -n festvox-bdl-arctic-hts
US English male speaker ("BDL") for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English male speaker. The speaker
is experienced in building synthetic voices. This was recorded at 16bit
32KHz, in a sound proof room, in stereo, one channel was the waveform, the
other EGG. The database was automatically labelled using CMU Sphinx using
the FestVox labelling scripts. No hand correction has been made.

%description -n festvox-clb-arctic-hts
US English female speaker ("CLB") for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English female speaker. The
speaker is experienced in building synthetic voices. This was recorded at
16bit 32KHz, in a sound proof room, in stereo, one channel was the waveform,
the other EGG. The database was automatically labelled using CMU Sphinx
using the FestVox labelling scripts. No hand correction has been made.

%description -n festvox-jmk-arctic-hts
US English male speaker ("JMK") voice for Festival. JMK is a native Canadian
English speaker, but the voice uses the US English front end.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1138 utterances spoken by a US English male speaker. The speaker
is experienced in building synthetic voices. This was recorded at 16bit
32KHz, in a sound proof room, in stereo, one channel was the waveform, the
other EGG. The database was automatically labelled using CMU Sphinx using
the FestVox labelling scripts. No hand correction has been made.

%description -n festvox-rms-arctic-hts
US English male speaker ("RMS") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English male speaker. The speaker
is experienced in building synthetic voices. This was recorded at 16bit
32KHz, in a sound proof room, in stereo, one channel was the waveform, the
other EGG. The database was automatically labelled using EHMM an HMM labeler
that is included in the FestVox distribution. No hand correction has been
made.

%description -n festvox-slt-arctic-hts
US English female speaker ("SLT") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English female speaker. The
speaker is experienced in building synthetic voices. This was recorded at
16bit 32KHz, in a sound proof room, in stereo, one channel was the waveform,
the other EGG. The database was automatically labelled using CMU Sphinx
using the FestVox labelling scripts. No hand correction has been made.

%description data
Data files for the Festival speech synthesis system.

%description devel
Development files for the Festival speech synthesis system. Install
festival-devel if you want to use Festival's capabilities from within your
own programs, or if you intend to compile other programs using it. Note that
you can also interface with Festival in via the shell or with BSD sockets.

%prep
%oreon_sha256
echo '%{source100_hash}  %{SOURCE100}' | sha256sum -c -
echo '%{source101_hash}  %{SOURCE101}' | sha256sum -c -
echo '%{source200_hash}  %{SOURCE200}' | sha256sum -c -
echo '%{source202_hash}  %{SOURCE202}' | sha256sum -c -
echo '%{source220_hash}  %{SOURCE220}' | sha256sum -c -
echo '%{source221_hash}  %{SOURCE221}' | sha256sum -c -
echo '%{source222_hash}  %{SOURCE222}' | sha256sum -c -
echo '%{source223_hash}  %{SOURCE223}' | sha256sum -c -
echo '%{source224_hash}  %{SOURCE224}' | sha256sum -c -
echo '%{source225_hash}  %{SOURCE225}' | sha256sum -c -
echo '%{source230_hash}  %{SOURCE230}' | sha256sum -c -
%setup -q -n festival

%setup -q -n festival -D -T -b 100
%setup -q -n festival -D -T -b 101

%setup -q -n festival -D -T -b 200
%setup -q -n festival -D -T -b 202
%setup -q -n festival -D -T -b 220
%setup -q -n festival -D -T -b 221
%setup -q -n festival -D -T -b 222
%setup -q -n festival -D -T -b 223
%setup -q -n festival -D -T -b 224
%setup -q -n festival -D -T -b 225

%patch -P100 -p1 -b .pulseaudio
%patch -P101 -p1 -b .use-system-speech-tools
%patch -P102 -p1 -b .use-system-libs
%patch -P103 -p1 -b .filesystem-standard
%patch -P104 -p1 -b .siteinit
%patch -P105 -p1

cat >festival.sysusers.conf <<EOF
u festival - 'festival Daemon' - -
EOF

%build

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/src/lib
export PATH=$(pwd)/bin:$PATH
%configure
make \
  EST=%{_libdir}/speech_tools \
  LIBDIR="%{_libdir}" \
  CFLAGS="$RPM_OPT_FLAGS -fPIC" \
  CXXFLAGS="$RPM_OPT_FLAGS -fPIC"

make -C lib/dicts/cmu

%install

mkdir -p $RPM_BUILD_ROOT%{_libdir}

TOPDIR=$( pwd )
pushd lib/dicts
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/dicts
  cp COPYING.poslex $OLDPWD/COPYING.poslex
  cp cmu/COPYING $OLDPWD/COPYING.cmudict
  for f in wsj.wp39.poslexR wsj.wp39.tri.ngrambin ; do
    install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/festival/dicts/
  done
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/dicts/cmu
  pushd cmu
    for f in allowables.scm cmudict-0.4.diff cmudict-0.4.out \
             cmudict_extensions.scm cmulex.scm cmu_lts_rules.scm; do
      install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/festival/dicts/cmu/
    done
  popd
popd

pushd lib/voices
  for f in $( find . -name COPYING ); do
    n=$( echo $f | sed 's/.*\/\(.*\)\/COPYING/COPYING.\1/' )
    mv $f $OLDPWD/$n
  done
popd
cp -a lib/voices $RPM_BUILD_ROOT%{_datadir}/festival

make INSTALLED_BIN=$RPM_BUILD_ROOT%{_bindir} make_installed_bin_static
install -p -m 755 bin/text2wave $RPM_BUILD_ROOT%{_bindir}

cp -a src/lib/libFestival.a $RPM_BUILD_ROOT%{_libdir}

install -p -m 755 examples/saytime $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -a doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

pushd lib
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival
  for f in *.scm festival.el *.ent *.gram *.dtd *.ngrambin speech.properties ; do
    install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/festival/
  done
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/multisyn/
  install -p -m 644 multisyn/*.scm $RPM_BUILD_ROOT%{_datadir}/festival/multisyn/
popd

sed -r -i '/The master copy of this file is in|and is copied here at build time/d' \
  $RPM_BUILD_ROOT%{_datadir}/festival/*.scm

pushd lib/etc
  mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/festival
  install -p -m 755 */audsp $RPM_BUILD_ROOT%{_libexecdir}/festival
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/examples/
install -p -m 644 examples/intro.text $RPM_BUILD_ROOT%{_datadir}/festival/examples

mkdir -p $RPM_BUILD_ROOT%{_includedir}/festival
cp -a src/include/* $RPM_BUILD_ROOT%{_includedir}/festival

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE230} $RPM_BUILD_ROOT%{_unitdir}/

install -m0644 -D festival.sysusers.conf %{buildroot}%{_sysusersdir}/festival.conf

%files
%doc ACKNOWLEDGMENTS NEWS README.md
%license COPYING COPYING.poslex COPYING.cmudict
%{_bindir}/default_voices
%{_bindir}/festival
%{_bindir}/festival_client
%{_bindir}/festival_server
%{_bindir}/festival_server_control
%{_bindir}/text2wave
%{_bindir}/saytime
%{_libexecdir}/festival
%{_mandir}/man1/*
%{_unitdir}/festival.service
%{_sysusersdir}/festival.conf

%post
%systemd_post festival.service

%preun
%systemd_preun festival.service

%postun
%systemd_postun_with_restart festival.service

%files -n festvox-kal-diphone
%license COPYING.kal_diphone
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/english
%{_datadir}/festival/voices/english/kal_diphone

%files -n festvox-rab-diphone
%license COPYING.rab_diphone
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/english
%{_datadir}/festival/voices/english/rab_diphone

%files -n festvox-awb-arctic-hts
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/us
%{_datadir}/festival/voices/us/cmu_us_awb_cg

%files -n festvox-bdl-arctic-hts
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/us
%{_datadir}/festival/voices/us/cmu_us_bdl_cg

%files -n festvox-clb-arctic-hts
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/us
%{_datadir}/festival/voices/us/cmu_us_clb_cg

%files -n festvox-jmk-arctic-hts
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/us
%{_datadir}/festival/voices/us/cmu_us_jmk_cg

%files -n festvox-rms-arctic-hts
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/us
%{_datadir}/festival/voices/us/cmu_us_rms_cg

%files -n festvox-slt-arctic-hts
%dir %{_datadir}/festival/voices
%dir %{_datadir}/festival/voices/us
%{_datadir}/festival/voices/us/cmu_us_slt_cg

%files data
%{_datadir}/festival
%exclude %{_datadir}/festival/voices/*
%dir %{_datadir}/festival/voices

%files devel
%license COPYING
%{_libdir}/libFestival.a
%dir %{_includedir}/festival
%{_includedir}/festival/*

%changelog
%autochangelog
