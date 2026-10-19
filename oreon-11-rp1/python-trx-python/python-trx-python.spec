%global source0_hash e09c9288fce2c31952f561e9d2061ce49be26be14b1175f9d8251c30cfd3d406
Name:           python-trx-python
Version:        0.5.0
Release:        1%{?dist}
Summary:        A community-oriented file format for tractography
License:        ...
URL:            https://github.com/tee-ar-ex/trx-python
Source0:        https://files.pythonhosted.org/packages/source/t/trx_python/trx_python-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/pull/75.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7
Requires:       python3-trx-python = %{version}-%{release}
# /oreon:deps
%package -n       python3-trx-python+utils
Summary:        Metapackage for python3-trx-python utils extras
Requires:       python3-trx-python = %{version}-%{release}
Requires:       python3dist(fury) >= 0.10.0
Requires:       python3dist(fury) < 2.0.0
Provides:       python3dist(trx-python[utils]) = %{version}-%{release}

%description -n python3-trx-python+utils
Metapackage for python3-trx-python utils extras.

%package -n       python3-trx-python+dev
Summary:        Metapackage for python3-trx-python dev extras
Requires:       python3-trx-python = %{version}-%{release}
Requires:       python3dist(spin) >= 0.13
Provides:       python3dist(trx-python[dev]) = %{version}-%{release}

%description -n python3-trx-python+dev
Metapackage for python3-trx-python dev extras.

%package -n       python3-trx-python+doc
Summary:        Metapackage for python3-trx-python doc extras
Requires:       python3-trx-python = %{version}-%{release}
Requires:       python3dist(pydata-sphinx-theme) >= 0.16.1
Requires:       python3dist(sphinx) >= 8.2.0
Requires:       python3dist(sphinx-autoapi) >= 3.4.0
Provides:       python3dist(trx-python[doc]) = %{version}-%{release}

%description -n python3-trx-python+doc
Metapackage for python3-trx-python doc extras.

%package -n       python3-trx-python+style
Summary:        Metapackage for python3-trx-python style extras
Requires:       python3-trx-python = %{version}-%{release}
Provides:       python3dist(trx-python[style]) = %{version}-%{release}

%description -n python3-trx-python+style
Metapackage for python3-trx-python style extras.

%package -n       python3-trx-python+test
Summary:        Metapackage for python3-trx-python test extras
Requires:       python3-trx-python = %{version}-%{release}
Requires:       python3dist(pytest) >= 7
Requires:       python3dist(pytest-console-scripts) >= 0
Provides:       python3dist(trx-python[test]) = %{version}-%{release}

%description -n python3-trx-python+test
Metapackage for python3-trx-python test extras.

%package -n       python3-trx-python+all
Summary:        Metapackage for python3-trx-python all extras
Requires:       python3-trx-python = %{version}-%{release}
Provides:       python3dist(trx-python[all]) = %{version}-%{release}

%description -n python3-trx-python+all
Metapackage for python3-trx-python all extras.

%description

%package -n     python3-trx-python
Summary:        A community-oriented file format for tractography
# oreon:reqs
Requires:       python3dist(nibabel) >= 5
Requires:       python3dist(numpy) >= 1.22
Requires:       python3dist(typer) >= 0.9
# /oreon:reqs
%description -n python3-trx-python

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir trx_python-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-trx-python usr/lib/python3*/site-packages/trx_python* usr/lib64/python3*/site-packages/trx_python* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/trx_python* usr/lib64/python3*/site-packages/trx_python* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-trx-python -f %{oreon_filedir}/python3-trx-python.list

%changelog

%autochangelog
