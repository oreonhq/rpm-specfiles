%global source0_hash 693b31bf0e61210b7616be4de7b0e133fdf44af3a14a49db5fafb8af6a908a1d
Name:           deepin-calculator
Version:        6.5.40
Release:        1%{?dist}
Summary:        An easy to use calculator for ordinary users
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-calculator
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Recommends:     deepin-manual
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -GNinja
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
