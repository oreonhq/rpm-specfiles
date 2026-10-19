%global source0_hash cd9950fec2991e65364430dd419daeedf546928788f457e1106d5b751aea0be8
Name:           python-pytest-lsp
Version:        1.0.1
Release:        1%{?dist}
Summary:        A pytest plugin for end-to-end testing of language servers
License:        MIT
URL:            https://github.com/swyddfa/lsp-devtools
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_lsp/pytest_lsp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.17.1
Requires:       python3-pytest-lsp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-lsp
Summary:        A pytest plugin for end-to-end testing of language servers
# oreon:reqs
Requires:       python3dist(pygls) >= 2.0.0
Requires:       python3dist(pytest) >= 8.0
Requires:       python3dist(pytest-asyncio) >= 1.0
# /oreon:reqs
%description -n python3-pytest-lsp

%prep
%global oreon_srcdir pytest_lsp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-lsp usr/lib/python3*/site-packages/pytest_lsp* usr/lib64/python3*/site-packages/pytest_lsp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_lsp* usr/lib64/python3*/site-packages/pytest_lsp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-lsp -f %{oreon_filedir}/python3-pytest-lsp.list

%changelog

%autochangelog
