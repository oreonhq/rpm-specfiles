%global source0_hash 51c01a1bb48de2bc98c025afd4eeade0059376785337725da7ee323a79e862f0
%bcond_with	debug
%if %{with debug}
%global		config			debug
%global		dbg			_dbg
%else
%global		config			release
%global		dbg			%{nil}
%endif
%bcond_without	system_mozjs128
%bcond_without	system_nvtt
%bcond_without	nvtt
%global __provides_exclude_from ^%{_libdir}/0ad/
%global __requires_exclude ^(libAtlasUI.*\.so|libCollada.*\.so|libmozjs78.*\.so)
Name:		0ad
Version:	0.28.0
Release:        2%{?dist}
License:	GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND IPL-1.0 AND MPL-2.0
Summary:        Cross-Platform RTS Game of Ancient Warfare
Url:		http://play0ad.com
%if ! %{with nvtt}
Source0:        %{name}-%{version}-alpha-unix-build.tar.xz
%else
Source0:        %{name}-%{version}-alpha-unix-build.tar.xz
%endif
Source1:	%{name}-licensecheck.txt
Source2:	%{name}.6
Source5:        premake-core-5.0.0-beta7.tar.gz
Requires:	%{name}-data = %{version}
Requires:	hicolor-icon-theme
%if %{with system_nvtt}
%endif
%if %{without system_mozjs128}
%else
%endif
ExclusiveArch:	%{ix86} x86_64 %{arm} aarch64 ppc64le
%if %{without system_mozjs128}
Provides: bundled(mozjs) = 128
%endif
Patch1:		%{name}-debug.patch
Patch2:		%{name}-check.patch
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  SDL2-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cxxtest
BuildRequires:  desktop-file-utils
BuildRequires:  enet-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gloox-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdnet-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libsodium-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  miniupnpc-devel
BuildRequires:  nvidia-texture-tools-devel
BuildRequires:  openal-soft-devel
BuildRequires:  perl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(mozjs-128)
BuildRequires:  python3.11-devel
BuildRequires:  subversion
BuildRequires:  valgrind-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer,
hobbyist game developers, since 2001.

#-----------------------------------------------------------------------
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%if ! %{with debug}
# disable debug build, and "int 0x3" to trap to debugger (x86 only)
#%%patch -P1 -p0
%endif
#%%patch -P2 -p0

cp %{SOURCE5} libraries/source/premake-core/

%if %{with system_nvtt}
rm -fr libraries/source/nvtt
%endif

rm -fr libraries/source/valgrind

#-----------------------------------------------------------------------
%build

%define _lto_cflags %{nil}
%set_build_flags
unset RUSTFLAGS
./libraries/source/premake-core/build.sh
./libraries/source/cxxtest-4.4/build.sh
./libraries/source/fcollada/build.sh
build/workspaces/update-workspaces.sh	\
    --bindir=%{_bindir}			\
    --datadir=%{_datadir}/%{name}	\
    --libdir=%{_libdir}/%{name}		\
%if %{with system_mozjs128}
    --with-system-mozjs			\
%endif
%if %{with system_nvtt}
    --with-system-nvtt			\
%endif
%if ! %{with nvtt}
    --without-nvtt			\
%endif
    %{?_smp_mflags}
make %{?_smp_mflags} -C build/workspaces/gcc config=%{config} verbose=1
%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 build/resources/0ad.sh %{buildroot}%{_bindir}/0ad
install -p -m 755 binaries/system/pyrogenesis%{dbg} %{buildroot}%{_bindir}/pyrogenesis%{dbg}
install -d -m 755 %{buildroot}%{_libdir}/%{name}
for name in AtlasUI%{dbg} Collada%{dbg}; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done
%if %{with nvtt} && ! %{with system_nvtt}
for name in nvcore nvimage nvmath nvtt; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done
%endif
%if %{without system_mozjs128}
%if %{with debug}
name=mozjs128-ps-debug
%else
name=mozjs128-ps-release
%endif
install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
%endif
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 build/resources/0ad.appdata.xml %{buildroot}%{_datadir}/metainfo/0ad.appdata.xml
install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 build/resources/0ad.desktop %{buildroot}%{_datadir}/applications/0ad.desktop
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 build/resources/0ad.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/0ad.png
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -a binaries/data/* %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man6/%{name}.6
ln -sf %{name}.6 %{buildroot}%{_mandir}/man6/pyrogenesis.6
%if %{with debug}
export STRIP=/bin/true
%oreon_autofiles main
%endif
%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/0ad.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/0ad.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
