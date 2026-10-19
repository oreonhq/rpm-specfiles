%global source0_hash 3d546f92588e9ff97fa3d355e9111320262ae925ab4e541ef8cb99efe46d67bf
Name:           python-ipmi
Version:        1.1
Release:        1%{?dist}
Summary:        A ipmi python client used in NetXMS migrated from perl
License:        MIT
URL:            https://github.com/zhao-ji/check_ipmi_sensor_v3
Source0:        https://files.pythonhosted.org/packages/source/i/ipmi/ipmi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ipmi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ipmi
Summary:        A ipmi python client used in NetXMS migrated from perl
%description -n python3-ipmi

%prep
%global oreon_srcdir ipmi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ipmi usr/lib/python3*/site-packages/ipmi* usr/lib64/python3*/site-packages/ipmi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ipmi* usr/lib64/python3*/site-packages/ipmi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ipmi -f %{oreon_filedir}/python3-ipmi.list

%changelog

%autochangelog
