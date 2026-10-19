%global source0_hash fc124f751b1b04805c2a04b061898b436b45ab2320b045e1e052ea895de65189
Name:           python-croniter
Version:        6.2.4
Release:        1%{?dist}
Summary:        croniter provides iteration for datetime object with cron like format
License:        MIT
URL:            https://github.com/pallets-eco/croniter
Source0:        https://files.pythonhosted.org/packages/source/c/croniter/croniter-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-croniter-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) == 1.30.1
BuildRequires:  python3dist(packaging) == 26.2
BuildRequires:  python3dist(pathspec) == 1.1.1
BuildRequires:  python3dist(pluggy) == 1.6.0
BuildRequires:  python3dist(trove-classifiers) == 2026.6.1.19
Requires:       python3-croniter = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-croniter
Summary:        croniter provides iteration for datetime object with cron like format
%description -n python3-croniter

%prep
%global oreon_srcdir croniter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-croniter usr/lib/python3*/site-packages/croniter* usr/lib64/python3*/site-packages/croniter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/croniter* usr/lib64/python3*/site-packages/croniter* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-croniter -f %{oreon_filedir}/python3-croniter.list

%changelog

%autochangelog
