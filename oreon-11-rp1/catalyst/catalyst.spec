%global source0_hash 7558b9fd4c5c9cc74ebf29f97898d6c5013d85268c9d9a2cd5e32f98cb0b73aa
%global commit 2fc94c55ba4eb994f27728141ebcf15c3435f306
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
Name:           catalyst
Version:        2.0
Release:        1%{?dist}
Summary:        API specification for simulations to analyze and visualize data in situ
License:        LicenseRef-Callaway-BSD
URL:            https://gitlab.kitware.com/paraview/catalyst
Source0:        https://gitlab.kitware.com/paraview/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         catalyst-unbundle.patch
Provides: bundled(conduit)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libb64-devel
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  rapidjson-devel
# /oreon:deps
%description
Catalyst is an API specification developed for simulations (and other
scientific data producers) to analyze and visualize data in situ.

Catalyst has been split out of ParaView. This package includes the definition
together with a lightweight implementation of this Catalyst API.

For details how to use Catalyst for in situ analysis and visualization in
simulations, see https://catalyst-in-situ.readthedocs.io/en/latest/index.html.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
rm -r thirdparty/conduit/{libb64,libyaml,rapidjson}

%build

%cmake 
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n catalyst-devel -f %{oreon_filedir}/catalyst-devel.list

%changelog

%autochangelog
