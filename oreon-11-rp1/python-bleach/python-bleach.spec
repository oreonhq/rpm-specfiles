%global source0_hash 4202482733d85cedd04e59fcb2f89f4e4c7c385a78d3c3c23c30446843a37452
Name:           python-bleach
Version:        6.4.0
Release:        1%{?dist}
Summary:        An easy safelist-based HTML-sanitizing tool.
License:        ...
URL:            https://github.com/mozilla/bleach
Source0:        https://files.pythonhosted.org/packages/source/b/bleach/bleach-%{version}.tar.gz
BuildArch:      noarch
Patch:          Strip-leading-whitespaces-from-expected-values.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bleach = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bleach
Summary:        An easy safelist-based HTML-sanitizing tool.
%description -n python3-bleach

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir bleach-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bleach usr/lib/python3*/site-packages/bleach* usr/lib64/python3*/site-packages/bleach* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bleach* usr/lib64/python3*/site-packages/bleach* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bleach -f %{oreon_filedir}/python3-bleach.list

%changelog

%autochangelog
