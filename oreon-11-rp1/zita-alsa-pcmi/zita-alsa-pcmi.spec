%global source0_hash 8a297ace3d7a474131ed3fa321069c131337785b56a237d6f168c85ee796d56c

Summary:       ALSA C++ library
Name:          zita-alsa-pcmi
Version:       0.6.1
Release:       9%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later 
URL:           http://kokkinizita.linuxaudio.org
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: gcc-c++

%description
%{name} is the successor of clalsadrv. It provides easy access
to ALSA PCM devices, taking care of the many functions required to
open, initialize and use a hw: device in mmap mode, and providing
floating point audio data.

%package       devel
Summary:       Development libraries and headers for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      alsa-lib-devel

%description   devel
This package contains the headers and development libraries for %{name}.

%package       utils
Summary:       ALSA utilities using the %{name} library
Requires:      %{name}%{?_isa} = %{version}-%{release}
# The following are GPLv2+ licensed:
# /apps/alsa_delay.cc, /apps/alsa_loopback.cc, /apps/mtmd.cc /apps/mtdm.cc
License:       GPL-2.0-or-later AND GPL-3.0-or-later

%description   utils
This package contains the headers and development libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# No -march=native and ldconfig in Makefile and preserve timestamps
sed -i -e '/^CXXFLAGS += -march=native/d' -e '/ldconfig/d' -e 's/install -m/install -p -m/g' source/Makefile
sed -i -e 's/install -m/install -p -m/g' apps/Makefile

# Patch wrong bin destdir (sent upstream by email on 20190803)
sed -i -e 's/install -d $(BINDIR)/install -d $(DESTDIR)$(BINDIR)/' apps/Makefile

%build
%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} -C source

# Create symlink to build apps
ln -sf lib%{name}.so.%{version} source/lib%{name}.so

%make_build PREFIX=%{_prefix} CXXFLAGS="${CXXFLAGS} -I../source" LDFLAGS="${LDFLAGS} -L../source" -C apps

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} -C source
%make_install PREFIX=%{_prefix} -C apps

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files utils
%{_bindir}/alsa_delay
%{_bindir}/alsa_loopback

%changelog
%autochangelog
