%global source0_hash 21bf16bc9cc46bf98f94382c4b5c3c389be7056ff0be33029111ae11b3f1c82a
Name:           python-pytest-freezer
Version:        0.4.9
Release:        1%{?dist}
Summary:        Pytest plugin providing a fixture interface for freezegun
License:        MIT
URL:            https://github.com/pytest-dev/pytest-freezer
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_freezer/pytest_freezer-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pytest-freezer = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-pytest-freezer
Summary:        Pytest plugin providing a fixture interface for freezegun
# oreon:reqs
Requires:       python3dist(freezegun) >= 1.1
Requires:       python3dist(pytest) >= 3.6
# /oreon:reqs
%description -n python3-pytest-freezer %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-freezer usr/lib/python3*/site-packages/pytest_freezer* usr/lib64/python3*/site-packages/pytest_freezer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_freezer* usr/lib64/python3*/site-packages/pytest_freezer* usr/bin/*

%check

%pytest -v
%files
%files -n python3-pytest-freezer -f %{oreon_filedir}/python3-pytest-freezer.list

%changelog

%autochangelog
