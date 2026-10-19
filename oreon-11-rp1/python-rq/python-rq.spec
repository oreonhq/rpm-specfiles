%global source0_hash 78116d0c860f6285817b52d7d6d0b16a726372073ce8ea1d229732ce74ef9378
Name:           python-rq
Version:        2.12.0
Release:        1%{?dist}
Summary:        RQ is a simple, lightweight, library for creating background jobs, and processing them.
License:        BSD-2-Clause
URL:            https://python-rq.org/
Source0:        https://files.pythonhosted.org/packages/source/r/rq/rq-%{version}.tar.gz
BuildArch:      noarch
Patch: https://github.com/rq/rq/pull/2359.patch
Patch: https://github.com/rq/rq/commit/df29cf6.patch
Patch: https://github.com/rq/rq/commit/615525b.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rq = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rq
Summary:        RQ is a simple, lightweight, library for creating background jobs, and processing them.
# oreon:reqs
Requires:       python3dist(click) >= 5
Requires:       python3dist(redis) >= 3.5
# /oreon:reqs
%description -n python3-rq

%prep
%global oreon_srcdir rq-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rq usr/lib/python3*/site-packages/rq* usr/lib64/python3*/site-packages/rq* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rq* usr/lib64/python3*/site-packages/rq* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rq -f %{oreon_filedir}/python3-rq.list

%changelog

%autochangelog
