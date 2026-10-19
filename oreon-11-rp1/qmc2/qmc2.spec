%global source0_hash 0608a4e08bc451ae01856b85525f1dc767e01eb823e7e294c772876971e7609b
%global forgeurl https://github.com/qmc2/qmc2-mame-fe/
Version:        0.243
%forgemeta
Name:           qmc2
Release:        1%{?dist}
Summary:        M.A.M.E. Catalog / Launcher II
License:        GPL-2.0-only AND Apache-2.0 AND MIT AND BSD-3-Clause
URL:            http://qmc2.batcom-it.net
Source0:        %{forgeurl}archive/v%{version}/%{name}-mame-fe-%{version}.tar.gz
Patch1:         %{name}-ini.patch
Patch2:         0001-Fix-build-with-minizip-4.0.8.patch
Patch10:        0001-fix-MachineListDatabase-wasn-t-saved-to-qmc2.ini.patch
Patch11:        0001-new-added-a-Brasilian-Portuguese-translation-thanks-.patch
Patch12:        0001-imp-added-Ubuntu-22.04-build-configuration.patch
Patch13:        0001-imp-removed-ancient-build-configs.patch
Patch14:        0001-imp-Added-history.xml-support-and-use-XML-parser-to-.patch
Patch15:        0002-imp-Updated-Fedora-and-Ubuntu-build-configurations.-.patch
Patch16:        0007-imp-Updated-bundled-libraries-to-their-current-upstr.patch
Patch17:        0008-imp-Replaced-custom-XML-parsing-with-QXmlStreamReade.patch
Patch18:        0001-imp-Updated-SDL-to-2.30.3-LZMA-SDK-to-25.06-and-mini.patch
Requires:       games-menus
Provides:       bundled(lzma-sdk) = 24.06
Provides:       PDF.js = 3f320f0b
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libXmu-devel
BuildRequires:  libarchive-devel
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  rsync
# /oreon:deps
%description
A Qt based multi-platform GUI front-end for MAME.

%package -n qchdman
Summary:        Qt CHDMAN GUI
License:        GPL-2.0-only
Requires:       mame-tools
%description -n qchdman
A stand-alone graphical user interface / front-end to chdman

%package arcade
Summary:        Arcade QMC2 GUI
License:        GPL-2.0-only
%description arcade
A QML-based standalone graphical arcade mode binary which utilizes the cached
data of qmc2 to quickly display and launch emulators and get you "straight into
the games"

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1 -S git
#ensure system minizip and zlib are used
rm -rf src/minizip
rm -rf src/zlib
#fix opening documentation from the menu
sed -i s@doc/html/@doc/@ src/qmc2main.cpp

%build

%make_build DISTCFG=1 CC_FLAGS="$RPM_OPT_FLAGS" CXX_FLAGS="$RPM_OPT_FLAGS" \
    L_FLAGS="$RPM_LD_FLAGS" \
    SYSTEM_MINIZIP=1 \
    SYSTEM_ZLIB=1 LIBARCHIVE=1 GIT_REV=0
%make_build arcade DISTCFG=1 CC_FLAGS="$RPM_OPT_FLAGS" CXX_FLAGS="$RPM_OPT_FLAGS" \
    L_FLAGS="$RPM_LD_FLAGS"  \
    SYSTEM_MINIZIP=1 \
    SYSTEM_ZLIB=1 LIBARCHIVE=1 GIT_REV=0
%make_build qchdman DISTCFG=1 CXX_FLAGS="$RPM_OPT_FLAGS" L_FLAGS="$RPM_LD_FLAGS" \
    GIT_REV=0
%make_build doc DISTCFG=1
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make arcade-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make qchdman-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make doc-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 MAN_DIR=%{_mandir}
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -fr doc
ln -s %{_docdir}/%{name} doc
popd
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qmc2-sdlmame.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qmc2-arcade.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qchdman.desktop
%oreon_autofiles qchdman usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qchdman -f %{oreon_filedir}/qchdman.list
%files -n qmc2-arcade -f %{oreon_filedir}/qmc2-arcade.list

%changelog

%autochangelog
