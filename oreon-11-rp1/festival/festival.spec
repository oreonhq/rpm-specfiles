%global source0_hash 4c9007426b125290599d931df410e2def51e68a8aeebd89b4a61c7c96c09a4b4
%global source100_hash e7c6e3642dbd5b0d64942bc015a986fdd6244a79e51ec2e8309e63d569e49ea3
%global source101_hash c19430919bca45d5368cd4c82af6153fbcc96a487ebd30b78b5f3c08718b7c07
%global source200_hash 7a357c34086fbba8b813f9750f6b5ba13e2a00478a0a2e78a97981cb76395578
%global source202_hash a017ef70f6d3e64d51d3772ab438eb47a26b529b456dae3cea18936925ec20e8
%global source220_hash d8c4c8042571001ed07ada6588fa20f266fedef326a5e824bdf87d4c8306b5c9
%global source221_hash 5b2cdd41f75ad20cf77ed6ecec497da72d5cc6a095e0f67409f0f536882f8827
%global source222_hash c61f539444b6edb127ae4352632fcf5decdbce80a6132c88d51c809cabc6e357
%global source223_hash 49a0060c3252148b8942c7c0c9e2e7c7b7ef22475fa1871772bfdc39c2896f5f
%global source224_hash d67f0678b2fbbceae73dcf01acb560262bf41171e02e171e81bc16db4d0a347c
%global source225_hash 9f5377db127fe9ce6e9307e821ee45566cce1f4a6c209b9a3c3393a241cbf8a4
Name: festival
Version: 2.5.0
Release:        1%{?dist}
Summary:        Speech synthesis and text-to-speech system
License: MIT AND GPL-1.0-or-later AND TCL AND BSD-3-Clause
URL: http://www.cstr.ed.ac.uk/projects/festival/
Obsoletes: festival-lib < %{version}-%{release}
Obsoletes: festival-speechtools-libs < %{version}-%{release}
Obsoletes: festival-speechtools-libs-devel < %{version}-%{release}
Obsoletes: festival-speechtools-utils < %{version}-%{release}
%global baseURL  http://festvox.org/packed/festival/2.5
Source0:        https://deb.debian.org/debian/pool/main/f/festival/festival_%{version}.orig.tar.gz#/festival-%{version}-release.tar.gz
Source100:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/festlex_POSLEX.tar.gz
Source101:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/festlex_CMU.tar.gz
%global diphoneversion 0.19990610
Source200:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_kallpc16k.tar.gz
Source202:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_rablpc16k.tar.gz
Source220:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_cmu_us_awb_cg.tar.gz
Source221:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_cmu_us_bdl_cg.tar.gz
Source222:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_cmu_us_clb_cg.tar.gz
Source223:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_cmu_us_jmk_cg.tar.gz
Source224:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_cmu_us_rms_cg.tar.gz
Source225:        https://www.cstr.ed.ac.uk/downloads/festival/2.4/voices/festvox_cmu_us_slt_cg.tar.gz
Source230:        festival.service
Patch100:        festival-2.5.0-pulseaudio.patch
Patch101:        festival-2.5.0-use-system-speech-tools.patch
Patch102:        festival-2.5.0-use-system-libs.patch
Patch103:        festival-2.5.0-filesystem-standard.patch
Patch104:        festival-2.5.0-siteinit.patch
Patch105:        festival-configure-c99.patch
%{?systemd_requires}
Requires: festvox-slt-arctic-hts
Requires:  pulseaudio-utils
Requires: festival-data = %{version}-%{release}
Requires: speech-tools-libs
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  speech-tools-libs-devel
BuildRequires:  speech-tools-libs-static
BuildRequires:  systemd
BuildRequires:  texi2html
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source100_hash}" = "none" || { f="%{SOURCE100}"; test -f "$f" || { echo "oreon: missing Source100 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source100_hash}" || { echo "oreon: Source100 hash mismatch" >&2; exit 1; }; }
test "%{source101_hash}" = "none" || { f="%{SOURCE101}"; test -f "$f" || { echo "oreon: missing Source101 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source101_hash}" || { echo "oreon: Source101 hash mismatch" >&2; exit 1; }; }
test "%{source200_hash}" = "none" || { f="%{SOURCE200}"; test -f "$f" || { echo "oreon: missing Source200 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source200_hash}" || { echo "oreon: Source200 hash mismatch" >&2; exit 1; }; }
test "%{source202_hash}" = "none" || { f="%{SOURCE202}"; test -f "$f" || { echo "oreon: missing Source202 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source202_hash}" || { echo "oreon: Source202 hash mismatch" >&2; exit 1; }; }
test "%{source220_hash}" = "none" || { f="%{SOURCE220}"; test -f "$f" || { echo "oreon: missing Source220 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source220_hash}" || { echo "oreon: Source220 hash mismatch" >&2; exit 1; }; }
test "%{source221_hash}" = "none" || { f="%{SOURCE221}"; test -f "$f" || { echo "oreon: missing Source221 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source221_hash}" || { echo "oreon: Source221 hash mismatch" >&2; exit 1; }; }
test "%{source222_hash}" = "none" || { f="%{SOURCE222}"; test -f "$f" || { echo "oreon: missing Source222 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source222_hash}" || { echo "oreon: Source222 hash mismatch" >&2; exit 1; }; }
test "%{source223_hash}" = "none" || { f="%{SOURCE223}"; test -f "$f" || { echo "oreon: missing Source223 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source223_hash}" || { echo "oreon: Source223 hash mismatch" >&2; exit 1; }; }
test "%{source224_hash}" = "none" || { f="%{SOURCE224}"; test -f "$f" || { echo "oreon: missing Source224 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source224_hash}" || { echo "oreon: Source224 hash mismatch" >&2; exit 1; }; }
test "%{source225_hash}" = "none" || { f="%{SOURCE225}"; test -f "$f" || { echo "oreon: missing Source225 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source225_hash}" || { echo "oreon: Source225 hash mismatch" >&2; exit 1; }; }
%setup -q -n festival

# dictionaries
%setup -q -n festival -D -T -b 100
%setup -q -n festival -D -T -b 101

# voices
%setup -q -n festival -D -T -b 200
%setup -q -n festival -D -T -b 202
%setup -q -n festival -D -T -b 220
%setup -q -n festival -D -T -b 221
%setup -q -n festival -D -T -b 222
%setup -q -n festival -D -T -b 223
%setup -q -n festival -D -T -b 224
%setup -q -n festival -D -T -b 225

%patch 100 -p1 -b .pulseaudio
%patch 101 -p1 -b .use-system-speech-tools
%patch 102 -p1 -b .use-system-libs
%patch 103 -p1 -b .filesystem-standard
%patch 104 -p1 -b .siteinit
%patch 105 -p1

# Create a sysusers.d config file
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
%oreon_autofiles festvox-kal-diphone usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-rab-diphone usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-awb-arctic-hts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-bdl-arctic-hts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-clb-arctic-hts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-jmk-arctic-hts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-rms-arctic-hts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles festvox-slt-arctic-hts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post festival.service
%preun

%systemd_preun festival.service
%postun

%systemd_postun_with_restart festival.service
%files -f %{oreon_filedir}/main.list
%files -n festvox-kal-diphone -f %{oreon_filedir}/festvox-kal-diphone.list
%files -n festvox-rab-diphone -f %{oreon_filedir}/festvox-rab-diphone.list
%files -n festvox-awb-arctic-hts -f %{oreon_filedir}/festvox-awb-arctic-hts.list
%files -n festvox-bdl-arctic-hts -f %{oreon_filedir}/festvox-bdl-arctic-hts.list
%files -n festvox-clb-arctic-hts -f %{oreon_filedir}/festvox-clb-arctic-hts.list
%files -n festvox-jmk-arctic-hts -f %{oreon_filedir}/festvox-jmk-arctic-hts.list
%files -n festvox-rms-arctic-hts -f %{oreon_filedir}/festvox-rms-arctic-hts.list
%files -n festvox-slt-arctic-hts -f %{oreon_filedir}/festvox-slt-arctic-hts.list
%files -n festival-data -f %{oreon_filedir}/festival-data.list
%files -n festival-devel -f %{oreon_filedir}/festival-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.0-1
- Import
