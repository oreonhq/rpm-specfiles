%global source0_hash 1e04b47ab91b6d1c8805d5b19cb4c19d7ca27ac90bb644d6cd9c088b5147c540
%{!?python3_includedir: %global python3_includedir %(%{__python3} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")}
Name:       python-igraph
Version:    1.0.0
%global igraph_version 0.9
Release:        2%{?dist}
Summary:        Python bindings for igraph
License:    GPL-2.0-or-later
URL:        https://github.com/igraph/python-igraph
Source0:        https://github.com/igraph/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cmake) >= 3.18
BuildRequires:  python3dist(setuptools) < 72.2.0
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-igraph = %{version}-%{release}
# /oreon:deps
%description
This module extends Python with a Graph class which is capable of
handling arbitrary directed and undirected graphs with thousands of
nodes and millions of edges. Since the module makes use of the open
source igraph library written in almost 100% pure C, it is blazing
fast and outperforms most other pure Python-based graph packages
around.

%package -n python3-igraph
Summary:        Python bindings for igraph
Requires:   libxml2
Requires:   igraph >= %{igraph_version}
%description -n python3-igraph
This module extends Python with a Graph class which is capable of
handling arbitrary directed and undirected graphs with thousands of
nodes and millions of edges. Since the module makes use of the open
source igraph library written in almost 100% pure C, it is blazing
fast and outperforms most other pure Python-based graph packages
around.

%package -n python3-igraph-devel
Requires:  python3-igraph = %{version}-%{release}
Requires:  pkgconfig
Summary:   Development files for igraph
%description -n python3-igraph-devel
The python3-igraph-devel package contains the header files and some
documentation needed to develop application with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -p0

%build

%pyproject_wheel -C--global-option=--use-pkg-config
%install
%pyproject_install
%oreon_autofiles python3-igraph usr/lib/python3*/site-packages/igraph* usr/lib64/python3*/site-packages/igraph* usr/bin/*
%oreon_autofiles python3-igraph-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/lib/python3*/site-packages/igraph* usr/lib64/python3*/site-packages/igraph* usr/bin/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%pytest -v
%files
%files -n python3-igraph -f %{oreon_filedir}/python3-igraph.list
%files -n python3-igraph-devel -f %{oreon_filedir}/python3-igraph-devel.list

%changelog

%autochangelog
