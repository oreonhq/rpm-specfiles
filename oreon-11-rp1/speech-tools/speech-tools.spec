%global source0_hash e4fd97ed78f14464358d09f36dfe91bc1721b7c0fa6503e04364fb5847805dcc
Name:           speech-tools
Version:        2.5
Release:        28%{?dist}
Summary:        Edinburgh speech tools library
License:        MIT-Festival
URL:            http://festvox.org
Source0:        http://festvox.org/packed/festival/%{version}/speech_tools-%{version}.0-release.tar.gz
Source1: LICENSE
Patch0: enable_shared.patch
Patch1: fix_editline_types.patch
%define _legacy_common_support 1
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
The Edinburgh speech tools system is a library of C++ classes, functions
and utility programs that are frequently used in speech software.
The system compiles to a single Unix library .a file
which can be linked with software.
At present, C++ classes for several useful speech and language classes
have been written, along with audio software
and some basic signal processing software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir speech_tools
%oreon_prep
%build

%configure
%__make CFLAGS="%{optflags} -fPIC -flto -fno-lto" CXXFLAGS="%{optflags} -fPIC -flto -fno-lto -std=c++17" LDFLAGS="$LDFLAGS -flto -fno-lto"
%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{SOURCE1} .
install -p -m 755 main/{bcat,ch_lab,ch_track,ch_utt,ch_wave,dp,na_play,na_record,ngram_build,ngram_test,ols,ols_test,pda,pitchmark,scfg_make,scfg_parse,scfg_test,scfg_train,sig2fv,sigfilter,spectgen,tilt_analysis,tilt_synthesis,viterbi,wagon,wagon_test,wfst_build,wfst_run} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
install -p -m 755 lib/*.so* %{buildroot}%{_libdir}
install -p -m 644 lib/*.a %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/speech_tools
cp -dr include/* %{buildroot}%{_includedir}/speech_tools
rm -r %{buildroot}%{_includedir}/speech_tools/win32
mkdir -p %{buildroot}%{_libdir}/speech_tools/base_class
install -p -m 644 base_class/*.cc %{buildroot}%{_libdir}/speech_tools/base_class
install -p -m 644 base_class/*.h %{buildroot}%{_libdir}/speech_tools/base_class
mkdir -p %{buildroot}%{_libdir}/speech_tools
cp -dr config/ %{buildroot}%{_libdir}/speech_tools
mkdir -p %{buildroot}%{_libdir}/speech_tools/lib/siod
install -p -m 644 lib/siod/*.scm %{buildroot}%{_libdir}/speech_tools/lib/siod
mkdir -p %{buildroot}%{_libdir}/speech_tools/include
cp -r %{buildroot}%{_includedir}/speech_tools/* %{buildroot}%{_libdir}/speech_tools/include
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package libs
Summary: Edinburgh speech tools libraries
Obsoletes: festival-speechtools-libs < 1.2.96-40
%description libs
The shared libraries needed by speech-tools and other software.

%ldconfig_scriptlets libs

%package libs-devel
Summary: Development files for the speech-tools libraries
Requires: speech-tools-libs%{?_isa} = %{version}-%{release}
Obsoletes: festival-speechtools-devel < 1.2.96-40
%description libs-devel
This package contains the development related files for the speech-tools
libraries.

%package libs-static
Summary: Static libraries of speech-tools, so far needed by at least festival
Requires: speech-tools-libs-devel%{?_isa} = %{version}-%{release}
%description libs-static
This package contains the static libraries for speech-tools.
They are so far definitely needed for festival,
but they might be depended upon by some third-party developers as well.

%files -f %{oreon_filedir}/main.list
%files -n speech-tools-libs -f %{oreon_filedir}/speech-tools-libs.list
%files -n speech-tools-libs-devel -f %{oreon_filedir}/speech-tools-libs-devel.list
%files -n speech-tools-libs-static -f %{oreon_filedir}/speech-tools-libs-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5-28
- Prepare for Oreon 11 (RP1)
