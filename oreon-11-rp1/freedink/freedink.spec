%global source0_hash 5e0b35ac8f46d7bb87e656efd5f9c7c2ac1a6c519a908fc5b581e52657981002
Name:		freedink
Version:	109.6
Release:        1%{?dist}
Summary:        Humorous top-down adventure and role-playing game
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/freedink/
Source0:        https://ftp.gnu.org/gnu/freedink/freedink-%{version}.tar.gz
Patch0:         sdl-android.patch
Patch1:         gnulib.patch
Patch2:         const.patch
Patch3:         includes.patch
ExcludeArch:    s390x
Requires:	freedink-engine = %{version}-%{release} freedink-dfarc
Provides:	bundled(gnulib)
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_gfx-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  cxxtest
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humor, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

GNU FreeDink is a new and portable version of the game engine, which
runs the original game as well as its D-Mods, with close
compatibility, under multiple platforms.

This package is a meta-package to install the game, its data and a
front-end to manage game options and D-Mods.

%package engine
Summary:	Humorous top-down adventure and role-playing game (engine)
Requires:	freedink-data
%if 0%{?with_included_liberation_font}
%else
Requires: liberation-sans-fonts
%endif
%description engine
Dink Smallwood is an adventure/role-playing game, similar to classic
Zelda, made by RTsoft. Besides twisted humor, it includes the actual
game editor, allowing players to create hundreds of new adventures
called Dink Modules or D-Mods for short.

GNU FreeDink is a new and portable version of the game engine, which
runs the original game as well as its D-Mods, with close
compatibility, under multiple platforms.

This package contains the game engine alone.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build

export CXXFLAGS="$CXXFLAGS -std=gnu17"
%configure --disable-embedded-resources 
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %{name}
%find_lang %{name}-gnulib
cat %{name}-gnulib.lang >> %{name}.lang
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}edit.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%if 0%{?with_included_liberation_font}
%else
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/LiberationSans-Regular.ttf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n freedink-engine -f %{oreon_filedir}/freedink-engine.list

%changelog

%autochangelog
