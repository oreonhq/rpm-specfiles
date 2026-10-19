%global source0_hash d3c72e0e46a8fa1ddabea8f830762402dee090caf33c30c2295ac7010db8f09c
Name:           python-doit
Version:        0.37.0
Release:        1%{?dist}
Summary:        doit - Automation Tool
License:        MIT
URL:            https://pydoit.org
Source0:        https://files.pythonhosted.org/packages/source/d/doit/doit-%{version}.tar.gz
BuildArch:      noarch
Patch1:         python-doit_ignore_versions.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68.0
Requires:       python3-doit = %{version}-%{release}
# /oreon:deps
%package -n       python3-doit+toml
Summary:        Metapackage for python3-doit toml extras
Requires:       python3-doit = %{version}-%{release}
Provides:       python3dist(doit[toml]) = %{version}-%{release}

%description -n python3-doit+toml
Metapackage for python3-doit toml extras.

%package -n       python3-doit+cloudpickle
Summary:        Metapackage for python3-doit cloudpickle extras
Requires:       python3-doit = %{version}-%{release}
Provides:       python3dist(doit[cloudpickle]) = %{version}-%{release}

%description -n python3-doit+cloudpickle
Metapackage for python3-doit cloudpickle extras.

%description

%package -n     python3-doit
Summary:        doit - Automation Tool
%description -n python3-doit

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir doit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-doit usr/lib/python3*/site-packages/doit* usr/lib64/python3*/site-packages/doit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/doit* usr/lib64/python3*/site-packages/doit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-doit -f %{oreon_filedir}/python3-doit.list

%changelog

%autochangelog
