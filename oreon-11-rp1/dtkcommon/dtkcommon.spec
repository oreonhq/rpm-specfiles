%global source0_hash 5d45d2306e420d8091451efc06f66ba3582cffea27d2923ef0e205638e7d30c7

# This package contains files under %%_libdir but no binary files
%global debug_package %{nil}

Name:           dtkcommon
Version:        6.7.32
Release:        %autorelease
Summary:        A public project for building DTK Library
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
A public project for building DTK Library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_datadir}/dsg/configs/org.deepin.dtk.preference.json

%files devel
%{_libdir}/cmake/Dtk/
%{_libdir}/cmake/Dtk6/
%{_libdir}/cmake/DtkBuildHelper/

%changelog
%autochangelog
