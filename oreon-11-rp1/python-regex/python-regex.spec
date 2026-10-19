%global source0_hash 1e321e2c84f0e52c457f5ea5944f796d6e8e09cb99738ea98dcc1bfe402a128d
Name:           python-regex
Version:        2026.9.10
Release:        1%{?dist}
Summary:        Alternative regular expression module, to replace re.
License:        Apache-2.0 AND CNRI-Python
URL:            https://github.com/mrabarnett/mrab-regex
Source0:        https://files.pythonhosted.org/packages/source/r/regex/regex-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) > 77.0.3
Requires:       python3-regex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-regex
Summary:        Alternative regular expression module, to replace re.
%description -n python3-regex

%prep
%global oreon_srcdir regex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-regex usr/lib/python3*/site-packages/regex* usr/lib64/python3*/site-packages/regex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/regex* usr/lib64/python3*/site-packages/regex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-regex -f %{oreon_filedir}/python3-regex.list

%changelog

%autochangelog
