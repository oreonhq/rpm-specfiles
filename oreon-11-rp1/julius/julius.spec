%global source0_hash 74447d7adb3bd119adae7915ba9422b7da553556f979ac4ee53a262d94d47b47

%global dkcommit 1ceb4de

# julius has code that takes advantage of using func() to allow for different number/type of parameters
# c23 no longer permits this, and instead of rewriting this, i'm just going to pretend it is 2017
%global optflags %{optflags} -std=gnu17

Name:		julius
Version:	4.6
Release:	10%{?dist}
Summary:	Large vocabulary continuous speech recognition (LVCSR) decoder software
License:	BSD-3-Clause AND MIT
URL:		https://github.com/julius-speech/julius
Source0:	https://github.com/julius-speech/julius/archive/v%{version}.tar.gz
# Need to generate from git
# BE SURE YOU HAVE git-lfs installed before doing a clone
# git clone https://github.com/julius-speech/dictation-kit.git
# cd dictation-kit
# rm -rf bin src
# cd ..
# tar --exclude-vcs -cJf dictation-kit-%%{dkcommit}.tar.xz dictation-kit
Source1:	dictation-kit-%{dkcommit}.tar.xz
Patch0:		julius-4.6-DESTDIR.patch
Patch1:		julius-4.5-sharedlibs.patch
Patch2:		julius-4.5-cpuidfix.patch
Patch3:		julius-ldflags.patch
# https://github.com/julius-speech/julius/pull/187
Patch4:		187.patch
Patch5:		julius-4.6-configure-fixup.patch
# The viz code depends on GTK1 and we don't want it
Patch6:		julius-4.6-noviz.patch
Patch7:		julius-configure-c99.patch
# https://github.com/julius-speech/julius/pull/196
Patch8:		julius-4.6-bigendian-cast-fix.patch

BuildRequires:	perl-generators
BuildRequires:	perl(Jcode), alsa-lib-devel, libsndfile-devel, pulseaudio-libs-devel, zlib-devel, readline-devel
BuildRequires:	SDL2-devel
BuildRequires:	bison, flex, nkf
BuildRequires:	autoconf, automake, libtool, gettext-devel
BuildRequires:	make
# Requires:

%description
"Julius" is a high-performance, two-pass large vocabulary continuous speech
recognition (LVCSR) decoder software for speech-related researchers and
developers. Based on word N-gram and context-dependent HMM, it can perform
almost real-time decoding on most current PCs in 60k word dictation task.
Major search techniques are fully incorporated such as tree lexicon, N-gram
factoring, cross-word context dependency handling, enveloped beam search,
Gaussian pruning, Gaussian selection, etc. Besides search efficiency, it is
also modularized carefully to be independent from model structures, and
various HMM types are supported such as shared-state triphones and
tied-mixture models, with any number of mixtures, states, or phones.
Standard formats are adopted to cope with other free modeling toolkit such
as HTK, CMU-Cam SLM toolkit, etc.

%package devel
Requires:	julius = %{version}-%{release}
Summary:	Development files and libraries for libjulius and libsent

%description devel
Development files and libraries	for libjulius and libsent.

%package japanese-models
BuildArch:	noarch
Requires:	julius = %{version}-%{release}
Summary:	Julius Japanese language model and acoustic models
License:	LicenseRef-Julius-dictation-kit

%description japanese-models
A Japanese language model (20k-word trained by newspaper article) and acoustic
models (Phonetic tied-mixture triphone / monophone) for use with Julius.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1
%patch -P0 -p1 -b .DESTDIR
%patch -P1 -p1 -b .shared
%patch -P2 -p1 -b .cpuidfix
%patch -P3 -p1
%patch -P4 -p1 -b .187
%patch -P5 -p1 -b .fixup
%patch -P6 -p1 -b .noviz
%patch -P7 -p1 -b .c99
%patch -P8 -p1 -b .cast-fix

# Fix end-of-line encoding
sed -i 's/\r//' Release.txt
cp /usr/share/gettext/config.rpath support/
autoupdate
autoreconf -ifv || :

# remove msvc dir
rm -rf msvc

%build
# OpenMP only seems to find all its functions on these architectures.
%ifarch i686 x86_64
%configure
%else
%configure --disable-openmp
%endif
# this fails
# make %{?_smp_mflags}
make

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
make install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_libdir}/*.so.*

mkdir -p %{buildroot}%{_datadir}/julius/
cp -a Sample.jconf %{buildroot}%{_datadir}/julius/
pushd dictation-kit
cp *conf %{buildroot}%{_datadir}/julius/
cp -a model/ %{buildroot}%{_datadir}/julius/
popd

# rename to avoid conflict with Oracle Java
mv %{buildroot}%{_bindir}/jcontrol %{buildroot}%{_bindir}/julius-jcontrol

%ldconfig_scriptlets

%files
%doc Release.txt Release-ja.txt
%license LICENSE
%{_bindir}/accept_check
%{_bindir}/adinrec
%{_bindir}/adintool
%{_bindir}/adintool-gui
%{_bindir}/binlm2arpa
%{_bindir}/dfa_determinize
%{_bindir}/dfa_minimize
%{_bindir}/generate
%{_bindir}/generate-ngram
%{_bindir}/gram2sapixml.pl
%{_bindir}/jclient.pl
%{_bindir}/julius-jcontrol
%{_bindir}/julius
%{_bindir}/mkbingram
%{_bindir}/mkbinhmm
%{_bindir}/mkbinhmmlist
%{_bindir}/mkdfa.pl
%{_bindir}/mkdfa.py
%{_bindir}/mkfa
%{_bindir}/mkgshmm
%{_bindir}/mkss
%{_bindir}/nextword
%{_bindir}/yomi2voca.pl
%{_libdir}/libjulius.so.*
%{_libdir}/libsent.so.*
# %%lang(ja) %%{_mandir}/ja/man1/*
# %%{_mandir}/man1/*
%dir %{_datadir}/julius/
%{_datadir}/julius/*conf

%files devel
%{_bindir}/libjulius-config
%{_bindir}/libsent-config
%{_includedir}/julius/
%{_includedir}/sent/
%{_libdir}/libjulius.so
%{_libdir}/libsent.so
%{_libdir}/pkgconfig/*.pc

%files japanese-models
%{_datadir}/julius/model/

%changelog
%autochangelog
