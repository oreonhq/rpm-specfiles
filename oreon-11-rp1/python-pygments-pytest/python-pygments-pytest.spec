%global source0_hash 564b1a9bb9d254b93586361cf26a58011d71c66f8af20c33eaf5c3505e35ef28
Name:           python-pygments-pytest
Version:        2.5.0
Release:        1%{?dist}
Summary:        A pygments lexer for pytest output.
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source0:        https://files.pythonhosted.org/packages/source/p/pygments_pytest/pygments_pytest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pygments-pytest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygments-pytest
Summary:        A pygments lexer for pytest output.
%description -n python3-pygments-pytest

%prep
%global oreon_srcdir pygments_pytest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygments-pytest usr/lib/python3*/site-packages/pygments_pytest* usr/lib64/python3*/site-packages/pygments_pytest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygments_pytest* usr/lib64/python3*/site-packages/pygments_pytest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygments-pytest -f %{oreon_filedir}/python3-pygments-pytest.list

%changelog

%autochangelog
