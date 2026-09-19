%global source0_hash 00c0ce7efdbfdb8db338fe78802ee8997199f305c61c37a5f58aa5986cb2940d

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kbackup
Version:        25.12.3
Release:        1%{?dist}
Summary:        Back up your data in a simple, user friendly way
Summary(fr):    Sauvegarder vos données de manière simple et conviviale
Summary(ru):    Простое, дружественное к пользователю резервное копирование

License:        GPL-2.0-or-later
Url:            https://github.com/KDE/kbackup
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel

BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Widgets)

Requires:       hicolor-icon-theme

%description
KBackup is a program that lets you back up any directories or files,
whereby it uses an easy to use directory tree to select the things to back up.
The program was designed to be very simple in its use
so that it can be used by non-computer experts.
The storage format is the well known TAR format, whereby the data
is still stored in compressed format (bzip2 or gzip).

%description -l fr
KBackup est un programme qui vous permet de sauvegarder n'importe quels
fichiers ou répertoires que vous pouvez sélectionner dans une arborescence.
Il a été conçu pour être facile d'utilisation et est donc à la portée des
non-initiés à l'informatique.
Le format de stockage est le très connu format TAR, où les données sont
stockées compressées (bzip2 ou gzip).

%description -l ru
KBackup позволяет делать резервное копирование любых каталогов и файлов,
используя простое представление в виде дерева каталогов для выбора элементов
копирования.
Программа спроектирована очень простой в использовании даже не экспертами в
области компьютеров.
Формат хранения архивов - хорошо известный TAR, форматы сжатия bzip2 или gzip.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html --with-man --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_metainfodir}/org.kde.%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
