%global source0_hash 4069aaa3aa27b5862c51091009f4692ade8bdbcbe6b289a8b7eac65548f97c66

%global _vpath_srcdir src

Name:		yoshimi
Version:	2.3.0
Release:	9%{?dist}
Summary:	Rewrite of ZynAddSubFx aiming for better JACK support

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/%{name}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-cflags.patch

BuildRequires:  gcc-c++
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	cmake 
BuildRequires:	zlib-devel 
BuildRequires:	fontconfig-devel
BuildRequires:	fltk1.3-devel 
BuildRequires:	fltk1.3-fluid 
BuildRequires:	fftw3-devel
BuildRequires:	mxml-devel 
BuildRequires:	alsa-lib-devel 
BuildRequires:	libsndfile-devel
BuildRequires:	desktop-file-utils 
BuildRequires:	boost-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	cairo-devel
BuildRequires:  lv2-devel
BuildRequires:  readline-devel

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

# Fix directory permissions without affecting patch files
chmod 755 %{buildroot}%{_datadir}/%{name}/banks
chmod 755 %{buildroot}%{_datadir}/%{name}/banks/*
chmod 755 %{buildroot}%{_datadir}/%{name}/presets
chmod 755 %{buildroot}%{_datadir}/%{name}/presets/*

#rm %{buildroot}%{_datadir}/doc/%{name}/yoshimi-user-manual-2.0.pdf

%files
%doc Changelog COPYING README.txt doc/* 
%{_bindir}/%{name}
%{_datadir}/%{name}/banks/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/presets/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}_alt.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{name}/examples/
%{_libdir}/lv2/%{name}.lv2/
%{_mandir}/man1/yoshimi.1*

%changelog
%autochangelog
