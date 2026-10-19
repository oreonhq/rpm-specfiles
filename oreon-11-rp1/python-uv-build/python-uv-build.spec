%global source0_hash 32ca6fb8d5223c51c72bb09d6f52b6730406ded06ad17711ea2fef8bff260c62
Name:           python-uv-build
Version:        0.12.16
Release:        1%{?dist}
Summary:        The uv build backend
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/uv
Source0:        https://files.pythonhosted.org/packages/source/u/uv_build/uv_build-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-uv-build = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-uv-build
Summary:        The uv build backend
%description -n python3-uv-build

%prep
%global oreon_srcdir uv_build-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-uv-build usr/lib/python3*/site-packages/uv_build* usr/lib64/python3*/site-packages/uv_build* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uv_build* usr/lib64/python3*/site-packages/uv_build* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-uv-build -f %{oreon_filedir}/python3-uv-build.list

%changelog

%autochangelog
