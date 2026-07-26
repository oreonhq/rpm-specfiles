%global source0_hash none

# Filter provides of private plugins.
%if 0%{?fedora} || 0%{?rhel} >= 7
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
%else
%{?filter_setup:
%filter_provides_in %{_libdir}/%{name}/.*\.so$
%filter_setup
}
%endif

# Url to upstream GitHub repo.
%global git_url https://github.com/%{name}/%{name}

%global org_name org.scummvm.scummvm

Name:		scummvm
Version:	2.9.1
Release:	3%{?dist}
Summary:	Interpreter for several adventure games
# OFL only used by font files (distributed as fonts.dat)
License:	GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-OFL and LicenseRef-Callaway-MIT and ISC and Catharon AND Apache-2.0 AND BSL-1.0
URL:		https://www.scummvm.org/
Source0:	https://www.scummvm.org/frs/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0005:	scummvm-2.1.1-ftbfs-use-bfd-linker-on-x86.patch

BuildRequires:	make
BuildRequires:	libappstream-glib speech-dispatcher-devel alsa-lib-devel
BuildRequires:	SDL2-devel libvorbis-devel flac-devel zlib-devel
BuildRequires:	fluidsynth-devel desktop-file-utils libtheora-devel
BuildRequires:	libpng-devel freetype-devel libjpeg-devel libmad-devel
BuildRequires:	readline-devel libcurl-devel libmpeg2-devel gtk3-devel
BuildRequires:	gcc-c++ giflib-devel glew-devel
BuildRequires:	libmikmod-devel libvpx-devel sonivox-devel
BuildRequires:	pipewire-jack-audio-connection-kit

%ifarch %{ix86}
BuildRequires:	nasm
%endif
Requires:	hicolor-icon-theme
Requires:	%{name}-data = %{version}-%{release}

Provides:	bundled(mt32emu) = 2.5.1
# Lua is bundled twice: modified version 5.1 and 3.1
Provides:	bundled(lua)
Provides:	bundled(ags)

%description
ScummVM is a program which allows you to run certain classic graphical
point-and-click adventure games, provided you already have their
data files.

ScummVM supports many adventure games, including LucasArts SCUMM games
(such as Monkey Island 1-3, Day of the Tentacle, Sam & Max, ...),
many of Sierra's AGI and SCI games (such as King's Quest 1-6,
Space Quest 1-5, ...), Discworld 1 and 2, Simon the Sorcerer 1 and 2,
Beneath A Steel Sky, Lure of the Temptress, Broken Sword 1 and 2,
Flight of the Amazon Queen, Gobliiins 1-3, The Legend of Kyrandia 1-3,
many of Humongous Entertainment's children's SCUMM games (including
Freddi Fish and Putt Putt games) and many more.

The complete list can be found on ScummVM's compatibility page:
http://scummvm.org/compatibility/%{version}/

%package data
Summary:	Data files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description data
This package contains the data files for %{name}.

%prep
%autosetup -p 1

%build
# LTO combined with -Wl,--gdb-index and the Gold linker sometimes triggers
# occasional faults in the Gold linker.  We have already decided to deprecate
# the Gold linker so it does not seem worth the effort to reproduce, reduce,
# analyze # and report the heisenbug in Gold.
# Disable LTO
%define _lto_cflags %{nil}

# workaround FTBFS on i386
%ifarch %{ix86}
export LDFLAGS="-fuse-ld=bfd"
%endif

# The configure script shall ignore the parameter for the --host option
#passed by %%configure.
export CONFIGURE_NO_HOST=true

# The disables are so that these don't accidently get build in when rebuilding
# on a system with the necesarry deps installed.
%configure					\
	--datadir=%{_datadir}/%{name}		\
	--default-dynamic			\
	--enable-all-engines			\
	--enable-plugins			\
	--enable-release			\
	--enable-text-console			\
	--enable-translation			\
	--enable-verbose-build			\
	--enable-cloud				\
	--enable-libcurl			\
	--enable-mpeg2				\
	--with-freetype2-prefix=%{_prefix}
%make_build

%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.xml

%install
%make_install
# Remove doc files we want to include with %%doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--set-key=Keywords --set-value="game;emulator;adventure;adventuregame;" \
	--set-key=StartupWMClass --set-value="scummvm" \
	--add-category=Emulator \
	dists/%{org_name}.desktop

# Plugins should be executable.
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.so' | xargs chmod -Rc 0755

%files
%license COPYING LICENSES/COPYING.*
%doc AUTHORS README.md NEWS.md TODO doc/{cz,da,de,es,fr,it,no-nb,QuickStart,se}
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{org_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{org_name}.svg
%{_datadir}/pixmaps/%{org_name}.xpm
%{_metainfodir}/%{org_name}.metainfo.xml

%files data
%{_datadir}/%{name}/

%changelog
%autochangelog
