%global source0_hash 5ee332a31c5e86d6dd0a3bb7cd9a43e176adc2582f2e3b7d5e0c2fa9b90e9774

Name:    breeze-gtk
Version: 6.6.4
Release: 1%{?dist}
Summary: Breeze widget theme for GTK

License: BSD-3-Clause AND CC0-1.0
URL:     https://invent.kde.org/plasma/%{name}

Source0: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtk2-engines
BuildRequires:  plasma-breeze-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  sassc

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

# not used directly, but is an indirect dep from ECMQueryQmake.cmake
# probably should be fixed there -- rex
BuildRequires:  cmake(Qt6Core)

# main meta package to depend on all subpkgs, for cleaner/simpler upgrade path
Requires: %{name}-gtk2 = %{version}-%{release}
Requires: %{name}-gtk3 = %{version}-%{release}
Requires: %{name}-gtk4 = %{version}-%{release}

%description
%{summary}.

%package common
Summary:        Breeze widget theme for GTK common files
Conflicts:      breeze-gtk < 5.20.2-2

%description common
%{summary}.

%package gtk2
Summary:        Breeze widget theme for GTK 2
Requires:       gtk2-engines
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (plasma-breeze and gtk2)
%description gtk2
%{summary}.

%package gtk3
Summary:        Breeze widget theme for GTK 3
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (plasma-breeze and gtk3)
%description gtk3
%{summary}.

%package gtk4
Summary:        Breeze widget theme for GTK 4
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (plasma-breeze and gtk4)
%description gtk4
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%files
# empty metapackage

%files common
%license LICENSES/*.txt
%doc README.md
%dir %{_datadir}/themes/Breeze/
%{_datadir}/themes/Breeze/assets/
%{_datadir}/themes/Breeze/settings.ini
%dir %{_datadir}/themes/Breeze-Dark/
%{_datadir}/themes/Breeze-Dark/assets/
%{_datadir}/themes/Breeze-Dark/settings.ini

%files gtk2
%{_datadir}/themes/Breeze/gtk-2.0/
%{_datadir}/themes/Breeze-Dark/gtk-2.0/

%files gtk3
%{_datadir}/themes/Breeze/gtk-3.0/
%{_datadir}/themes/Breeze-Dark/gtk-3.0/

%files gtk4
%{_datadir}/themes/Breeze/gtk-4.0/
%{_datadir}/themes/Breeze-Dark/gtk-4.0/

%changelog
%autochangelog
