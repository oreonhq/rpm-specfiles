%global source0_hash 7bce04c21c87c4eeca1db585cc2897c36f39ab66da52413b276e6d103dd8b76a
Name:           python-aiounifi
Version:        27
Release:        1%{?dist}
Summary:        An asynchronous Python library for communicating with Unifi Controller API
License:        MIT
URL:            https://github.com/Kane610/aiounifi
Source0:        https://files.pythonhosted.org/packages/source/a/aiounifi/aiounifi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aiounifi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aiounifi
Summary:        An asynchronous Python library for communicating with Unifi Controller API
%description -n python3-aiounifi

%prep
%global oreon_srcdir aiounifi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiounifi usr/lib/python3*/site-packages/aiounifi* usr/lib64/python3*/site-packages/aiounifi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiounifi* usr/lib64/python3*/site-packages/aiounifi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiounifi -f %{oreon_filedir}/python3-aiounifi.list

%changelog

%autochangelog
