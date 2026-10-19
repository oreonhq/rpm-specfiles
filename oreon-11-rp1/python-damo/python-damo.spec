%global source0_hash ddb1a700281fff96a96190a152764cf006eca0239ad5f348f38c4e0e718a57d7
Name:           python-damo
Version:        3.4.1
Release:        1%{?dist}
Summary:        DAMON user-space tool
License:        ...
URL:            https://github.com/damonitor/damo/issues
Source0:        https://files.pythonhosted.org/packages/source/d/damo/damo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-damo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-damo
Summary:        DAMON user-space tool
%description -n python3-damo

%prep
%global oreon_srcdir damo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-damo usr/lib/python3*/site-packages/damo* usr/lib64/python3*/site-packages/damo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/damo* usr/lib64/python3*/site-packages/damo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-damo -f %{oreon_filedir}/python3-damo.list

%changelog

%autochangelog
