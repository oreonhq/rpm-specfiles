%global source0_hash dc3d82e1fe00e491829d8939c549bf4bd9b39a260f87113c619b9d517c2f8ff1
Name:           python-pytest-httpserver
Version:        1.1.5
Release:        1%{?dist}
Summary:        pytest-httpserver is a httpserver for pytest
License:        MIT
URL:            https://github.com/csernazs/pytest-httpserver
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_httpserver/pytest_httpserver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-pytest-httpserver = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-httpserver
Summary:        pytest-httpserver is a httpserver for pytest
# oreon:reqs
Requires:       python3dist(werkzeug) >= 2.0.0
# /oreon:reqs
%description -n python3-pytest-httpserver

%prep
%global oreon_srcdir pytest_httpserver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-httpserver usr/lib/python3*/site-packages/pytest_httpserver* usr/lib64/python3*/site-packages/pytest_httpserver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_httpserver* usr/lib64/python3*/site-packages/pytest_httpserver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-httpserver -f %{oreon_filedir}/python3-pytest-httpserver.list

%changelog

%autochangelog
