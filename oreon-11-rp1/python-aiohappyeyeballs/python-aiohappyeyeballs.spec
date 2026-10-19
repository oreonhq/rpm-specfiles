%global source0_hash 065665c041c42a5938ed220bdcd7230f22527fbec085e1853d2402c8a3615d9d
Name:           python-aiohappyeyeballs
Version:        2.7.1
Release:        1%{?dist}
Summary:        Happy Eyeballs for asyncio
License:        PSF-2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
Source0:        https://files.pythonhosted.org/packages/source/a/aiohappyeyeballs/aiohappyeyeballs-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Downstream-only-remove-pytest-options-for-coverage-a.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.0.0
Requires:       python3-aiohappyeyeballs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aiohappyeyeballs
Summary:        Happy Eyeballs for asyncio
%description -n python3-aiohappyeyeballs

%prep
%global oreon_srcdir aiohappyeyeballs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiohappyeyeballs usr/lib/python3*/site-packages/aiohappyeyeballs* usr/lib64/python3*/site-packages/aiohappyeyeballs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiohappyeyeballs* usr/lib64/python3*/site-packages/aiohappyeyeballs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiohappyeyeballs -f %{oreon_filedir}/python3-aiohappyeyeballs.list

%changelog

%autochangelog
