%global source0_hash a272fb95af0eddccb881c4c65cda0f0fe7ce7900559e953e56408824dbc556e3
%global forgeurl https://github.com/jrmadsen/PTL
Version:        2.3.3
%global date 20230707
%global commit f892a93d79615ed8f51c1b9c71f0f7b771dd8223
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta
Name:           ptl
Release:        1%{?dist}
Summary:        Lightweight C++11 mutilthreading tasking system
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/PTL-%{commit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  tbb-devel
# /oreon:deps
%description
Parallel Tasking Library (PTL) is a lightweight C++11 multithreading tasking
system featuring thread-pool, task-groups, and lock-free task queue.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_STATIC_LIBS=OFF \
    -DPTL_USE_TBB=ON \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n ptl-devel -f %{oreon_filedir}/ptl-devel.list

%changelog

%autochangelog
