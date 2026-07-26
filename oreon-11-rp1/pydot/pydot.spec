%global source0_hash d58e7a1bdaf7e47a0da21af0370139242b83ac0bfdfa926b3b054c5f9e4211b2

%global common_desc								\
An interface for creating both directed and non directed graphs from Python.	\
Currently all attributes implemented in the Dot language are supported.												\
										\
Output can be inlined in Postscript into interactive scientific environments	\
like TeXmacs, or output in any of the format's supported by the Graphviz	\
tools dot, neato, twopi.

Name:		pydot
Version:	4.0.1
Release:	6%{?dist}
Summary:	Python interface to Graphviz's Dot language
License:	MIT
URL:		https://github.com/pydot/pydot
Source0:	https://github.com/pydot/pydot/archive/refs/tags/v%{version}.tar.gz
Patch0:		https://github.com/pydot/pydot/commit/103a1a1d7027d90eab7577a8860dba2b09e94ec6.patch
# Replace parameterized with built-in pytest functionality
# https://github.com/pydot/pydot/pull/515
Patch2:		%{url}/pull/515.patch
BuildArch:	noarch

BuildRequires:	tomcli

%description
%{common_desc}

%package -n python3-%{name}
Summary:	Python3 interface to the Graphviz Dot language
BuildRequires:	python3-devel
BuildRequires:	graphviz-devel
Requires:	graphviz
%if 0%{?fedora} >= 43
# Additional req't for tests (no JPEG output from GDKPixbuf-less Graphvi)z
BuildRequires: graphviz-devil
Recommends: graphviz-devil
%endif
Provides:	%{name} = %{version}-%{release}

%description -n python3-%{name}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 

# Do not depend on linters, typecheckers, or coverage tools
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem project.optional-dependencies.dev \
    'pydot\[(lint|types)\]'
tomcli set pyproject.toml lists delitem project.optional-dependencies.tests \
    'pytest-cov'
sed -r -i 's/--cov\b//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -t -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pydot

%check
%tox

%files -n python3-%{name} -f %{pyproject_files}
%doc ChangeLog README.md

%changelog
%autochangelog
