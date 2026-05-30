%global source0_hash ab1555fe5adc3f99f1d4a1a0eb1596d329fd6d74f1464a0097c81f53c0cf9e5c

%ifnarch s390x
%bcond_without check
%else
# https://github.com/festvox/flite/issues/67
%bcond_with check
%endif

# https://github.com/festvox/flite/pull/92#issuecomment-1481980430
%global _smp_mflags -j1

%global abi 1

Name:           flite
Version:        2.2
Release:        13%{?dist}
Summary:        Small, fast speech synthesis engine (text-to-speech)
License:        MIT
URL:            http://cmuflite.org/

Source0:        https://github.com/festvox/flite/archive/v%{version}/flite-%{version}.tar.gz
Patch0:         flite-2.2-lto.patch
# fixes build with texinfo-7.0+, see https://lists.gnu.org/archive/html/bug-texinfo/2022-11/msg00036.html
Patch1:         flite-2.2-texinfo-7.0.patch
# https://github.com/festvox/flite/issues/86
Patch2:         flite-2.2-parallel-make.patch
# https://github.com/festvox/flite/pull/90
Patch3:         flite-2.2-tests.patch
# texi2pdf
# WARNING see explanation about PDF doc below.
#BuildRequires:  texinfo-tex
BuildRequires:  gcc
BuildRequires:  autoconf automake libtool
BuildRequires:  ed alsa-lib-devel
BuildRequires: make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  texinfo


%description
Flite (festival-lite) is a small, fast run-time speech synthesis engine
developed at CMU and primarily designed for small embedded machines and/or
large servers. Flite is designed as an alternative synthesis engine to
Festival for voices built using the FestVox suite of voice building tools.


%package devel
Summary: Development files for flite
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Flite, a small, fast speech synthesis engine.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1 -b .lto
%patch -P1 -p1 -b .ti7
%patch -P2 -p1 -b .pmake
%patch -P3 -p1 -b .tst


%build
autoreconf -vif
%configure \
    --enable-shared \
    --with-audio=pulseaudio \

%make_build
# Build documentation
cd doc
# WARNING "make doc" provides a huge PDF file. It was decided not to produce/package it.
#make doc
make flite.html


%install
%make_install
rm %{buildroot}%{_libdir}/libflite*.a


%if %{with check}
%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check
%endif


%files
%license COPYING
%doc ACKNOWLEDGEMENTS
%doc doc/html
%doc README.md
%{_libdir}/libflite_cmu_{grapheme,indic}_{lang,lex}.so.{%{abi},%{version}}
%{_libdir}/libflite_cmulex.so.{%{abi},%{version}}
%{_libdir}/libflite_cmu_time_awb.so.{%{abi},%{version}}
%{_libdir}/libflite_cmu_us_{awb,kal,kal16,rms,slt}.so.{%{abi},%{version}}
%{_libdir}/libflite.so.{%{abi},%{version}}
%{_libdir}/libflite_usenglish.so.{%{abi},%{version}}
%{_bindir}/flite
%{_bindir}/flite_cmu_time_awb
%{_bindir}/flite_cmu_us_{awb,kal,kal16,rms,slt}
%{_bindir}/flite_time


%files devel
%{_libdir}/libflite_cmu_{grapheme,indic}_{lang,lex}.so
%{_libdir}/libflite_cmulex.so
%{_libdir}/libflite_cmu_time_awb.so
%{_libdir}/libflite_cmu_us_{awb,kal,kal16,rms,slt}.so
%{_libdir}/libflite.so
%{_libdir}/libflite_usenglish.so
%{_includedir}/flite


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2-13
- Prepare for Oreon 11 (RP1)
