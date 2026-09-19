%global source0_hash 5e0b35ac8f46d7bb87e656efd5f9c7c2ac1a6c519a908fc5b581e52657981002

Name:		freedink
Version:	109.6
Release:	19%{?dist}
Summary:	Humorous top-down adventure and role-playing game

BuildRequires:	gcc-c++
BuildRequires:	SDL2-devel SDL2_gfx-devel SDL2_ttf-devel SDL2_image-devel SDL2_mixer-devel
BuildRequires:	fontconfig-devel
BuildRequires:	glm-devel
BuildRequires:	cxxtest
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_desktop_files
BuildRequires:	desktop-file-utils
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/
BuildRequires:	libappstream-glib
BuildRequires: make
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/freedink/
Source0:	https://ftp.gnu.org/gnu/freedink/freedink-%{version}.tar.gz
Patch0:         sdl-android.patch
Patch1:         gnulib.patch
Patch2:         const.patch
Patch3:         includes.patch
ExcludeArch:    s390x

Requires:	freedink-engine = %{version}-%{release} freedink-dfarc
# Reference bundled copy of gnulib - cf. https://fedorahosted.org/fpc/ticket/174
Provides:	bundled(gnulib)

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
# No dependency
%else
# Respect Fedora guidelines (see below)
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
# Using '--disable-embedded-resources' because 'rpmbuild' will remove
# them anyway (so it can make the -debuginfo package -- too bad :/)
%configure --disable-embedded-resources 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %{name}
%find_lang %{name}-gnulib
# %%files only support one '-f' argument (see below)
cat %{name}-gnulib.lang >> %{name}.lang
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}edit.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
# http://fedoraproject.org/wiki/Packaging/Guidelines#Avoid_bundling_of_fonts_in_other_packages
# Policy insists on not installing a different version of "Liberation
# Sans". Beware that the system version may be different than the
# official FreeDink font, because Liberation changes regularly.
%if 0%{?with_included_liberation_font}
# Include it nonetheless for the sake of avoiding
# liberation-fonts<->liberation-sans-fonts distro naming conflicts in
# the freedink.org RPM repository
%else
# Remove it for compliance with Fedora guidelines
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/LiberationSans-Regular.ttf
%endif

%files

%files engine -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README THANKS TROUBLESHOOTING ChangeLog
%{_bindir}/*
%{_datadir}/applications/*
%{_metainfodir}/*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_mandir}/man6/*

%changelog
%autochangelog
