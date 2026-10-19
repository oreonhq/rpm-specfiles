%global source0_hash 52d920e50eaa76eb065b20bfd4e42f72195e894a079098dacc1cafa908cd4b83
Name:           python-fitdecode
Version:        0.11.0
Release:        1%{?dist}
Summary:        FIT file parser and decoder
License:        MIT
URL:            https://github.com/polyvertex/fitdecode
Source0:        https://files.pythonhosted.org/packages/source/f/fitdecode/fitdecode-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-fitdecode = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fitdecode
Summary:        FIT file parser and decoder
%description -n python3-fitdecode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fitdecode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fitdecode usr/lib/python3*/site-packages/fitdecode* usr/lib64/python3*/site-packages/fitdecode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fitdecode* usr/lib64/python3*/site-packages/fitdecode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fitdecode -f %{oreon_filedir}/python3-fitdecode.list

%changelog

%autochangelog
