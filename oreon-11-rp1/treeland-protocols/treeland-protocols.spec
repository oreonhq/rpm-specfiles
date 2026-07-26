%global source0_hash 3fa6342c0d42f8cf4c1313a833011971ac555d9221dae2dcd362a3fe0ba250bb

Name:           treeland-protocols
Version:        0.5.4
Release:        %autorelease
Summary:        Wayland protocol extensions for treeland
License:        Apache-2.0 OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://github.com/linuxdeepin/treeland-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Wayland protocol extensions for treeland.

%package        devel
Summary:        Development files for %{name}

%description    devel
Wayland protocol extensions for treeland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSES/
%doc README.md
%{_datadir}/cmake/TreelandProtocols/
%{_datadir}/pkgconfig/treeland-protocols.pc
%dir %{_datadir}/treeland-protocols
%{_datadir}/treeland-protocols/*.xml

%changelog
%autochangelog
