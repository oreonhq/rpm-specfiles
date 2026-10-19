%global source0_hash 358bb878b7b1e20e90dc944ac4261796dd3d5c2b7860aa960a08fc10e0b5beff
Name:           python-optuna
Version:        5.0.0
Release:        1%{?dist}
Summary:        A hyperparameter optimization framework
License:        MIT
URL:            https://optuna.org/
Source0:        https://files.pythonhosted.org/packages/source/o/optuna/optuna-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.1.0
Requires:       python3-optuna = %{version}-%{release}
# /oreon:deps
%package -n       python3-optuna+document
Summary:        Metapackage for python3-optuna document extras
Requires:       python3-optuna = %{version}-%{release}
Requires:       python3dist(cmaes) >= 0.12.0
Requires:       python3dist(kaleido) < 0.4
Requires:       python3dist(matplotlib)
Requires:       python3dist(plotly) >= 4.9.0
Requires:       python3dist(plotly) < 7
Requires:       python3dist(sphinx-rtd-theme) >= 1.2.0
Provides:       python3dist(optuna[document]) = %{version}-%{release}

%description -n python3-optuna+document
Metapackage for python3-optuna document extras.

%package -n       python3-optuna+optional
Summary:        Metapackage for python3-optuna optional extras
Requires:       python3-optuna = %{version}-%{release}
Requires:       python3dist(cmaes) >= 0.12.0
Requires:       python3dist(matplotlib)
Requires:       python3dist(plotly) >= 4.9.0
Requires:       python3dist(scikit-learn) >= 0.24.2
Requires:       python3dist(protobuf) >= 5.28.1
Provides:       python3dist(optuna[optional]) = %{version}-%{release}

%description -n python3-optuna+optional
Metapackage for python3-optuna optional extras.

%description

%package -n     python3-optuna
Summary:        A hyperparameter optimization framework
# oreon:reqs
Requires:       python3dist(alembic) >= 1.5.0
Requires:       python3dist(packaging) >= 20.0
Requires:       python3dist(sqlalchemy) >= 1.4.2
# /oreon:reqs
%description -n python3-optuna

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir optuna-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-optuna usr/lib/python3*/site-packages/optuna* usr/lib64/python3*/site-packages/optuna* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/optuna* usr/lib64/python3*/site-packages/optuna* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-optuna -f %{oreon_filedir}/python3-optuna.list

%changelog

%autochangelog
