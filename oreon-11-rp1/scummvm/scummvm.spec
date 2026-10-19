%global source0_hash f646fbd8767cceec8752b03361d84ace55835714a53fc3a8f2f6d991d312ac77
%{?filter_setup:
%filter_provides_in %{_libdir}/%{name}/.*\.so$
%filter_setup
}
%global git_url https://github.com/%{name}/%{name}
%global org_name org.scummvm.scummvm
Name:		scummvm
Version:	2.9.1
Release:        1%{?dist}
Summary:        Interpreter for several adventure games
License:	GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-OFL and LicenseRef-Callaway-MIT and ISC and Catharon AND Apache-2.0 AND BSL-1.0
URL:		https://www.scummvm.org/
Source0:        https://www.scummvm.org/frs/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0005:	scummvm-2.1.1-ftbfs-use-bfd-linker-on-x86.patch
%ifarch %{ix86}
%endif
Requires:	hicolor-icon-theme
Requires:	%{name}-data = %{version}-%{release}
Provides:	bundled(mt32emu) = 2.5.1
Provides:	bundled(lua)
Provides:	bundled(ags)
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flac-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvpx-devel
BuildRequires:  make
BuildRequires:  pipewire-jack-audio-connection-kit
BuildRequires:  readline-devel
BuildRequires:  sonivox-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_prep
%build

%define _lto_cflags %{nil}
%ifarch %{ix86}
export LDFLAGS="-fuse-ld=bfd"
%endif
export CONFIGURE_NO_HOST=true
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

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.xml
%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--set-key=Keywords --set-value="game;emulator;adventure;adventuregame;" \
	--set-key=StartupWMClass --set-value="scummvm" \
	--add-category=Emulator \
	dists/%{org_name}.desktop
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.so' | xargs chmod -Rc 0755
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n scummvm-data -f %{oreon_filedir}/scummvm-data.list

%changelog

%autochangelog
