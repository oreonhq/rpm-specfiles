%global source0_hash 2be1891bf498cb38030ca5db1ad022c502557c1c0b8ff6ac3fdac8254a5bb76b
%undefine __cmake_in_source_build
Name:    okteta
Summary:        Binary/hex editor
Epoch:   1
Version: 0.26.25
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://cgit.kde.org/%{name}.git
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Patch0: okteta-gcc11.patch
Requires: kio-extras-kf5
Conflicts: kde-l10n < 17.03
Conflicts:      kdesdk-common < 4.10.80
Obsoletes:      kdesdk-okteta < 4.10.80
Provides:       kdesdk-okteta = %{epoch}:%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: castxml libxslt
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-kbookmarks-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(qca2-qt5)
# /oreon:deps
%description
Okteta is a binary/hex editor for KDE

%package libs
Summary: Runtime libraries and kpart plugins for %{name}
Obsoletes: kdesdk-okteta-libs < 4.10.80
Provides:  kdesdk-okteta-libs = %{epoch}:%{version}-%{release}
Provides:  okteta5-part = %{epoch}:%{version}-%{release}
Provides:  okteta5-part%{?_isa} = %{epoch}:%{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Obsoletes: kdesdk-okteta-devel < 4.10.80
Provides:  kdesdk-okteta-devel = %{epoch}:%{version}-%{release}
Provides:  okteta5-devel = %{epoch}:%{version}-%{release}
Requires:  %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.okteta.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.okteta.desktop
%files -f %{oreon_filedir}/main.list
%files -n okteta-libs -f %{oreon_filedir}/okteta-libs.list
%files -n okteta-devel -f %{oreon_filedir}/okteta-devel.list

%changelog

%autochangelog
