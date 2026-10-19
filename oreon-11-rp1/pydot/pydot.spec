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
Release:        1%{?dist}
Summary:        Python interface to Graphviz's Dot language
License:	MIT
URL:		https://github.com/pydot/pydot
Source0:        https://github.com/pydot/pydot/archive/refs/tags/v%{version}.tar.gz
Patch0:		https://github.com/pydot/pydot/commit/103a1a1d7027d90eab7577a8860dba2b09e94ec6.patch
Patch2:		%{url}/pull/515.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.3.2
Requires:       python3-pydot = %{version}-%{release}
# /oreon:deps
%package -n       python3-pydot+lint
Summary:        Metapackage for python3-pydot lint extras
Requires:       python3-pydot = %{version}-%{release}
Provides:       python3dist(pydot[lint]) = %{version}-%{release}

%description -n python3-pydot+lint
Metapackage for python3-pydot lint extras.

%package -n       python3-pydot+types
Summary:        Metapackage for python3-pydot types extras
Requires:       python3-pydot = %{version}-%{release}
Provides:       python3dist(pydot[types]) = %{version}-%{release}

%description -n python3-pydot+types
Metapackage for python3-pydot types extras.

%package -n       python3-pydot+dev
Summary:        Metapackage for python3-pydot dev extras
Requires:       python3-pydot = %{version}-%{release}
Provides:       python3dist(pydot[dev]) = %{version}-%{release}

%description -n python3-pydot+dev
Metapackage for python3-pydot dev extras.

%package -n       python3-pydot+tests
Summary:        Metapackage for python3-pydot tests extras
Requires:       python3-pydot = %{version}-%{release}
Provides:       python3dist(pydot[tests]) = %{version}-%{release}

%description -n python3-pydot+tests
Metapackage for python3-pydot tests extras.

%package -n       python3-pydot+release
Summary:        Metapackage for python3-pydot release extras
Requires:       python3-pydot = %{version}-%{release}
Provides:       python3dist(pydot[release]) = %{version}-%{release}

%description -n python3-pydot+release
Metapackage for python3-pydot release extras.

%description
%{common_desc}

%package -n python3-%{name}
Summary:	Python3 interface to the Graphviz Dot language
BuildRequires:	python3-devel
BuildRequires:	graphviz-devel
Requires:	graphviz
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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pydot* usr/lib64/python3*/site-packages/pydot* usr/bin/*

%check

%tox
%files
%files -n python3-pydot -f %{oreon_filedir}/python3-pydot.list

%changelog

%autochangelog
