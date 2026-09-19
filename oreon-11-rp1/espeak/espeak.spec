%global source0_hash bf9a17673adffcc28ff7ea18764f06136547e97bbd9edf2ec612f09b207f0659

# package options
%global with_portaudio no

%if "%{with_portaudio}" == "yes"
%global backend runtime
%else
%global backend pulseaudio
%endif

Name:           espeak
Version:        1.48.04
Release:        34%{?dist}
Summary:        Software speech synthesizer (text-to-speech)

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://espeak.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.zip
# Upstream ticket: https://sourceforge.net/p/espeak/patches/10/
Source1:        espeak.1
Patch0:         espeak-1.47-makefile-nostaticlibs.patch
Patch1:         espeak-1.47-ftbs-ld-libm.patch
# Upstream ticket: https://sourceforge.net/p/espeak/patches/10/
Patch2:         espeak-1.48-help-fix.patch
# Upstream ticket: https://sourceforge.net/p/espeak/bugs/105/
Patch3:         espeak-1.47-wav-close.patch
Patch4:         espeak-1.48-gcc-6-fix.patch
# Upstream-accepted patch (to the new fork espeak-ng)
# https://github.com/espeak-ng/espeak-ng/commit/7659aaa2e88cc0401d032d04602731ca45070fab
Patch5:         espeak-1.48-read-fifo.patch
Requires(post): coreutils
%{?ldconfig:Requires(post): %ldconfig}
%if "%{with_portaudio}" == "yes"
BuildRequires:  portaudio-devel
%endif
BuildRequires:  pulseaudio-libs-devel gcc-c++
BuildRequires: make

%description
eSpeak is a software speech synthesizer for English and other languages.

eSpeak produces good quality English speech. It uses a different synthesis
method from other open source TTS engines, and sounds quite different.
It's perhaps not as natural or "smooth", but some people may find the
articulation clearer and easier to listen to for long periods. eSpeak supports
several languages, however in most cases these are initial drafts and need more
work to improve them.

It can run as a command line program to speak text from a file or from stdin.

%package devel
Summary: Development files for espeak
Requires: %{name} = %{version}-%{release}

%description devel
Development files for eSpeak, a software speech synthesizer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n espeak-%{version}-source
%patch -P 0 -p1 -b .nostaticlibs
%patch -P 1 -p1 -b .ftbs-ld-libm
%patch -P 2 -p1 -b .help-fix
%patch -P 3 -p1 -b .wav-close
%patch -P 4 -p1 -b .1.48-gcc-6-fix
%patch -P 5 -p1 -b .read-fifo

# Fix file permissions
find . -type f -exec chmod 0644 {} ";"
# Prepare documentation
rm -rf docs/images/.svn
mv docs html
sed -i 's/\r//' License.txt
# Compile against portaudio v19 (see ReadMe)
cp -f src/portaudio19.h src/portaudio.h
# Don't use the included binary voice dictionaries; we compile these from source
rm -f espeak-data/*_dict

%build
# Compile espeak
cd src
%make_build CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" DATADIR=%{_datadir}/espeak-data AUDIO=%{backend}

# Compile the TTS voice dictionaries
export ESPEAK_DATA_PATH=$RPM_BUILD_DIR/espeak-%{version}-source
cd ../dictsource
# Strange sed regex to parse ambiguous output from 'speak --voices', filled upstream BZ 3608811
for voice in $(../src/speak --voices | \
LANG=C sed -n '/Age\/Gender/ ! s/ *[0-9]\+ *\([^ ]\+\) *M\? *[^ ]\+ *\(\((\|[A-Z]\)[^ ]\+\)\? *\([^ ]\+\).*/\1 \4/ p' | \
sort | uniq); do \
    ../src/speak --compile=$voice; \
done

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/espeak-%{version}-source/src
%make_install BINDIR=%{_bindir} INCDIR=%{_includedir}/espeak LIBDIR=%{_libdir} DATADIR=%{_datadir}/espeak-data AUDIO=%{backend}
# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -pf %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

%post
%{?ldconfig}

%ldconfig_postun

%files
%doc ReadMe ChangeLog.txt License.txt html
%{_mandir}/man1/espeak.1*
%{_bindir}/espeak
%{_datadir}/espeak-data
%{_libdir}/libespeak.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/espeak

%changelog
%autochangelog
