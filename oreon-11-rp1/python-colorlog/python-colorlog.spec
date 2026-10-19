%global source0_hash 2a7924c1dadf18b22a0eb8b06d1c7b01d5341707ec1641eb6fcc4fde0c3e8e5f
Name:           python-colorlog
Version:        6.12.0
Release:        1%{?dist}
Summary:        Add colours to the output of Python_s logging module.
License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source0:        https://files.pythonhosted.org/packages/source/c/colorlog/colorlog-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colorlog = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colorlog
Summary:        Add colours to the output of Python_s logging module.
%description -n python3-colorlog

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colorlog-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colorlog usr/lib/python3*/site-packages/colorlog* usr/lib64/python3*/site-packages/colorlog* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colorlog* usr/lib64/python3*/site-packages/colorlog* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colorlog -f %{oreon_filedir}/python3-colorlog.list

%changelog

%autochangelog
