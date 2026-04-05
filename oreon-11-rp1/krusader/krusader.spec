Name:		krusader
Version:	2.9.0
Release:	5%{?dist}
Summary:	An advanced twin-panel (commander-style) file-manager for KDE

License:	GPL-2.0-or-later
URL:		https://www.krusader.org/
Source0:	https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	extra-cmake-modules
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:	libacl-devel
BuildRequires:	libappstream-glib
BuildRequires:	libattr-devel
BuildRequires:	ninja-build
BuildRequires:	qt6-qtbase-devel
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:	zlib-devel

%description
Krusader is an advanced twin panel (commander style) file manager for KDE and
other desktops in the *nix world, similar to Midnight or Total Commander.
It provides all the file management features you could possibly want.
Plus: extensive archive handling, mounted filesystem support, FTP, advanced
search module, an internal viewer/editor, directory synchronisation,
file content comparisons, powerful batch renaming and much much more.
It supports a wide variety of archive formats and can handle other KIO slaves
such as smb or fish. It is (almost) completely customizable, very user
friendly, fast and looks great on your desktop! You should give it a try.

%prep
%autosetup -p1

%build
%cmake_kf6 -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-kde

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog README README.md NEWS TODO
%license LICENSES/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/doc/HTML/*/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/kxmlgui5/%{name}/
%{_libdir}/qt6/plugins/kf6/kio/kio*.so
%{_mandir}/*/man1/%{name}.1*
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/*.appdata.xml
%{_sysconfdir}/xdg/kio_isorc

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.0-4
- Prepare for Oreon 11 (RP1)
