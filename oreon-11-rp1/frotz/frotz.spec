%global source0_hash 92051a90c55fdcdf8c4336add2bf09b8329b468f3c0d2739dd850c00d1b9c8f1
%if 0%{?shortref:1}
%global buildref .%{gitdate}git%{shortref}
%endif
Name:           frotz
Version:        2.55
Release:        1%{?dist}
Summary:        Interactive fiction interpreter for Z-Machine (Infocom) games
License:        GPL-2.0-or-later
URL:            https://gitlab.com/DavidGriffith/frotz/
Source0:        https://gitlab.com/DavidGriffith/frotz/-/archive/%{version}/frotz-%{version}.tar.bz2
Patch0:         frotz-2.54-no_font_install.patch
# oreon:deps
BuildRequires:  bdftopcf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description

%package gui
Summary: SDL GUI for frotz interactive fiction interpreter
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui
%_description

This package contains the sfrotz GUI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build all
%install
%make_install PREFIX=%{_prefix} install_all
sed -Ee '/(^#|^$)/! s/^/#/' < doc/frotz.conf-big > frotz.conf
install -m0644 -D frotz.conf -t %{buildroot}%{_sysconfdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n frotz-gui -f %{oreon_filedir}/frotz-gui.list

%changelog

%autochangelog
