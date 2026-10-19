%global source0_hash eaaac4c9fdd5e9e8852dc778d2d7405897ec510f2a298071453e5e3a07914bb1
Name:           python-parso
Version:        0.8.7
Release:        1%{?dist}
Summary:        A Python Parser
License:        MIT
URL:            https://github.com/davidhalter/parso
Source0:        https://files.pythonhosted.org/packages/source/p/parso/parso-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-parso = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-parso
Summary:        A Python Parser
%description -n python3-parso

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir parso-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-parso usr/lib/python3*/site-packages/parso* usr/lib64/python3*/site-packages/parso* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/parso* usr/lib64/python3*/site-packages/parso* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-parso -f %{oreon_filedir}/python3-parso.list

%changelog

%autochangelog
