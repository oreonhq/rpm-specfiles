%global source0_hash none

Name:           mimic
Version:        1.3.0.1
Release:        16%{?dist}
Summary:        Mycroft's TTS engine

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://mimic.mycroft.ai/
Source0:        https://github.com/MycroftAI/mimic/archive/%{version}.tar.gz
Patch0:         mimic-fix-pulse.patch
# upstream fix for GCC 12
Patch1:         mimic-gcc12.patch

BuildRequires: make
BuildRequires:  automake autoconf libtool
BuildRequires:  alsa-lib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  pulseaudio-libs-devel

%description
Mimic is a fast, lightweight Text-to-speech engine developed by Mycroft A.I. 
and VocalID, based on Carnegie Mellon University’s FLITE software. Mimic takes 
in text and reads it out loud to create a high quality voice. Mimic's 
low-latency, small resource footprint, and good quality voices set it apart 
from other open source text-to-speech projects.

%package devel
Summary: Development files for Mimic
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Mimic, a small, fast speech synthesis engine.

%prep
%autosetup -p1 -n %{name}1-%{version}

%build
# This package triggers a fault in GCC when building with LTO enabled.
# Disable LTO until GCC is fixed
%define _lto_cflags %{nil}

autoreconf -vif
%configure --enable-shared --with-audio=alsa --with-audio=pulseaudio
%{make_build}

%install
%{make_install}

# Remove static libraries and libtool archives
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc ACKNOWLEDGEMENTS
%{_libdir}/libttsmimic*.so.*
%{_bindir}/mimic*
%{_bindir}/compile_regexes
%{_bindir}/t2p
%{_datadir}/man/man1/mimic.1*
%{_datadir}/%{name}

%files devel
%{_libdir}/libttsmimic*.so
%{_libdir}/pkgconfig/mimic.pc
%{_includedir}/ttsmimic

%changelog
%autochangelog
