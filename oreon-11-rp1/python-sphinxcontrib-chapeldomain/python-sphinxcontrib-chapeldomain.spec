%global source0_hash 07b71391e28664e5ed47aef25d7852e3d15a311d1c4cd63e971e493e379e47c2
Name:           python-sphinxcontrib-chapeldomain
Version:        0.0.41
Release:        1%{?dist}
Summary:        Chapel domain for Sphinx
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/chapel-lang/sphinxcontrib-chapeldomain
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_chapeldomain/sphinxcontrib_chapeldomain-%{version}.tar.gz
BuildArch:      noarch
Patch:          relax-dep-requirements.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinxcontrib-chapeldomain = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinxcontrib-chapeldomain
Summary:        Chapel domain for Sphinx
%description -n python3-sphinxcontrib-chapeldomain

%prep
%global oreon_srcdir sphinxcontrib_chapeldomain-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-chapeldomain usr/lib/python3*/site-packages/sphinxcontrib_chapeldomain* usr/lib64/python3*/site-packages/sphinxcontrib_chapeldomain* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_chapeldomain* usr/lib64/python3*/site-packages/sphinxcontrib_chapeldomain* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinxcontrib-chapeldomain -f %{oreon_filedir}/python3-sphinxcontrib-chapeldomain.list

%changelog

%autochangelog
