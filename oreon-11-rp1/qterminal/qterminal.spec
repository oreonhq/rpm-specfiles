%global source0_hash c2cc182e23f142bf2318523c7063012d146a802cd7b6d59e4f7563869a307dc5

Name:		qterminal
Version:	2.3.0
Release:	2%{?dist}
License:	GPL-2.0-only
URL:		https://github.com/qterminal/qterminal
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary:	Advanced Qt6-based terminal emulator

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(lxqt) >= 1.0.0
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  lxqt-build-tools
BuildRequires:  cmake(Qt6Test)
BuildRequires:	pkgconfig(qtermwidget6)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libcanberra-devel
BuildRequires:  perl-devel
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

# Require qtermwidget to be the same version, as suggested by upstream
Requires:       qtermwidget >= 2.2.0

Provides:       %{name}-common = %{version}-%{release}
Provides:       %{name}-qt5 = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-qt5 < %{version}-%{release}

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-drop.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_metainfodir}/qterminal.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%{_datadir}/icons/*/*
%{_datadir}/%{name}

%files l10n -f qterminal.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/qterminal/translations

%changelog
%autochangelog
