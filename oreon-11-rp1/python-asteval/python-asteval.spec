%global source0_hash 46a4ed13cc2e4a29a21418f89dedd57db70d98eb96db0fb4c441d4edb2f5afed
Name:           python-asteval
Version:        1.0.10
Release:        1%{?dist}
Summary:        Safe, minimalistic evaluator of python expression using ast module
License:        MIT
URL:            https://github.com/lmfit/asteval
Source0:        https://files.pythonhosted.org/packages/source/a/asteval/asteval-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm) >= 6.2
Requires:       python3-asteval = %{version}-%{release}
# /oreon:deps
%package -n       python3-asteval+dev
Summary:        Metapackage for python3-asteval dev extras
Requires:       python3-asteval = %{version}-%{release}
Provides:       python3dist(asteval[dev]) = %{version}-%{release}

%description -n python3-asteval+dev
Metapackage for python3-asteval dev extras.

%package -n       python3-asteval+doc
Summary:        Metapackage for python3-asteval doc extras
Requires:       python3-asteval = %{version}-%{release}
Provides:       python3dist(asteval[doc]) = %{version}-%{release}

%description -n python3-asteval+doc
Metapackage for python3-asteval doc extras.

%package -n       python3-asteval+test
Summary:        Metapackage for python3-asteval test extras
Requires:       python3-asteval = %{version}-%{release}
Provides:       python3dist(asteval[test]) = %{version}-%{release}

%description -n python3-asteval+test
Metapackage for python3-asteval test extras.

%package -n       python3-asteval+all
Summary:        Metapackage for python3-asteval all extras
Requires:       python3-asteval = %{version}-%{release}
Provides:       python3dist(asteval[all]) = %{version}-%{release}

%description -n python3-asteval+all
Metapackage for python3-asteval all extras.

%description

%package -n     python3-asteval
Summary:        Safe, minimalistic evaluator of python expression using ast module
%description -n python3-asteval

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir asteval-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-asteval usr/lib/python3*/site-packages/asteval* usr/lib64/python3*/site-packages/asteval* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asteval* usr/lib64/python3*/site-packages/asteval* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-asteval -f %{oreon_filedir}/python3-asteval.list

%changelog

%autochangelog
