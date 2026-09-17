%global source0_hash none

Name: goldendict
Version: 1.5.0
Release: 9%{?dist}

License: GPL-3.0-or-later
Summary: A feature-rich dictionary lookup program
URL: http://goldendict.org
Source0: https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)

BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lzo2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(xtst)

BuildRequires: eb-devel
BuildRequires: phonon-qt5-devel
BuildRequires: qtsingleapplication-qt5-devel

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make

Requires: qt5-qtsvg%{?_isa}

Recommends: %{name}-docs = %{?epoch:%{epoch}:}%{version}-%{release}

%description
GoldenDict is a feature-rich dictionary lookup program, supporting multiple
dictionary formats (StarDict/Babylon/Lingvo/Dictd/AARD/MDict/SDict) and
online dictionaries, featuring perfect article rendering with the complete
markup, illustrations and other content retained, and allowing you to type
in words without any accents or correct case.

%package docs
Summary: Documentation for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description docs
Contain doc files of %{name}.

%prep
%autosetup -p1
rm -rf {qtsingleapplication,maclibs,winlibs}
sed -e '/qtsingleapplication.pri/d' -i %{name}.pro

%build
%qmake_qt5 PREFIX=%{_prefix} CONFIG+=qtsingleapplication CONFIG+=no_ffmpeg_player %{name}.pro
echo "%{version}" > version.txt
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/app-install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/locale
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/*.metainfo.xml

%files docs
%{_datadir}/%{name}/help

%changelog
%autochangelog
