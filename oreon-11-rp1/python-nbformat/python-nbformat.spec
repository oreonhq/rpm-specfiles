%global source0_hash 32d4521c68c6e7d5b29c76defaeed9f42ea733142b9b19f88277ce10390b9c4d
Name:           python-nbformat
Version:        5.11.1
Release:        1%{?dist}
Summary:        The Jupyter Notebook format
License:        ...
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/n/nbformat/nbformat-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5
Requires:       python3-nbformat = %{version}-%{release}
# /oreon:deps
%package -n       python3-nbformat+docs
Summary:        Metapackage for python3-nbformat docs extras
Requires:       python3-nbformat = %{version}-%{release}
Provides:       python3dist(nbformat[docs]) = %{version}-%{release}

%description -n python3-nbformat+docs
Metapackage for python3-nbformat docs extras.

%package -n       python3-nbformat+test
Summary:        Metapackage for python3-nbformat test extras
Requires:       python3-nbformat = %{version}-%{release}
Provides:       python3dist(nbformat[test]) = %{version}-%{release}

%description -n python3-nbformat+test
Metapackage for python3-nbformat test extras.

%description

%package -n     python3-nbformat
Summary:        The Jupyter Notebook format
# oreon:reqs
Requires:       python3dist(fastjsonschema) >= 2.15
Requires:       python3dist(jsonschema) >= 2.6
Requires:       python3dist(jupyter-core) >= 4.12
Requires:       python3dist(traitlets) >= 5.1
# /oreon:reqs
%description -n python3-nbformat

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir nbformat-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nbformat usr/lib/python3*/site-packages/nbformat* usr/lib64/python3*/site-packages/nbformat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nbformat* usr/lib64/python3*/site-packages/nbformat* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nbformat -f %{oreon_filedir}/python3-nbformat.list

%changelog

%autochangelog
