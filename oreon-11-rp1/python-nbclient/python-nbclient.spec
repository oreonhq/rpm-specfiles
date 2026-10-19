%global source0_hash 04a134a5b087f2c5887f228aca155db50169b8cd9334dee6942c8e927e56081a
Name:           python-nbclient
Version:        0.11.0
Release:        1%{?dist}
Summary:        A client library for executing notebooks. Formerly nbconvert_s ExecutePreprocessor.
License:        ...
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/n/nbclient/nbclient-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/jupyter/nbclient/commit/b42ad03acc0bb1ed26db65ab72ac617679cbbb62.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.10.0
Requires:       python3-nbclient = %{version}-%{release}
# /oreon:deps
%package -n       python3-nbclient+test
Summary:        Metapackage for python3-nbclient test extras
Requires:       python3-nbclient = %{version}-%{release}
Requires:       python3dist(ipykernel) >= 6.19.3
Requires:       python3dist(nbconvert) >= 7.1.0
Requires:       python3dist(pytest-asyncio) >= 1.3.0
Requires:       python3dist(pytest-cov) >= 4.0
Requires:       python3dist(pytest) >= 9.0.1
Requires:       python3dist(pytest) < 10
Provides:       python3dist(nbclient[test]) = %{version}-%{release}

%description -n python3-nbclient+test
Metapackage for python3-nbclient test extras.

%package -n       python3-nbclient+docs
Summary:        Metapackage for python3-nbclient docs extras
Requires:       python3-nbclient = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.7
Provides:       python3dist(nbclient[docs]) = %{version}-%{release}

%description -n python3-nbclient+docs
Metapackage for python3-nbclient docs extras.

%package -n       python3-nbclient+dev
Summary:        Metapackage for python3-nbclient dev extras
Requires:       python3-nbclient = %{version}-%{release}
Provides:       python3dist(nbclient[dev]) = %{version}-%{release}

%description -n python3-nbclient+dev
Metapackage for python3-nbclient dev extras.

%description

%package -n     python3-nbclient
Summary:        A client library for executing notebooks. Formerly nbconvert_s ExecutePreprocessor.
# oreon:reqs
Requires:       python3dist(jupyter-client) >= 7.0.0
Requires:       python3dist(jupyter-core) >= 5.4.0
Requires:       python3dist(nbformat) >= 5.2.0
Requires:       python3dist(traitlets) >= 5.13
# /oreon:reqs
%description -n python3-nbclient

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir nbclient-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nbclient usr/lib/python3*/site-packages/nbclient* usr/lib64/python3*/site-packages/nbclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nbclient* usr/lib64/python3*/site-packages/nbclient* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nbclient -f %{oreon_filedir}/python3-nbclient.list

%changelog

%autochangelog
