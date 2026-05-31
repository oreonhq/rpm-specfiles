%global source0_hash 4c9007426b125290599d931df410e2def51e68a8aeebd89b4a61c7c96c09a4b4
%global source100_hash e7c6e3642dbd5b0d64942bc015a986fdd6244a79e51ec2e8309e63d569e49ea3
%global source101_hash c19430919bca45d5368cd4c82af6153fbcc96a487ebd30b78b5f3c08718b7c07
%global source200_hash 809c4ab5ed9e4df4a658b58d5c56fe35055723f00d81a238168f5a1ebdaed08c
%global source202_hash ecd14b77c528e94dfb076e44050102fe8fba57e5fe813acf78a66629317f52a5
%global source220_hash b2adbdfeda0cba289bb4da68dd14114d3eb3e7f72049cc8d2cbdfb2df39f6934
%global source221_hash 1dc6792af9e2c1660a46fe499aa67af4affa665a0bdc08207cc11719baa62f6d
%global source222_hash 8473e5bb37b2101eb17c1b25577d340710f48c862bebcd61d424f9aff43c0dd7
%global source223_hash 711db388bc500331cfda86a46a72193ca1e2c9dc7d5ef16dfc86827e499946f2
%global source224_hash 3167afa3a6ffb5bbc305c94a1e6b671e40783a87a49372fce04c54942872c421
%global source225_hash 78cb93e361ab016fd23833c56853ddf21e2f1356310f54eed1c09a9755ce9f43

Name: festival
Summary: Speech synthesis and text-to-speech system
Version: 2.5.0
Release: %autorelease

URL: http://www.cstr.ed.ac.uk/projects/festival/
# The Emacs file is GPL+, there is one TCL-licensed source file, and
# the hts_engine module is covered by the three-clause BSD license.
License: MIT AND GPL-1.0-or-later AND TCL AND BSD-3-Clause

Obsoletes: festival-lib < %{version}-%{release}Obsoletes: festival-speechtools-libs < %{version}-%{release}Obsoletes: festival-speechtools-libs-devel < %{version}-%{release}Obsoletes: festival-speechtools-utils < %{version}-%{release}
# Files needed for everything...
%global baseURL  http://festvox.org/packed/festival/2.5
Source0:        http://festvox.org/packed/festival/2.5/festival-2.5.0-release.tar.gz

### DICTIONARIES
# Generic English dictionary
Source100:        http://festvox.org/packed/festival/2.5/festlex_POSLEX.tar.gz
# American English dictionary
Source101:        http://festvox.org/packed/festival/2.5/festlex_CMU.tar.gz
# OALD isn't included because it's got a more restrictive (non-commercial
# only) license. OALD voices not included for same reason.

# Note on voice versions: I'm simply using the file date of the newest file
# in each set of tarballs. It happens that the dates for all files from each
# source (diphone, cmu_arctic, etc.) match, which is handy.

### DIPHONE VOICES
%global diphoneversion 0.19990610
Source200:        http://festvox.org/packed/festival/2.5/voices/festvox_kallpc16k.tar.gz
Source202:        http://festvox.org/packed/festival/2.5/voices/festvox_rablpc16k.tar.gz

### HTS VOICES
Source220:        http://festvox.org/packed/festival/2.5/voices/festvox_cmu_us_awb_cg.tar.gz
Source221:        http://festvox.org/packed/festival/2.5/voices/festvox_cmu_us_bdl_cg.tar.gz
Source222:        http://festvox.org/packed/festival/2.5/voices/festvox_cmu_us_clb_cg.tar.gz
Source223:        http://festvox.org/packed/festival/2.5/voices/festvox_cmu_us_jmk_cg.tar.gz
Source224:        http://festvox.org/packed/festival/2.5/voices/festvox_cmu_us_rms_cg.tar.gz
Source225:        http://festvox.org/packed/festival/2.5/voices/festvox_cmu_us_slt_cg.tar.gz

### Hispavoces Spanish voices left out; did they move?

### Multisyn voices left out because they're ~ 100MB each.

### MBROLA voices left out, because they require MBROLA, which ain't free.

### Systemd service file.
Source230: festival.service

Patch100: festival-2.5.0-pulseaudio.patch
Patch101: festival-2.5.0-use-system-speech-tools.patch
Patch102: festival-2.5.0-use-system-libs.patch
Patch103: festival-2.5.0-filesystem-standard.patch
Patch104: festival-2.5.0-siteinit.patch
Patch105: festival-configure-c99.patch

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

# Requires: festival-voice
# The hard dep below provides a festival-voice, no need to require it here.

# This is hard-coded as a requirement because it's the smallest voice (and,
# subjectively I think the most pleasant to listen to and so a good
# default).
#
# Ideally, this would be a "suggests" instead of a hard requirement.
#
# Update: with the new nitech versions of the voices, slt-arctic is no
# longer the smallest. But... AWB has a strong scottish accent, and JMK a
# kind of odd canadian one, so they're not great candidates for inclusion.
# And I find RMS a bit hard to understand. BDL isn't much smaller than SLT,
# and since I like it better, I think I'm going to keep it as the default
# for a price 12k. So, in case anyone later questions why this is the
# default, there's the answer. :)
Requires: festvox-slt-arctic-hts

# festival-2.5.0-pulseaudio.patch makes use of paplay.
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

# This is last as a lovely hack to make sure Version gets set back
# to what it should be. Grr.
%package devel
Summary: Development files for the Festival speech synthesis system
# Note: rpmlint complains incorrectly about
# "no-dependency-on festival"
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source100_hash}" = "none" || { f="%{SOURCE100}"; test -f "$f" || { echo "oreon: missing Source100 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source100_hash}" || { echo "oreon: Source100 hash mismatch" >&2; exit 1; }; }
test "%{source101_hash}" = "none" || { f="%{SOURCE101}"; test -f "$f" || { echo "oreon: missing Source101 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source101_hash}" || { echo "oreon: Source101 hash mismatch" >&2; exit 1; }; }
test "%{source200_hash}" = "none" || { f="%{SOURCE200}"; test -f "$f" || { echo "oreon: missing Source200 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source200_hash}" || { echo "oreon: Source200 hash mismatch" >&2; exit 1; }; }
test "%{source202_hash}" = "none" || { f="%{SOURCE202}"; test -f "$f" || { echo "oreon: missing Source202 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source202_hash}" || { echo "oreon: Source202 hash mismatch" >&2; exit 1; }; }
test "%{source220_hash}" = "none" || { f="%{SOURCE220}"; test -f "$f" || { echo "oreon: missing Source220 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source220_hash}" || { echo "oreon: Source220 hash mismatch" >&2; exit 1; }; }
test "%{source221_hash}" = "none" || { f="%{SOURCE221}"; test -f "$f" || { echo "oreon: missing Source221 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source221_hash}" || { echo "oreon: Source221 hash mismatch" >&2; exit 1; }; }
test "%{source222_hash}" = "none" || { f="%{SOURCE222}"; test -f "$f" || { echo "oreon: missing Source222 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source222_hash}" || { echo "oreon: Source222 hash mismatch" >&2; exit 1; }; }
test "%{source223_hash}" = "none" || { f="%{SOURCE223}"; test -f "$f" || { echo "oreon: missing Source223 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source223_hash}" || { echo "oreon: Source223 hash mismatch" >&2; exit 1; }; }
test "%{source224_hash}" = "none" || { f="%{SOURCE224}"; test -f "$f" || { echo "oreon: missing Source224 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source224_hash}" || { echo "oreon: Source224 hash mismatch" >&2; exit 1; }; }
test "%{source225_hash}" = "none" || { f="%{SOURCE225}"; test -f "$f" || { echo "oreon: missing Source225 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source225_hash}" || { echo "oreon: Source225 hash mismatch" >&2; exit 1; }; }
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

%patch -P100 -p1 -b .pulseaudio
%patch -P101 -p1 -b .use-system-speech-tools
%patch -P102 -p1 -b .use-system-libs
%patch -P103 -p1 -b .filesystem-standard
%patch -P104 -p1 -b .siteinit
%patch -P105 -p1

# Create a sysusers.d config file
cat >festival.sysusers.conf <<EOF
u festival - 'festival Daemon' - -
EOF

%build

# build the main program
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/src/lib
# instead of doing this, maybe we should patch the make process
# so it looks in the right place explicitly:
export PATH=$(pwd)/bin:$PATH
%configure
make \
  EST=%{_libdir}/speech_tools \
  LIBDIR="%{_libdir}" \
  CFLAGS="$RPM_OPT_FLAGS -fPIC" \
  CXXFLAGS="$RPM_OPT_FLAGS -fPIC"

# build the patched CMU dictionary
make -C lib/dicts/cmu


%install
# "make install" for this package is, um, "interesting". It seems geared for
# local user-level builds. So, rather than doing that and then patching it
# up, do the right parts by hand as necessary.

# Create %%{_libdir} because make install copies to it without first creating.
mkdir -p $RPM_BUILD_ROOT%{_libdir}

# install the dictionaries
TOPDIR=$( pwd )
pushd lib/dicts
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/dicts
  # we want to put the licenses in the docs...
  cp COPYING.poslex $OLDPWD/COPYING.poslex
  cp cmu/COPYING $OLDPWD/COPYING.cmudict
  for f in wsj.wp39.poslexR wsj.wp39.tri.ngrambin ; do
    install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/festival/dicts/
  done
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/dicts/cmu
  pushd cmu
    # note I'm keeping cmudict-0.4.diff and cmudict_extensions.scm to
    # satisfy the "all changes clearly marked" part of the license -- these
    # are the changes. And yes, the ".out" file is the one actually used.
    # Sigh.
    for f in allowables.scm cmudict-0.4.diff cmudict-0.4.out \
             cmudict_extensions.scm cmulex.scm cmu_lts_rules.scm; do
      install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/festival/dicts/cmu/
    done
  popd
popd

# install the voices
pushd lib/voices
  # get the licenses. This is probably too clever by half, but oh well.
  for f in $( find . -name COPYING ); do
    n=$( echo $f | sed 's/.*\/\(.*\)\/COPYING/COPYING.\1/' )
    mv $f $OLDPWD/$n
  done
popd
cp -a lib/voices $RPM_BUILD_ROOT%{_datadir}/festival

# okay, now install the main festival program.

# binaries:
make INSTALLED_BIN=$RPM_BUILD_ROOT%{_bindir} make_installed_bin_static
install -p -m 755 bin/text2wave $RPM_BUILD_ROOT%{_bindir}

# install the library
cp -a src/lib/libFestival.a $RPM_BUILD_ROOT%{_libdir}

# this is just nifty. and it's small.
install -p -m 755 examples/saytime $RPM_BUILD_ROOT%{_bindir}

# man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -a doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

# lib: the bulk of the program -- the scheme stuff and so on
pushd lib
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival
  for f in *.scm festival.el *.ent *.gram *.dtd *.ngrambin speech.properties ; do
    install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/festival/
  done
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/multisyn/
  install -p -m 644 multisyn/*.scm $RPM_BUILD_ROOT%{_datadir}/festival/multisyn/
popd

# Remove comments that look like this:
#
# 	;;; The master copy of this file is in /usr/{lib,lib64}/speech_tools/lib/siod/cstr.scm
#
# Such comments exist in files generated by lib/Makefile and thus vary between
# builds based on the value of %_libdir. Furthermore,
# /usr/lib*/speech_tools/* might not exist on the user system.
sed -r -i '/The master copy of this file is in|and is copied here at build time/d' \
  $RPM_BUILD_ROOT%{_datadir}/festival/*.scm

# "etc" -- not in the configuration sense, but in the sense of "extra helper
# binaries".
pushd lib/etc
  mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/festival
  install -p -m 755 */audsp $RPM_BUILD_ROOT%{_libexecdir}/festival
popd

# copy in the intro.text. It's small and makes (intro) work. in the future,
# we may want include more examples in an examples subpackage
mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/examples/
install -p -m 644 examples/intro.text $RPM_BUILD_ROOT%{_datadir}/festival/examples


# header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}/festival
cp -a src/include/* $RPM_BUILD_ROOT%{_includedir}/festival


# systemd service
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.0-1
- Import
