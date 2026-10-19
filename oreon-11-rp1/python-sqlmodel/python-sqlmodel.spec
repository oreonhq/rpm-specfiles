%global source0_hash 9ecec2b6aa4c2aa58da39d2572e7bef4373419dcd6ec52973c07de7be2b1c516
Name:           python-sqlmodel
Version:        0.0.42
Release:        1%{?dist}
Summary:        SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
License:        MIT
URL:            https://github.com/fastapi/sqlmodel
Source0:        https://files.pythonhosted.org/packages/source/s/sqlmodel/sqlmodel-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Downstream-only-Patch-for-running-tests-without-cove.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sqlmodel = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sqlmodel
Summary:        SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
# oreon:reqs
Requires:       python3dist(pydantic) >= 2.11.0
Requires:       python3dist(sqlalchemy) < 2.1.0
Requires:       python3dist(sqlalchemy) >= 2.0.14
Requires:       python3dist(typing-extensions) >= 4.5.0
# /oreon:reqs
%description -n python3-sqlmodel

%prep
%global oreon_srcdir sqlmodel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlmodel usr/lib/python3*/site-packages/sqlmodel* usr/lib64/python3*/site-packages/sqlmodel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlmodel* usr/lib64/python3*/site-packages/sqlmodel* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlmodel -f %{oreon_filedir}/python3-sqlmodel.list

%changelog

%autochangelog
