%global source0_hash 70ec0b03a474fd5c29ce2d2050e15546e91f4e7d5f709d209ad45d091deaa2f6
Name:           python-mirakuru
Version:        3.0.3
Release:        1%{?dist}
Summary:        Process executor _not only_ for tests.
License:        LGPL-3.0-or-later
URL:            https://github.com/dbfixtures/mirakuru
Source0:        https://files.pythonhosted.org/packages/source/m/mirakuru/mirakuru-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) >= 0.11
Requires:       python3-mirakuru = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mirakuru
Summary:        Process executor _not only_ for tests.
# oreon:reqs
Requires:       python3dist(psutil) >= 4.0.0
# /oreon:reqs
%description -n python3-mirakuru

%prep
%global oreon_srcdir mirakuru-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mirakuru usr/lib/python3*/site-packages/mirakuru* usr/lib64/python3*/site-packages/mirakuru* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mirakuru* usr/lib64/python3*/site-packages/mirakuru* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mirakuru -f %{oreon_filedir}/python3-mirakuru.list

%changelog

%autochangelog
