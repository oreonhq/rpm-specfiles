%global source0_hash 02cca45e655727360990db8a9e3935be54cc4fbb01b339d1cd406d280ecdf3ae
%global srcname     lumina
Summary:        A lightweight, portable desktop environment
Name:               %{srcname}-desktop
Version:            1.6.2
Release:        1%{?dist}
License:            LicenseRef-Callaway-BSD
URL:                http://%{name}.org
Source0:        https://github.com/%{name}/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Requires:           firstboot(windowmanager)
Requires:           %{name}-filesystem = %{version}-%{release}
Requires:           %{name}-data = %{version}-%{release}
Requires:           %{srcname}-open%{?_isa} = %{version}-%{release}
Requires:           %{srcname}-info%{?_isa} = %{version}-%{release}
Requires:           %{srcname}-themeengine%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libxcb-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
# /oreon:deps
%description
The Lumina Desktop Environment is a lightweight system interface
that is designed for use on any Unix-like operating system.

%package            filesystem
Summary:            Common folders for Lumina Desktop
BuildArch:          noarch
Obsoletes:          %{name}-libs < 1.2.0
%description        filesystem
This package provides the common folders for the Lumina Desktop Environment.

%package            data
Summary:            Data for Lumina Desktop
BuildArch:          noarch
Requires:           %{name}-filesystem = %{version}-%{release}
%description        data
This package provides the data files for the Lumina Desktop
Environment: Colors, desktop background, theme templates.

%package -n         %{srcname}-open
Summary:            xdg-open style utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-open
This package provides %{srcname}-open, which handles opening of
files and URLs according to the system-wide mimetype association.
It also provides an optional selector if more than one application
is assigned with the given url or file type.

%package -n         %{srcname}-info
Summary:            Basic information utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-info
This package provides %{srcname}-info, which is a simple
utility that displays various information about the Lumina
installation, like paths, contributors, license or version.

%package -n         %{srcname}-themeengine
License:            MIT
Summary:            Theme engine for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-themeengine
This package provides %{srcname}-theme-engine.

%package -n         %{srcname}-config
Summary:            Configuration utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-config
This package provides %{srcname}-config, which allows changing
various aspects of %{srcname} and fluxbox, like the wallpaper being
used, theme, icons, panel (and plugins), startup and default
applications, desktop menu and more.

%package -n         %{srcname}-xconfig
Summary:            X server display configuration tool for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-xconfig
This package provides %{srcname}-xconfig, which is a simple
multi-head aware display configuration tool for configuring
the X server.

%package -n         %{srcname}-search
Summary:            Search utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-search
This package provides %{srcname}-search, which is a simple
search utility that allows to search for applications or
files and directories in the home directory and launch
or open them.

%package -n         %{srcname}-archiver
Summary:            Archiver for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-archiver
Front-end to tar, used for managing/creating archives.

%package -n         %{srcname}-fileinfo
Summary:            Desktop file editor for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-fileinfo
File properties viewer, and simple XDG application registration creator.

%package -n         %{srcname}-fm
Summary:            File manager for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-fm
This package provides %{srcname}-fm, which is a simple file manager
with support for multiple view modes, tabbed browsing,
including an integrated slideshow-based picture viewer.

%package -n         %{srcname}-mediaplayer
Summary:            Mediaplayer for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-mediaplayer
Simple media player with hooks for streaming from online radio services.

%package -n         %{srcname}-photo
Summary:            Image viewer for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-photo
Simple image viewer.

%package -n         %{srcname}-screenshot
Summary:            Screenshot utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-screenshot
This package provides %{srcname}-screenshot, which is a simple
screenshot utility that allows to snapshot the whole desktop
or a single window after a configurable delay.

Optionally the window border can be hidden when taking a
screenshot of a single window.

%package -n         %{srcname}-textedit
Summary:            Text file editor for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}
%description -n     %{srcname}-textedit
Plaintext editor with syntax highlighting, tab support, and find/replace functionality.

%package -n         material-design-dark
License:            Apache-2.0
Summary:            Material Design icon theme (dark)
BuildArch:          noarch
%description -n     material-design-dark
Optional icons theme recommended for Lumina Desktop (dark version).

%package -n         material-design-light
License:            Apache-2.0
Summary:            Material Design icon theme (light)
BuildArch:          noarch
%description -n     material-design-light
Optional icons theme recommended for Lumina Desktop (light version).

%package -n         %{srcname}-icons
License:            LicenseRef-Callaway-CC-BY
Summary:            Icon set for Lumina Desktop
BuildArch:          noarch
%description -n     %{srcname}-icons
Optional icons theme recommended for Lumina Desktop (new).

########################################################################################
%prep

%autosetup -n%{srcname}-%{version} -p 0
desktop-file-edit --remove-key=Categories --remove-only-show-in=Lumina --add-only-show-in=X-Lumina \
 src-qt5/core/%{srcname}-info/%{srcname}-support.desktop
for i in `grep -lir 'OnlyShowIn=Lumina' src-qt5`
do
 desktop-file-edit --remove-only-show-in=Lumina --add-only-show-in=X-Lumina $i
done

%build

%qmake_qt5 *.pro \
 CONFIG+=configure \
 LIBPREFIX="%{_libdir}" \
 L_BINDIR="%{_bindir}" \
 L_LIBDIR=%{_libdir} \
 L_SHAREDIR=%{_datadir} \
 L_ETCDIR=%{_sysconfdir} \
 L_INCLUDEDIR=%{_includedir} \
 L_MANDIR=%{_mandir} \
 QT5LIBDIR="%{_qt5_prefix}" \
 QMAKE_LFLAGS+="-Wl,--as-needed"
for i in `find . -type d -name i18n`; do lrelease-qt5 -silent -nounfinished $i/*.ts; done
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
install -d %{buildroot}%{_datadir}/%{name}/i18n
for i in `find . -type d -name i18n`
do
 install -m0644 -D $i/*.qm -t %{buildroot}%{_datadir}/%{name}/i18n/
done
%find_lang %{name} --with-qt
%find_lang %{srcname}-info --with-qt
%find_lang %{srcname}-open --with-qt
%find_lang %{srcname}-config --with-qt
%find_lang %{srcname}-search --with-qt
%find_lang %{srcname}-xconfig --with-qt
%find_lang l-archiver --with-qt
%find_lang l-fileinfo --with-qt
%find_lang %{srcname}-fm --with-qt
%find_lang l-mediap --with-qt
%find_lang l-photo --with-qt
%find_lang l-screenshot --with-qt
%find_lang l-te --with-qt
%oreon_autofiles material-design-dark usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles material-design-light usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{srcname}-*.desktop
%files -f %{oreon_filedir}/main.list
%files -n lumina-desktop-filesystem -f %{oreon_filedir}/lumina-desktop-filesystem.list
%files -n lumina-desktop-data -f %{oreon_filedir}/lumina-desktop-data.list
%files -n lumina-open -f %{oreon_filedir}/lumina-open.list
%files -n lumina-info -f %{oreon_filedir}/lumina-info.list
%files -n lumina-themeengine -f %{oreon_filedir}/lumina-themeengine.list
%files -n lumina-config -f %{oreon_filedir}/lumina-config.list
%files -n lumina-xconfig -f %{oreon_filedir}/lumina-xconfig.list
%files -n lumina-search -f %{oreon_filedir}/lumina-search.list
%files -n lumina-archiver -f %{oreon_filedir}/lumina-archiver.list
%files -n lumina-fileinfo -f %{oreon_filedir}/lumina-fileinfo.list
%files -n lumina-fm -f %{oreon_filedir}/lumina-fm.list
%files -n lumina-mediaplayer -f %{oreon_filedir}/lumina-mediaplayer.list
%files -n lumina-photo -f %{oreon_filedir}/lumina-photo.list
%files -n lumina-screenshot -f %{oreon_filedir}/lumina-screenshot.list
%files -n lumina-textedit -f %{oreon_filedir}/lumina-textedit.list
%files -n material-design-dark -f %{oreon_filedir}/material-design-dark.list
%files -n material-design-light -f %{oreon_filedir}/material-design-light.list
%files -n lumina-icons -f %{oreon_filedir}/lumina-icons.list

%changelog

%autochangelog
