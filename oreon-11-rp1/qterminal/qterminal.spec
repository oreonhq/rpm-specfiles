%global source0_hash aeb6cf5ff7f31f0b89e60f6cc1c83c4d6fbed57717196d2ebba2bc0dcb8436d4
Name:		qterminal
Version:	2.4.0
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		https://github.com/qterminal/qterminal
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary:        Advanced Qt6-based terminal emulator
%if 0%{?el7}
%endif
Requires:       qtermwidget >= 2.2.0
Provides:       %{name}-common = %{version}-%{release}
Provides:       %{name}-qt5 = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-qt5 < %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libcanberra-devel
BuildRequires:  lxqt-build-tools
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(qtermwidget6)
# /oreon:deps
%description
Advanced Qt6-based terminal emulator with many useful bells and whistles.

%package l10n
BuildArch:      noarch
Summary:        Translations for qterminal
Requires:       qterminal
%description l10n
This package provides translations for the qterminal package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

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
%find_lang qterminal --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-drop.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n qterminal-l10n -f %{oreon_filedir}/qterminal-l10n.list

%changelog

%autochangelog
