%global source0_hash 235a8606aa1e654aa5a5a41b5c7b5ae1e934aab30fb2e2b18e2e35a4eafcd745

#%%global gitref d9676545fc072222d3b50742ee881f8c3570a62e
#%%global gitdate 20250127
#%%global shortref %%(echo %%{gitref} |cut -c1-8)

%if 0%{?shortref:1}
%global buildref .%{gitdate}git%{shortref}
%endif

Name:           frotz
Version:        2.55
Release:        3%{?buildref}%{?dist}
Summary:        Interactive fiction interpreter for Z-Machine (Infocom) games

License:        GPL-2.0-or-later
URL:            https://gitlab.com/DavidGriffith/frotz/
Source0:        https://gitlab.com/DavidGriffith/frotz/-/archive/%{version}/frotz-%{version}.tar.bz2

# Installing the X11 font would seem to be prohibited by the Fonts Policy
# https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/
Patch0:         frotz-2.54-no_font_install.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisfile)

# For sfrotz
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(zlib)

# For xfrotz
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  bdftopcf

BuildRequires: make

%global _description\
Frotz is an interpreter for Infocom games and other Z-machine games.  It\
complies with standard 1.0 of Graham Nelson's specification.\
\
Free Z-machine game file downloads, as well as more information about\
Infocom, Z-machine games, and interactive fiction can be found at the\
Interactive Fiction Archive, http://mirror.ifarchive.org/.

%description %_description

%package gui
Summary: SDL GUI for frotz interactive fiction interpreter
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gui
%_description

This package contains the sfrotz GUI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build all

%install
%make_install PREFIX=%{_prefix} install_all

# Make a version of the config file with all settings commented out,
# to install in /etc
sed -Ee '/(^#|^$)/! s/^/#/' < doc/frotz.conf-big > frotz.conf
install -m0644 -D frotz.conf -t %{buildroot}%{_sysconfdir}

%files
%doc AUTHORS ChangeLog DUMB HOW_TO_PLAY README
%license COPYING
%doc doc/frotz.conf*
%{_bindir}/frotz
%{_bindir}/dfrotz
%{_mandir}/man6/frotz.6*
%{_mandir}/man6/dfrotz.6*
%config(noreplace) %{_sysconfdir}/frotz.conf

%files gui
%{_bindir}/sfrotz
%{_bindir}/xfrotz
%{_mandir}/man6/sfrotz.6*
%{_mandir}/man6/xfrotz.6*

%changelog
%autochangelog
