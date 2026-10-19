%global source0_hash 8558f304df08ce400958e6ae6d632e43ef61ccca463c9e8df4f265b4a6195e79
Name:           python-qcelemental
Version:        0.51.2
Release:        1%{?dist}
Summary:        Core data structures for Quantum Chemistry.
License:        ...
URL:            https://github.com/MolSSI/QCElemental
Source0:        https://files.pythonhosted.org/packages/source/q/qcelemental/qcelemental-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm) >= 8.0
Requires:       python3-qcelemental = %{version}-%{release}
# /oreon:deps
%package -n       python3-qcelemental+standard
Summary:        Metapackage for python3-qcelemental standard extras
Requires:       python3-qcelemental = %{version}-%{release}
Provides:       python3dist(qcelemental[standard]) = %{version}-%{release}

%description -n python3-qcelemental+standard
Metapackage for python3-qcelemental standard extras.

%package -n       python3-qcelemental+viz
Summary:        Metapackage for python3-qcelemental viz extras
Requires:       python3-qcelemental = %{version}-%{release}
Requires:       python3dist(setuptools) >= 68.0.0
Requires:       python3dist(ipykernel) < 6.0
Provides:       python3dist(qcelemental[viz]) = %{version}-%{release}

%description -n python3-qcelemental+viz
Metapackage for python3-qcelemental viz extras.

%package -n       python3-qcelemental+align
Summary:        Metapackage for python3-qcelemental align extras
Requires:       python3-qcelemental = %{version}-%{release}
Requires:       python3dist(networkx) < 3.0
Provides:       python3dist(qcelemental[align]) = %{version}-%{release}

%description -n python3-qcelemental+align
Metapackage for python3-qcelemental align extras.

%package -n       python3-qcelemental+test
Summary:        Metapackage for python3-qcelemental test extras
Requires:       python3-qcelemental = %{version}-%{release}
Provides:       python3dist(qcelemental[test]) = %{version}-%{release}

%description -n python3-qcelemental+test
Metapackage for python3-qcelemental test extras.

%package -n       python3-qcelemental+lint
Summary:        Metapackage for python3-qcelemental lint extras
Requires:       python3-qcelemental = %{version}-%{release}
Requires:       python3dist(black) >= 25.1.0
Requires:       python3dist(black) < 26.0a0
Requires:       python3dist(isort) >= 6.1.0
Provides:       python3dist(qcelemental[lint]) = %{version}-%{release}

%description -n python3-qcelemental+lint
Metapackage for python3-qcelemental lint extras.

%package -n       python3-qcelemental+docs
Summary:        Metapackage for python3-qcelemental docs extras
Requires:       python3-qcelemental = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(autodoc-pydantic) > 2.0
Provides:       python3dist(qcelemental[docs]) = %{version}-%{release}

%description -n python3-qcelemental+docs
Metapackage for python3-qcelemental docs extras.

%description

%package -n     python3-qcelemental
Summary:        Core data structures for Quantum Chemistry.
# oreon:reqs
Requires:       python3dist(numpy) >= 2.3.3
Requires:       python3dist(pint) >= 0.24
Requires:       python3dist(pydantic) >= 2.11
Requires:       python3dist(pydantic) >= 2.12
# /oreon:reqs
%description -n python3-qcelemental

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir qcelemental-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-qcelemental usr/lib/python3*/site-packages/qcelemental* usr/lib64/python3*/site-packages/qcelemental* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/qcelemental* usr/lib64/python3*/site-packages/qcelemental* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-qcelemental -f %{oreon_filedir}/python3-qcelemental.list

%changelog

%autochangelog
