%global source0_hash b3c887e2ab381f9183a8a1e42b6300ac2ea1766496ae5d91f3257bb7e6786649
Name:          meterbridge
Summary:        Meter Bridge for JACK
Version:       0.9.2
Release:        38%{?dist}
URL:           http://plugin.org.uk/meterbridge/
Source0:        http://plugin.org.uk/%{name}/%{name}-%{version}.tar.gz
Patch0:        meterbridge-gcc10.patch
License:       GPL-1.0-or-later
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  make
# /oreon:deps
%description
%{name} is a software meter bridge for the UNIX based JACK audio system.
It supports a number of different types of meter, rendered using the SDL
library and user-editable pixmaps.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc10

%build

export CPPFLAGS="%{optflags} -std=gnu89"
autoreconf -fi
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
