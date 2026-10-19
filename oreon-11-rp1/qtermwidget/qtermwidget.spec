%global source0_hash 4595bf4be80fbb197c97aae5d054e82067ca741ffe4351f376fb1df3adc9df8b
Name:		qtermwidget
Version:	2.4.0
Release:        1%{?dist}
License:	GPL-2.0-or-later
Summary:        Qt6 terminal widget
URL:		https://github.com/lxqt/%{name}/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if 0%{?el7}
%endif
Provides:       qtermwidget-qt5 = %{version}-%{release}
Obsoletes:      qtermwidget-qt5 < %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qtermwidget-devel -f %{oreon_filedir}/qtermwidget-devel.list
%files -n qtermwidget-l10n -f %{oreon_filedir}/qtermwidget-l10n.list

%changelog

%autochangelog
