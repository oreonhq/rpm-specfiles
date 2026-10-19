%global source0_hash 31d0e35a4ca567ec9b5ebda6c3062bb4435d6d3eacd6ef0d95cadd7854dc03ee
%global out out123
%global fmt fmt123
%global syn syn123
Name: mpg123
Version: 1.33.7
Release:        1%{?dist}
Summary:        Real time MPEG 1.0/2.0/2.5 audio player/decoder for layers 1, 2 and 3
License: GPL-2.0-or-later
URL: https://mpg123.org
Source0:        https://mpg123.org/download/mpg123-1.33.7.tar.bz2
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%global _summary %{summary}
# oreon:deps
BuildRequires:  /usr/bin/doxygen
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)
# /oreon:deps
%description

%package plugins-pulseaudio
Summary: Pulseaudio output plug-in for %{name}
BuildRequires: pkgconfig(libpulse-simple)
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (mpg123%{?_isa} and pulseaudio%{?_isa})
%description plugins-pulseaudio

Pulseaudio output plug-in.

%if 0%{?enable_jack}
%package plugins-jack
Summary: JACK output plug-in for %{name}
BuildRequires: pkgconfig(jack)
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (mpg123%{?_isa} and jack-audio-connection-kit%{?_isa})
Obsoletes: %{name}-plugins-extras < 1.23.4-1
%description plugins-jack

JACK output plug-in.
%endif

%if 0%{?enable_portaudio}
%package plugins-portaudio
Summary: PortAudio output plug-in for %{name}
BuildRequires: pkgconfig(portaudio-2.0)
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (mpg123%{?_isa} and portaudio%{?_isa})
%description plugins-portaudio

PortAudio output plug-in.
%endif

%package libs
Summary: %{_summary}
Provides: lib%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: lib%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: lib%{name} < 1.23.4-1
%description libs

%package devel
Summary: %{_summary}
BuildRequires: /usr/bin/doxygen
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: lib%{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: lib%{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: lib%{name}-devel < 1.23.4-1
Obsoletes: %{name}-libs-devel < 1.23.8-3
%description devel

Development files for decoding and output libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vfi
%configure --enable-modules=yes --with-default-audio=alsa \
  --with-audio=alsa,%{?enable_jack:jack},pulse,oss,%{?enable_portaudio:portaudio}
%make_build
pushd doc
  doxygen doxygen.conf
popd
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mpg123-plugins-pulseaudio -f %{oreon_filedir}/mpg123-plugins-pulseaudio.list
%files -n mpg123-libs -f %{oreon_filedir}/mpg123-libs.list
%files -n mpg123-devel -f %{oreon_filedir}/mpg123-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.32.10-1
- Prepare for Oreon 11 (RP1)
