%global source0_hash 7e327b255dee3de3c8f7fef58f835ccb7685881ea72176697ff60269c57743b2
Name:           python-holidays
Version:        0.104
Release:        1%{?dist}
Summary:        Open World Holidays Framework
License:        MIT
URL:            https://github.com/vacanza/holidays/
Source0:        https://files.pythonhosted.org/packages/source/h/holidays/holidays-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-holidays = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-holidays
Summary:        Open World Holidays Framework
# oreon:reqs
Requires:       python3dist(python-dateutil) < 3
Requires:       python3dist(python-dateutil) >= 2.9.0.post0
# /oreon:reqs
%description -n python3-holidays

%prep
%global oreon_srcdir holidays-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-holidays usr/lib/python3*/site-packages/holidays* usr/lib64/python3*/site-packages/holidays* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/holidays* usr/lib64/python3*/site-packages/holidays* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-holidays -f %{oreon_filedir}/python3-holidays.list

%changelog

%autochangelog
