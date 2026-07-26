%global source0_hash 194b97c46fe39268864b98d0d2b510692daebb2a94e6b242515f5d98d3ab718f

Name:		qtermwidget
Version:	2.3.0
Release:	2%{?dist}
License:	GPL-2.0-or-later
Summary:	Qt6 terminal widget
URL:		https://github.com/lxqt/%{name}/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(lxqt)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  lxqt-build-tools
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

# Provide and Obsolete the old -qt5 name
Provides:       qtermwidget-qt5 = %{version}-%{release}
Obsoletes:      qtermwidget-qt5 < %{version}-%{release}

%description
QTermWidget is an open-source project originally based on KDE4 Konsole
application, but it took its own direction later.
The main goal of this project is to provide Unicode-enabled, embeddable
Qt widget for using as a built-in console (or terminal emulation widget)

%package	devel
Summary:	Qt6 terminal widget - devel package
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:       qtermwidget-qt5-devel = %{version}-%{release}
Obsoletes:	qtermwidget-qt5-devel < %{version}-%{release}

%description	devel
Development files for qtermwidget-qt6 library.

%package l10n
BuildArch:      noarch
Summary:        Translations for qtermwidget
Requires:       qtermwidget
%description l10n
This package provides translations for the qtermwidget package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
%cmake
%cmake_build

%if 0%{?el7}
EOF
%endif

%install
%cmake_install
%find_lang qtermwidget --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libdir}/lib%{name}6.so.2
%{_libdir}/lib%{name}6.so.%{version}
%{_datadir}/%{name}6

%files devel
%{_includedir}/%{name}6
%{_libdir}/lib%{name}6.so
%{_libdir}/pkgconfig/%{name}6.pc
%{_libdir}/cmake/%{name}6

%files l10n -f qtermwidget.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/qtermwidget6/translations

%changelog
%autochangelog
