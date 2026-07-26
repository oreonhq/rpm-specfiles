%global source0_hash 30ab4cc0f36aedd3f454cec2468d7b8a5820f12de1dd9e69d2e65d7299716d09

Name:           pcmanfm-qt
Version:        2.3.0
Release:        2%{?dist}
Summary:        LXQt file manager PCManFM

License:        GPL-2.0-or-later
URL:            https://lxqt-project.org
Source0:        https://github.com/lxde/pcmanfm-qt/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-backgrounds-compat
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm)
BuildRequires:  pkgconfig(libfm-qt6)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(lxqt) >= 1.0.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  lxqt-menu-data
Requires:       lxqt-sudo

# for /usr/share/backgrounds/default.{jxl,png}
Requires:       desktop-backgrounds-compat
# for jxl support
Requires:       kf6-kimageformats%{?_isa}
Obsoletes:      pcmanfm-qt5 < 0.9.0
Provides:       pcmanfm-qt5 = %{version}-%{release}
Obsoletes:      pcmanfm-qt4 <= 0.9.0
Obsoletes:      pcmanfm-qt-common <= 0.9.0

# gvfs is optional depencency at runtime, so we add a weak dependency here
Recommends:     gvfs
# configuration patched to use qterminal instead as the default terminal emulator but allow to use others
Requires:       qterminal

%description
PCManFM-Qt is a Qt-based file manager which uses GLib for file management. It
was started as the Qt port of PCManFM, the file manager of LXDE.

PCManFM-Qt is used by LXQt for handling the desktop. Nevertheless, it can also
be used independently of LXQt and under any desktop environment.

%package        l10n
Summary:        Translations for pcmanfm-qt
BuildArch:      noarch
Requires:       pcmanfm-qt = %{?epoch:%{epoch}:}%{version}-%{release}

%description    l10n
This package provides translations for the pcmanfm-qt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Set the wallpaper properly
bg_file_ext="jxl"
if [ -f "%{_datadir}/backgrounds/default.png" ]; then
bg_file_ext="png"
fi
sed -e "s|Wallpaper=.*$|Wallpaper=%{_datadir}/backgrounds/default.${bg_file_ext}|" -i config/pcmanfm-qt/lxqt/settings.conf.in

%build
%cmake
%cmake_build

%install
%cmake_install
for dfile in pcmanfm-qt-desktop-pref pcmanfm-qt; do
    desktop-file-edit \
        --remove-category=LXQt --add-category=X-LXQt \
        --remove-category=Help --add-category=X-Help \
        --remove-only-show-in=LXQt \
        %{buildroot}/%{_datadir}/applications/${dfile}.desktop
done

%find_lang %{name} --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-desktop-pref.desktop
%{_mandir}/man1/%{name}.*
%{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/pcmanfm-qt.svg

%files l10n -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/%{name}/translations

%changelog
%autochangelog
