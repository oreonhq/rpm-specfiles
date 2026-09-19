%global source0_hash 04481e3fd21199a3b4ff8aea8a2cec46586a4efc9bb52096b49b5676031944f9

# https://github.com/hluk/qxtglobalshortcut/commit/16446200b699e0610b8a5fb20b74938225d81d87
%global commit 16446200b699e0610b8a5fb20b74938225d81d87
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20171021

Name:           qxtglobalshortcut
Version:        0.0.1
Release:        0.31.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Cross-platform library for handling system-wide shortcuts in Qt applications
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/hluk/qxtglobalshortcut
Source0:        https://github.com/hluk/qxtglobalshortcut/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5)
%if 0%{?fedora} > 32
BuildRequires:  qt5-qtbase-private-devel
%endif

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
# TODO: Please submit an issue to upstream (rhbz#2381403)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
 -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
