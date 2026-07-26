%global source0_hash 9bf92ec683089da7e66ecac7e5ebedb5bac366946353dd85b74a49868ba55c23

%{!?python3_includedir: %global python3_includedir %(%{__python3} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")}
Name:       python-igraph
Version:    1.0.0
%global igraph_version 0.9
Release:    2%{?dist}
Summary:    Python bindings for igraph

License:    GPL-2.0-or-later
URL:        https://github.com/igraph/python-igraph
Source0:    https://github.com/igraph/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  igraph-devel >= %{igraph_version}
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel

BuildRequires:  python3-devel
BuildRequires:  cmake

BuildRequires:  git-core

# for tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist texttable}
BuildRequires:  %{py3_dist networkx}
BuildRequires:  %{py3_dist numpy}
# not available on ix86
BuildRequires:  (%{py3_dist pandas} or python3(x86-32))
BuildRequires:  %{py3_dist scipy}
# does not provide py3_dist variant, needs fixing
# not available on ix86
BuildRequires:  (python3-graph-tool or python3(x86-32))

%description
This module extends Python with a Graph class which is capable of
handling arbitrary directed and undirected graphs with thousands of
nodes and millions of edges. Since the module makes use of the open
source igraph library written in almost 100% pure C, it is blazing
fast and outperforms most other pure Python-based graph packages
around.

%package -n python3-igraph
Summary:    %{summary}
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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel -C--global-option=--use-pkg-config

%install
%pyproject_install
%pyproject_save_files -l igraph

%check
%pytest -v

%files -n python3-igraph -f %{pyproject_files}
%{_bindir}/igraph

%files -n python3-igraph-devel
%{python3_includedir}/igraph

%changelog
%autochangelog
