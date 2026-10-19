%global source0_hash d6b7f0737a732c54c92b271f2932c91e386238c8b6ded49d4180eed44eb50684
Name:           python-colored
Version:        2.3.2
Release:        1%{?dist}
Summary:        Simple python library for color and formatting to terminal
License:        MIT
URL:            https://dslackw.gitlab.io/colored/
Source0:        https://files.pythonhosted.org/packages/source/c/colored/colored-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.10.1
Requires:       python3-colored = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colored
Summary:        Simple python library for color and formatting to terminal
%description -n python3-colored

%prep
%global oreon_srcdir colored-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colored usr/lib/python3*/site-packages/colored* usr/lib64/python3*/site-packages/colored* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colored* usr/lib64/python3*/site-packages/colored* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colored -f %{oreon_filedir}/python3-colored.list

%changelog

%autochangelog
