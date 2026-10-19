%global source0_hash 035e37496d245640353acb5629fec31946a57a12967e433c1cc54d3d2e83369e
%global forgeurl https://github.com/linuxdeepin/dareader
%global date 20230710
%global commit 933fddbdae37322674adfeeda201d70fd71390f9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta
Name:           dareader
Version:        0
Release:        1%{?dist}
Summary:        library for reading data from fd provided by deepin-authentication
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dareader-devel -f %{oreon_filedir}/dareader-devel.list

%changelog

%autochangelog
