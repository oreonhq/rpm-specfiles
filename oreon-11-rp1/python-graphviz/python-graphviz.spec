%global source0_hash 20743e7183be82aaaa8ad6c93f8893c923bd6658a04c32ee115edb3c8a835f78
Name:           python-graphviz
Version:        0.21
Release:        1%{?dist}
Summary:        Simple Python interface for Graphviz
License:        MIT
URL:            https://github.com/xflr6/graphviz
Source0:        https://files.pythonhosted.org/packages/source/g/graphviz/graphviz-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-graphviz = %{version}-%{release}
# /oreon:deps
%package -n       python3-graphviz+dev
Summary:        Metapackage for python3-graphviz dev extras
Requires:       python3-graphviz = %{version}-%{release}
Requires:       python3dist(tox) >= 3
Provides:       python3dist(graphviz[dev]) = %{version}-%{release}

%description -n python3-graphviz+dev
Metapackage for python3-graphviz dev extras.

%package -n       python3-graphviz+test
Summary:        Metapackage for python3-graphviz test extras
Requires:       python3-graphviz = %{version}-%{release}
Requires:       python3dist(pytest) >= 7
Requires:       python3dist(pytest) < 8.1
Requires:       python3dist(pytest-mock) >= 3
Provides:       python3dist(graphviz[test]) = %{version}-%{release}

%description -n python3-graphviz+test
Metapackage for python3-graphviz test extras.

%package -n       python3-graphviz+docs
Summary:        Metapackage for python3-graphviz docs extras
Requires:       python3-graphviz = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5
Requires:       python3dist(sphinx) < 7
Requires:       python3dist(sphinx-rtd-theme) >= 0.2.5
Provides:       python3dist(graphviz[docs]) = %{version}-%{release}

%description -n python3-graphviz+docs
Metapackage for python3-graphviz docs extras.

%description

%package -n     python3-graphviz
Summary:        Simple Python interface for Graphviz
%description -n python3-graphviz

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir graphviz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-graphviz usr/lib/python3*/site-packages/graphviz* usr/lib64/python3*/site-packages/graphviz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/graphviz* usr/lib64/python3*/site-packages/graphviz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-graphviz -f %{oreon_filedir}/python3-graphviz.list

%changelog

%autochangelog
