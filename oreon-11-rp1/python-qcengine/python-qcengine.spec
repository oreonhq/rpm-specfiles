%global source0_hash 23a122d132329585a8add8cd023d305c0c4c1f5032bf8a7ab22273e05d7c4c0d
Name:           python-qcengine
Version:        0.51.0
Release:        1%{?dist}
Summary:        A compute wrapper for Quantum Chemistry, ingesting and producing QCSchema for a variety of QC programs.
License:        ...
URL:            https://github.com/MolSSI/QCEngine
Source0:        https://files.pythonhosted.org/packages/source/q/qcengine/qcengine-%{version}.tar.gz
BuildArch:      noarch
Patch0:         https://github.com/MolSSI/QCEngine/pull/451.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
BuildRequires:  python3dist(setuptools-scm) >= 8.0
Requires:       python3-qcengine = %{version}-%{release}
# /oreon:deps
%package -n       python3-qcengine+test
Summary:        Metapackage for python3-qcengine test extras
Requires:       python3-qcengine = %{version}-%{release}
Provides:       python3dist(qcengine[test]) = %{version}-%{release}

%description -n python3-qcengine+test
Metapackage for python3-qcengine test extras.

%package -n       python3-qcengine+lint
Summary:        Metapackage for python3-qcengine lint extras
Requires:       python3-qcengine = %{version}-%{release}
Requires:       python3dist(black) >= 22.1.0
Requires:       python3dist(black) < 23.0a0
Requires:       python3dist(isort) >= 5.13.2
Provides:       python3dist(qcengine[lint]) = %{version}-%{release}

%description -n python3-qcengine+lint
Metapackage for python3-qcengine lint extras.

%package -n       python3-qcengine+docs
Summary:        Metapackage for python3-qcengine docs extras
Requires:       python3-qcengine = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(autodoc-pydantic) >= 2.0
Provides:       python3dist(qcengine[docs]) = %{version}-%{release}

%description -n python3-qcengine+docs
Metapackage for python3-qcengine docs extras.

%description

%package -n     python3-qcengine
Summary:        A compute wrapper for Quantum Chemistry, ingesting and producing QCSchema for a variety of QC programs.
# oreon:reqs
Requires:       python3dist(pydantic) >= 2.11
Requires:       python3dist(pydantic) >= 2.12
Requires:       python3dist(qcelemental) < 0.70.0
Requires:       python3dist(qcelemental) >= 0.50.4
# /oreon:reqs
%description -n python3-qcengine

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir qcengine-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-qcengine usr/lib/python3*/site-packages/qcengine* usr/lib64/python3*/site-packages/qcengine* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/qcengine* usr/lib64/python3*/site-packages/qcengine* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-qcengine -f %{oreon_filedir}/python3-qcengine.list

%changelog

%autochangelog
