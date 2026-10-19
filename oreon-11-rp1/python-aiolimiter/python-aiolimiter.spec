%global source0_hash 7343008c2228e89def7d4ce29ab98ee98822bf5db69018c09c90088929f7c104
Name:           python-aiolimiter
Version:        1.3.0
Release:        1%{?dist}
Summary:        asyncio rate limiter, a leaky bucket implementation
License:        MIT
URL:            https://github.com/mjpieters/aiolimiter
Source0:        https://files.pythonhosted.org/packages/source/a/aiolimiter/aiolimiter-%{version}.tar.gz
BuildArch:      noarch
Patch: 0001-tests-Prefer-tomllib-where-available.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27
BuildRequires:  python3dist(uv-dynamic-versioning) >= 0.8
Requires:       python3-aiolimiter = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aiolimiter
Summary:        asyncio rate limiter, a leaky bucket implementation
%description -n python3-aiolimiter

%prep
%global oreon_srcdir aiolimiter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiolimiter usr/lib/python3*/site-packages/aiolimiter* usr/lib64/python3*/site-packages/aiolimiter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiolimiter* usr/lib64/python3*/site-packages/aiolimiter* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiolimiter -f %{oreon_filedir}/python3-aiolimiter.list

%changelog

%autochangelog
