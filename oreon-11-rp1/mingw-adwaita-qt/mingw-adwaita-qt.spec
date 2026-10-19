%global source0_hash cd5fd71c46271d70c08ad44562e57c34e787d6a8650071db115910999a335ba8
%global shortname adwaita-qt
%{?mingw_package_header}
Name:           mingw-adwaita-qt
Version:        1.4.2
Release:        1%{?dist}
Summary:        Adwaita theme for Qt-based applications
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Url:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}/adwaita-qt-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt6-qtbase
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt6-qtbase
# /oreon:deps
%description
Theme to let Qt applications fit nicely into Fedora Workstation

# Win32
%package -n mingw32-adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       mingw32-libadwaita-qt5 = %{version}-%{release}
%description -n mingw32-adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n mingw32-libadwaita-qt5
Summary:        Adwaita Qt5 library
%description -n mingw32-libadwaita-qt5
%{summary}.

%package -n mingw32-libadwaita-qt5-static
Summary:        Development files for mingw32-libadwaita-qt5
Requires:       mingw32-libadwaita-qt5 = %{version}-%{release}
%description -n mingw32-libadwaita-qt5-static
Static version of the mingw32-libadwaita-qt5 library.

# Win64
%package -n mingw64-adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       mingw64-libadwaita-qt5 = %{version}-%{release}
BuildArch:      noarch
%description -n mingw64-adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n mingw64-libadwaita-qt5
Summary:        Adwaita Qt5 library
%description -n mingw64-libadwaita-qt5
%{summary}.

%package -n mingw64-libadwaita-qt5-static
Summary:        Development files for mingw64-libadwaita-qt5
Requires:       mingw64-libadwaita-qt5 = %{version}-%{release}
%description -n mingw64-libadwaita-qt5-static
Static version of the mingw64-libadwaita-qt5 library.

# Win32
%package -n mingw32-adwaita-qt6
Summary:        Adwaita Qt6 theme
Requires:       mingw32-libadwaita-qt6 = %{version}-%{release}
%description -n mingw32-adwaita-qt6
Adwaita theme variant for applications utilizing Qt6.

%package -n mingw32-libadwaita-qt6
Summary:        Adwaita Qt6 library
%description -n mingw32-libadwaita-qt6
%{summary}.

%package -n mingw32-libadwaita-qt6-static
Summary:        Development files for mingw32-libadwaita-qt6
Requires:       mingw32-libadwaita-qt6 = %{version}-%{release}
%description -n mingw32-libadwaita-qt6-static
Static version of the mingw32-libadwaita-qt6 library.

# Win64
%package -n mingw64-adwaita-qt6
Summary:        Adwaita Qt6 theme
Requires:       mingw64-libadwaita-qt6 = %{version}-%{release}
BuildArch:      noarch
%description -n mingw64-adwaita-qt6
Adwaita theme variant for applications utilizing Qt6.

%package -n mingw64-libadwaita-qt6
Summary:        Adwaita Qt6 library
%description -n mingw64-libadwaita-qt6
%{summary}.

%package -n mingw64-libadwaita-qt6-static
Summary:        Development files for mingw64-libadwaita-qt6
Requires:       mingw64-libadwaita-qt6 = %{version}-%{release}
%description -n mingw64-libadwaita-qt6-static
Static version of the mingw64-libadwaita-qt6 library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir adwaita-qt-%{version}
%oreon_prep
%build

mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%mingw_cmake ../..
%mingw_make_build
popd
mkdir %{_target_platform}-qt6
pushd %{_target_platform}-qt6
%mingw_cmake -DUSE_QT6=ON ../..
%mingw_make_build
popd
%install
pushd %{_target_platform}-qt5
%mingw_make_install
popd
pushd %{_target_platform}-qt6
%mingw_make_install
popd
%oreon_autofiles mingw32-adwaita-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libadwaita-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libadwaita-qt5-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-adwaita-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libadwaita-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libadwaita-qt5-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-adwaita-qt6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libadwaita-qt6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libadwaita-qt6-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-adwaita-qt6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libadwaita-qt6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libadwaita-qt6-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-adwaita-qt5 -f %{oreon_filedir}/mingw32-adwaita-qt5.list
%files -n mingw32-libadwaita-qt5 -f %{oreon_filedir}/mingw32-libadwaita-qt5.list
%files -n mingw32-libadwaita-qt5-static -f %{oreon_filedir}/mingw32-libadwaita-qt5-static.list
%files -n mingw64-adwaita-qt5 -f %{oreon_filedir}/mingw64-adwaita-qt5.list
%files -n mingw64-libadwaita-qt5 -f %{oreon_filedir}/mingw64-libadwaita-qt5.list
%files -n mingw64-libadwaita-qt5-static -f %{oreon_filedir}/mingw64-libadwaita-qt5-static.list
%files -n mingw32-adwaita-qt6 -f %{oreon_filedir}/mingw32-adwaita-qt6.list
%files -n mingw32-libadwaita-qt6 -f %{oreon_filedir}/mingw32-libadwaita-qt6.list
%files -n mingw32-libadwaita-qt6-static -f %{oreon_filedir}/mingw32-libadwaita-qt6-static.list
%files -n mingw64-adwaita-qt6 -f %{oreon_filedir}/mingw64-adwaita-qt6.list
%files -n mingw64-libadwaita-qt6 -f %{oreon_filedir}/mingw64-libadwaita-qt6.list
%files -n mingw64-libadwaita-qt6-static -f %{oreon_filedir}/mingw64-libadwaita-qt6-static.list

%changelog

%autochangelog
