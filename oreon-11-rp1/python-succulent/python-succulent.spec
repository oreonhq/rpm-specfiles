%global source0_hash e679bdf9507b904f3663cf80d97188eff4cbd3248c6b9b8e78d19134de947a96
Name:           python-succulent
Version:        0.4.6
Release:        1%{?dist}
Summary:        A lightweight framework for collecting and processing data from HTTP POST requests
License:        MIT
URL:            https://github.com/firefly-cpp/succulent
Source0:        https://files.pythonhosted.org/packages/source/s/succulent/succulent-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-succulent = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-succulent
Summary:        A lightweight framework for collecting and processing data from HTTP POST requests
%description -n python3-succulent

%prep
%global oreon_srcdir succulent-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-succulent usr/lib/python3*/site-packages/succulent* usr/lib64/python3*/site-packages/succulent* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/succulent* usr/lib64/python3*/site-packages/succulent* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-succulent -f %{oreon_filedir}/python3-succulent.list

%changelog

%autochangelog
