%global source0_hash d896b5df877c9ca5eeddbf0e5994124694d6cb535aba698fb23344c7025155a1
Name:           python-multitasking
Version:        0.0.13
Release:        1%{?dist}
Summary:        Non-blocking Python methods using decorators
License:        ...
URL:            https://github.com/ranaroussi/multitasking
Source0:        https://files.pythonhosted.org/packages/source/m/multitasking/multitasking-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-multitasking = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-multitasking
Summary:        Non-blocking Python methods using decorators
%description -n python3-multitasking

%prep
%global oreon_srcdir multitasking-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-multitasking usr/lib/python3*/site-packages/multitasking* usr/lib64/python3*/site-packages/multitasking* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/multitasking* usr/lib64/python3*/site-packages/multitasking* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-multitasking -f %{oreon_filedir}/python3-multitasking.list

%changelog

%autochangelog
