%global source0_hash b3c887e2ab381f9183a8a1e42b6300ac2ea1766496ae5d91f3257bb7e6786649

Name:          meterbridge
Summary:       Meter Bridge for JACK
Version:       0.9.2
Release:       38%{?dist}
URL:           http://plugin.org.uk/meterbridge/
Source0:       http://plugin.org.uk/%{name}/%{name}-%{version}.tar.gz
# Patch sent upstream via email (there is no bugtracker)
Patch0:        meterbridge-gcc10.patch
License:       GPL-1.0-or-later

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: SDL_image-devel

%description
%{name} is a software meter bridge for the UNIX based JACK audio system.
It supports a number of different types of meter, rendered using the SDL
library and user-editable pixmaps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc10

%build
# FIXME: The Makefile.ams don't honor CFLAGS correctly
# Resort to overriding CPPFLAGS.
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CPPFLAGS
# Proper fix would be to fix the source-code
export CPPFLAGS="%{optflags} -std=gnu89"
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
%autochangelog
