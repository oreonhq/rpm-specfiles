%global source0_hash 629cada3e33e2b9bf376cdc7614a47a4140b8aedc1d836579e359736fbd82977
Name:           python-scikit-learn
Version:        1.9.1
Release:        1%{?dist}
Summary:        A set of python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org
Source0:        https://files.pythonhosted.org/packages/source/s/scikit_learn/scikit_learn-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 3.2.6
BuildRequires:  python3dist(cython) >= 3.1.2
BuildRequires:  python3dist(meson-python) < 0.22.0
BuildRequires:  python3dist(meson-python) >= 0.17.1
BuildRequires:  python3dist(numpy) < 2.6.0
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(scipy) < 1.19.0
BuildRequires:  python3dist(scipy) >= 1.10.0
Requires:       python3-scikit-learn = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-scikit-learn
Summary:        A set of python modules for machine learning and data mining
# oreon:reqs
Requires:       python3dist(joblib) >= 1.4.0
Requires:       python3dist(narwhals) >= 2.0.1
Requires:       python3dist(numpy) >= 1.24.1
Requires:       python3dist(scipy) >= 1.10.0
Requires:       python3dist(threadpoolctl) >= 3.5.0
# /oreon:reqs
%description -n python3-scikit-learn

%prep
%global oreon_srcdir scikit_learn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scikit-learn usr/lib/python3*/site-packages/scikit_learn* usr/lib64/python3*/site-packages/scikit_learn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scikit_learn* usr/lib64/python3*/site-packages/scikit_learn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-scikit-learn -f %{oreon_filedir}/python3-scikit-learn.list

%changelog

%autochangelog

