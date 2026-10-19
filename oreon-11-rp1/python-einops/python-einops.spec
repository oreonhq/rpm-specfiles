%global source0_hash 609da665570e5e265e27283aab09e7f279ade90c4f01bcfca111f3d3e13f2827
Name:           python-einops
Version:        0.8.2
Release:        1%{?dist}
Summary:        A new flavour of deep learning operations
License:        MIT
URL:            https://github.com/arogozhnikov/einops
Source0:        https://files.pythonhosted.org/packages/source/e/einops/einops-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.10.0
Requires:       python3-einops = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-einops
Summary:        A new flavour of deep learning operations
%description -n python3-einops

%prep
%global oreon_srcdir einops-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-einops usr/lib/python3*/site-packages/einops* usr/lib64/python3*/site-packages/einops* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/einops* usr/lib64/python3*/site-packages/einops* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-einops -f %{oreon_filedir}/python3-einops.list

%changelog

%autochangelog
