%global source0_hash 86c0f6d2836b184a250fc2907091c076bf53c9603dd291eaebade36cc342e13c
%global debug_package %{nil}
%global forgeurl https://github.com/ThePhD/sol2
Version: 3.5.0
Release:        1%{?dist}
%global tag v%{version}
%forgemeta
Name:           sol2
Summary:        a C++ <-> Lua API wrapper with advanced features and top notch performance
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  ninja-build
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:  lua-devel >= 5.4
%description devel
%{summary}.

%package devel-docs
Summary:        API documentation for %{name}-devel
Requires: %{name}-devel = %{version}-%{release}
BuildArch:  noarch
%description devel-docs
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{forgesetup}

%build

%cmake -G Ninja \
                -DSOL2_CI=ON \
                -DSOL2_BUILD_LUA=OFF \
                -DSOL2_LUA_VERSION=5.4 \
                -DSOL2_DOCS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sol2-devel -f %{oreon_filedir}/sol2-devel.list
%files -n sol2-devel-docs -f %{oreon_filedir}/sol2-devel-docs.list

%changelog

%autochangelog
