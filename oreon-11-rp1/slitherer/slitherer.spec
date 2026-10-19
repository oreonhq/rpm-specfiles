%global source0_hash 24be4896b8caed366ab7db4e93d0aaa913235ce12d280442bda20398b5468838
%global qt_minver 6.8
%global commit d230dbaa42d652419d2b7299bd0e650f63e5dbea
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251108
Name:           slitherer
Version:        0~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        Simple QtWebView based runner for Anaconda installer Web UI
License:        MPL-2.0 and BSD-3-Clause
URL:            https://gitlab.com/VelocityLimitless/Projects/slitherer
Source0:        https://gitlab.com/VelocityLimitless/Projects/%{name}/-/archive/%{commit}/%{name}-d230dba.tar.gz
Requires:       anaconda-webui
Supplements:    (anaconda-webui unless fedora-release-workstation)
Requires:      qt6-qtwebengine%{?_isa} >= 6.10.1-5
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6WebView)
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ninja-build
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -S git_am

%conf
%cmake_qt6

%build

%cmake_build
%install
%cmake_install
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-anaconda
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
