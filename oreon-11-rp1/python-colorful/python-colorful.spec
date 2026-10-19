%global source0_hash bb16502b198be2f1c42ba3c52c703d5f651d826076817185f0294c1a549a7445
Name:           python-colorful
Version:        0.5.8
Release:        1%{?dist}
Summary:        Terminal string styling done right, in Python.
License:        MIT
URL:            http://github.com/timofurrer/colorful
Source0:        https://files.pythonhosted.org/packages/source/c/colorful/colorful-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colorful = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colorful
Summary:        Terminal string styling done right, in Python.
%description -n python3-colorful

%prep
%global oreon_srcdir colorful-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colorful usr/lib/python3*/site-packages/colorful* usr/lib64/python3*/site-packages/colorful* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colorful* usr/lib64/python3*/site-packages/colorful* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colorful -f %{oreon_filedir}/python3-colorful.list

%changelog

%autochangelog
