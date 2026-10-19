%global source0_hash d147231509c496c26e5b297ffc7273869f827d249ec368ac620e590f1f25cc7f
%global _vpath_srcdir src
Name:		yoshimi
Version:	2.3.6.5
Release:        1%{?dist}
Summary:        Rewrite of ZynAddSubFx aiming for better JACK support
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/%{name}
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-cflags.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  boost-devel
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fftw3-devel
BuildRequires:  fltk1.3-devel
BuildRequires:  fltk1.3-fluid
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lv2-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mxml-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description

Yoshimi is a rewrite of ZynAddSubFx to improve its compatibility with
the Jack Audio Connection Kit.

ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sound like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1

%build

export CFLAGS="%{optflags}"
%cmake -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -fPIC" -DFLTK_INCLUDE_DIR=%{_includedir}/Fl
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 644 desktop/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
chmod 755 %{buildroot}%{_datadir}/%{name}/banks
chmod 755 %{buildroot}%{_datadir}/%{name}/banks/*
chmod 755 %{buildroot}%{_datadir}/%{name}/presets
chmod 755 %{buildroot}%{_datadir}/%{name}/presets/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
