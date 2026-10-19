%global source0_hash 00d3aa24bfedff9420b2e0d5d9f5ab6d9d4268e72afbf59bb3fa542781d5218e
Name:           python-yapf
Version:        0.43.0
Release:        1%{?dist}
Summary:        A formatter for Python code
License:        ...
URL:            https://github.com/google/yapf
Source0:        https://files.pythonhosted.org/packages/source/y/yapf/yapf-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix_installed_modules.patch
Patch:          fix_tox_requirements.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 58.5.0
Requires:       python3-yapf = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-yapf
Summary:        A formatter for Python code
# oreon:reqs
Requires:       python3dist(platformdirs) >= 3.5.1
Requires:       python3dist(tomli) >= 2.0.1
# /oreon:reqs
%description -n python3-yapf

%prep
%global oreon_srcdir yapf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-yapf usr/lib/python3*/site-packages/yapf* usr/lib64/python3*/site-packages/yapf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/yapf* usr/lib64/python3*/site-packages/yapf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-yapf -f %{oreon_filedir}/python3-yapf.list

%changelog

%autochangelog
