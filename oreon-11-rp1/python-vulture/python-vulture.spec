%global source0_hash f8d9f6e2af03011664a3c6c240c9765b3f392917d3135fddca6d6a68d359f717
Name:           python-vulture
Version:        2.16
Release:        1%{?dist}
Summary:        Find dead code
License:        MIT
URL:            https://github.com/jendrikseipp/vulture
Source0:        https://files.pythonhosted.org/packages/source/v/vulture/vulture-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68
Requires:       python3-vulture = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-vulture
Summary:        Find dead code
# oreon:reqs
Requires:       python3dist(tomli) >= 1.1.0
# /oreon:reqs
%description -n python3-vulture

%prep
%global oreon_srcdir vulture-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-vulture usr/lib/python3*/site-packages/vulture* usr/lib64/python3*/site-packages/vulture* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/vulture* usr/lib64/python3*/site-packages/vulture* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-vulture -f %{oreon_filedir}/python3-vulture.list

%changelog

%autochangelog
