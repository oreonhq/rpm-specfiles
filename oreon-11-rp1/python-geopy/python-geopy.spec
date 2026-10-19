%global source0_hash 7b6c849f18108dcce4faa3d614e2801107b465f7b05fd3c1db9db12e225ae950
Name:           python-geopy
Version:        2.5.0
Release:        1%{?dist}
Summary:        Python Geocoding Toolbox
License:        MIT
URL:            https://github.com/geopy/geopy
Source0:        https://files.pythonhosted.org/packages/source/g/geopy/geopy-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Downstream-only-drop-coverage-from-test-extra.patch
Patch:          0002-Downstream-only-allow-newer-Sphinx-for-testing.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-geopy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-geopy
Summary:        Python Geocoding Toolbox
%description -n python3-geopy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir geopy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-geopy usr/lib/python3*/site-packages/geopy* usr/lib64/python3*/site-packages/geopy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/geopy* usr/lib64/python3*/site-packages/geopy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-geopy -f %{oreon_filedir}/python3-geopy.list

%changelog

%autochangelog
