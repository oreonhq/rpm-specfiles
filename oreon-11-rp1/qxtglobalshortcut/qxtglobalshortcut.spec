%global source0_hash 04481e3fd21199a3b4ff8aea8a2cec46586a4efc9bb52096b49b5676031944f9
%global commit 16446200b699e0610b8a5fb20b74938225d81d87
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20171021
Name:           qxtglobalshortcut
Version:        0.0.1
Release:        1%{?dist}
Summary:        Cross-platform library for handling system-wide shortcuts in Qt applications
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/hluk/qxtglobalshortcut
Source0:        https://github.com/hluk/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5)
# /oreon:deps
%description
Cross-platform library for handling system-wide shortcuts in Qt applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}
%description devel
This package provides libraries, header files and documentation for developing
applications using qxtglobalshortcut library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# remove windows files
rm -rf utils/appveyor/
rm -f appveyor.yml

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
 -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qxtglobalshortcut-devel -f %{oreon_filedir}/qxtglobalshortcut-devel.list

%changelog

%autochangelog
