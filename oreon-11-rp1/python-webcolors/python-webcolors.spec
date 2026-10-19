%global source0_hash 62abae86504f66d0f6364c2a8520de4a0c47b80c03fc3a5f1815fedbef7c19bf
Name:           python-webcolors
Version:        25.10.0
Release:        1%{?dist}
Summary:        A library for working with the color formats defined by HTML and CSS.
License:        BSD-3-Clause
URL:            https://github.com/ubernostrum/webcolors
Source0:        https://files.pythonhosted.org/packages/source/w/webcolors/webcolors-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-webcolors = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-webcolors
Summary:        A library for working with the color formats defined by HTML and CSS.
%description -n python3-webcolors

%prep
%global oreon_srcdir webcolors-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-webcolors usr/lib/python3*/site-packages/webcolors* usr/lib64/python3*/site-packages/webcolors* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/webcolors* usr/lib64/python3*/site-packages/webcolors* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-webcolors -f %{oreon_filedir}/python3-webcolors.list

%changelog

%autochangelog
