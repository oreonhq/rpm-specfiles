%global source0_hash 74447d7adb3bd119adae7915ba9422b7da553556f979ac4ee53a262d94d47b47
%global dkcommit 1ceb4de
%global optflags %{optflags} -std=gnu17
Name:		julius
Version:	4.6
Release:        1%{?dist}
Summary:        Large vocabulary continuous speech recognition (LVCSR) decoder software
License:	BSD-3-Clause AND MIT
URL:		https://github.com/julius-speech/julius
Source0:        https://github.com/julius-speech/julius/archive/v%{version}.tar.gz
Source1:	dictation-kit-%{dkcommit}.tar.xz
Patch0:		julius-4.6-DESTDIR.patch
Patch1:		julius-4.5-sharedlibs.patch
Patch2:		julius-4.5-cpuidfix.patch
Patch3:		julius-ldflags.patch
Patch4:		187.patch
Patch5:		julius-4.6-configure-fixup.patch
Patch6:		julius-4.6-noviz.patch
Patch7:		julius-configure-c99.patch
Patch8:		julius-4.6-bigendian-cast-fix.patch
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nkf
BuildRequires:  perl(Jcode)
BuildRequires:  perl-generators
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

%ifarch i686 x86_64
%configure
%else
%configure --disable-openmp
%endif
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
mv %{buildroot}%{_bindir}/jcontrol %{buildroot}%{_bindir}/julius-jcontrol
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n julius-devel -f %{oreon_filedir}/julius-devel.list
%files -n julius-japanese-models -f %{oreon_filedir}/julius-japanese-models.list

%changelog

%autochangelog
