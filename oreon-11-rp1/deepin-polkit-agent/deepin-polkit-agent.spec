%global source0_hash d699b57fcbaf9c42ffc55892dc517eb2195daa087cade45f4dae8b7473e20d8b
%global repo dde-polkit-agent
Name:           deepin-polkit-agent
Version:        6.0.24
Release:        1%{?dist}
Summary:        Deepin Polkit Agent
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(DtkTools)
BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  qt5-linguist
# /oreon:deps
%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|qdbusxml2cpp|qdbusxml2cpp-qt5|' CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{repo} --with-qt
rm %{buildroot}%{_datadir}/dde-polkit-agent/translations/dde-polkit-agent.qm
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n deepin-polkit-agent-devel -f %{oreon_filedir}/deepin-polkit-agent-devel.list

%changelog

%autochangelog
