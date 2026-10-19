%global source0_hash 3c78cec7c5a4abb4909a5252d66ab93e9b306b21ad86657e2c203c78b522431f
Name:           python-hacking
Version:        8.1.0
Release:        1%{?dist}
Summary:        OpenStack Hacking Guideline Enforcement
License:        Apache-2.0
URL:            https://docs.openstack.org/hacking/latest
Source0:        https://files.pythonhosted.org/packages/source/h/hacking/hacking-%{version}.tar.gz
BuildArch:      noarch
Patch1:         test-requirements.txt.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-hacking = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-hacking
Summary:        OpenStack Hacking Guideline Enforcement
%description -n python3-hacking

%prep
%global oreon_srcdir hacking-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hacking usr/lib/python3*/site-packages/hacking* usr/lib64/python3*/site-packages/hacking* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hacking* usr/lib64/python3*/site-packages/hacking* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hacking -f %{oreon_filedir}/python3-hacking.list

%changelog

%autochangelog
