%global source0_hash 583d308622a6c3ceafd6fbe614c31c979512c0a0666fa81929e1d9eb5a69fd7c

Name:		vlfrx-tools
Version:	0.9m
Release:	12%{?dist}
Summary:	VLF Receiver Software Toolkit
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.abelian.org/vlfrx-tools/
Source0:	http://www.abelian.org/%{name}/%{name}-%{version}.tgz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	alsa-lib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	libX11-devel
BuildRequires:	libpng-devel
BuildRequires:	libXpm-devel
BuildRequires:	ncurses-devel
BuildRequires:	xforms-devel
BuildRequires:	libshout-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	fftw-devel
Requires:	sox
Requires:	gnuplot

%description
Designed for VLF radio signal processing, it also has applications for meteor
forward scatter, seismographic and natural radioactivity recording, ELF and
magnetometers, radio astronomy, bat detection, amateur radio, and other
projects which require precision timestamps preserved through signal capture,
storage, and post-processing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install bindir=%{buildroot}%{_bindir}

%files
%{_bindir}/vt*
%doc README changelog

%changelog
%autochangelog
