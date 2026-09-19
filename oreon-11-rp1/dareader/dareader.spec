%global source0_hash 035e37496d245640353acb5629fec31946a57a12967e433c1cc54d3d2e83369e

# no tag release
%global forgeurl https://github.com/linuxdeepin/dareader
%global date 20230710
%global commit 933fddbdae37322674adfeeda201d70fd71390f9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           dareader
Version:        0
Release:        %autorelease
Summary:        library for reading data from fd provided by deepin-authentication
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       dareader%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdareader.so.1*

%files devel
%{_libdir}/libdareader.so
%{_libdir}/pkgconfig/dareader.pc
%dir %{_includedir}/dareader
%{_includedir}/dareader/reader.h

%changelog
%autochangelog
