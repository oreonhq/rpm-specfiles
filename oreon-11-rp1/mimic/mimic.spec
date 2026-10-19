%global source0_hash 9041f5c7d3720899c90c890ada179c92c3b542b90bb655c247e4a4835df79249
Name:           mimic
Version:        1.3.0.1
Release:        16%{?dist}
Summary:        Mycroft's TTS engine
License:        LicenseRef-Callaway-BSD
URL:            https://mimic.mycroft.ai/
Source0:        https://github.com/MycroftAI/mimic/archive/%{version}.tar.gz
Patch0:         mimic-fix-pulse.patch
Patch1:         mimic-gcc12.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
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
%global oreon_srcdir %{name}1-%{version}
%oreon_prep
%build

%define _lto_cflags %{nil}
autoreconf -vif
%configure --enable-shared --with-audio=alsa --with-audio=pulseaudio
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mimic-devel -f %{oreon_filedir}/mimic-devel.list

%changelog

%autochangelog
