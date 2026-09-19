%global source0_hash 0062ca9a0d000b937364567ff41e3bf15798807c839d1a981e7fe6aedfdb7378

Summary:       Horizontal or vertical bar-graph audio levels meter 
Name:          jkmeter
Version:       0.9.0
Release:       10%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
Source2:       %{name}.png

BuildRequires: desktop-file-utils
BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: alsa-lib-devel
BuildRequires: libpng-devel
BuildRequires: libsndfile-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: make

%description
%{name} is a horizontal or vertical bar-graph level
meter based on the ideas of mastering guru Bob Katz.
See <http://www.digido.com/bob-katz/index.php> and
follow the links on 'level practices'.

This is the type of meter you want for live recording,
mixing and mastering. It probably makes no sense to
use it on all tracks of a DAW, where keeping digital
level within limits is the main purpose of metering.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i -e 's/-ffast-math//' \
       -e '/^CXXFLAGS += -march=native/d' source/Makefile

%build
%set_build_flags
%make_build -C source PREFIX=%{_prefix}

%install
%make_install -C source PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
