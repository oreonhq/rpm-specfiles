%global source0_hash b7347bfc6232ec245097dd88e26dc368ee9210079f3feb65dacbc4906f19db61

%global commit a6208406d94a1da978f435605072ee5caefe1491
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: Audio effects processing rack for guitar
Name:    rakarrack
Version: 0.6.2
Release: 0.34.20150814git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://%{name}.sourceforge.net/
#S#ource0: http://downloads.sourceforge.net/%#{name}/%#{name}-%#{version}.tar.bz2
#S#ource0: http://rakarrack.git.sourceforge.net/git/gitweb.cgi?p=rakarrack/rakarrack;a=snapshot;h=47245c3fd30dc326fedd7cdae444ddcf0fd97490;sf=tgz
#S#ource0:  rakarrack-47245c3.tar.gz
# The snapshot download is created when accessed:
# https://sourceforge.net/p/rakarrack/git/ci/master/tree/
# Click: Download Snapshot, the download will then succeed for some hours.
Source0: http://sourceforge.net/code-snapshots/git/r/ra/rakarrack/git.git/rakarrack-git-%{commit}.zip
Patch1:  rakarrack-0.6.2.format-security.diff

Requires: hicolor-icon-theme

# mod of doc dir in configure.in requires autoconf/automake
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: automake
# not required (https://fedoraproject.org/wiki/Packaging:Guidelines#Exceptions_2)
# BuildRequires: gcc-c++ # just a reminder
BuildRequires: jack-audio-connection-kit-devel alsa-lib-devel alsa-utils
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: fltk1.3-devel
BuildRequires: libXpm-devel libpng-devel libjpeg-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

%description
Rakarrack is a basic rack of effects for guitar. 10 effects. Two EQ
(multi-band and parametric), distortion, overdrive, echo, chorus,
Flanger, Phaser, compression and Reverb. Real time processing. JACK
support. Online tuner. Bank & Preset management.

Most of the effects are based on the magnificent work done by Paul
Nasca Octavian in ZynAddSubFX synthesizer. The compressor is based on
ArtsCompressor of Matthias Kretzer & Stefen Westerfeld. The tuner was
adapted from Tuneit, a tuner in text mode created by Mario Lang. Paul
Nasca is our hero and a continuous inspiration

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# for releases
#%#setup -q -n %#{name}-%#{version}
# for git snapshot
%setup -q -n %{name}-git-%{commit}

%patch -P1 -p1 -b .format-security

# Fix spurious-executable-perm
find ./src/ -type f -perm /a=x -name "*" -exec chmod a-x {} \;
#find -type f -exec chmod a-x {} src\;
#-exec chmod a-x {} src\;

%{__sed} -i 's/Icon=icono_rakarrack_128x128/Icon=rakarrack/' data/%{name}.desktop
%{__sed} -i 's/Guitar Effects Processor/Real-time audio effects processing rack for guitar/' data/%{name}.desktop
echo "GenericName=Digital audio effects processor" >> data/%{name}.desktop
echo "Version=1.0" >> data/%{name}.desktop

%build
./autogen.sh

%define optimise ""
# ensure the builder arch does not influence the build 
%ifarch x86_64
  %define optimise "--enable-sse2"
%endif
%ifarch %{ix86}
  %define optimise "--enable-sse"
%endif  
 
%configure --enable-docdir=yes --docdir=%{_pkgdocdir} %{optimise}
  
# if DFortifySource is not passed to compile, try del smp_mflags
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install

# move icons to the proper freedesktop location
for dim in 32x32 64x64 128x128; do
  %{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/$dim/apps
  %{__mv} %{buildroot}%{_datadir}/pixmaps/icono_%{name}_$dim.png \
      %{buildroot}%{_datadir}/icons/hicolor/$dim/apps/%{name}.png
done

# extra desktop file categories are allowed if prepended with X-
BASE="X-Fedora AudioVideo"
XTRA="X-DigitalProcessing X-Jack"
MIXER="Mixer"

%{__mkdir} -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor "" \
  `for c in ${BASE} ${XTRA} ${MIXER}; do echo "--add-category $c " ; done` \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/rakarrack.desktop

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/PACKAGERS.README
%{_bindir}/%{name}
%{_bindir}/rakconvert
%{_bindir}/rakgit2new
%{_bindir}/rakverb
%{_bindir}/rakverb2
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
