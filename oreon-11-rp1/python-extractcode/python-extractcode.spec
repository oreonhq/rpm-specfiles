%global source0_hash e62b75ecf0379beea79cd54d5f1341ac05ec39974e5695ad21d0abb86a0ab6a4
Name:           python-extractcode
Version:        31.1.0
Release:        1%{?dist}
Summary:        A mostly universal archive extractor using 7zip, libarchive and the Python standard library for reliable archive extraction.
License:        Apache-2.0
URL:            https://github.com/nexB/extractcode
Source0:        https://files.pythonhosted.org/packages/source/e/extractcode/extractcode-%{version}.tar.gz
BuildArch:      noarch
Patch:          %url/commit/6270a8805c7fb964e545a56ca8a92829d240a96a.patch#/0001-Add-COC-to-redistributed-license-like-files.patch
Patch:          %url/pull/55.patch#/0001-Use-patch-ng-fork-instead-of-unmaintained-patch.patch
Patch:          %url/pull/56.patch#/0001-Usage-of-dash-separated-console-scripts-is-deprecate.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 50
Requires:       python3-extractcode = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-extractcode
Summary:        A mostly universal archive extractor using 7zip, libarchive and the Python standard library for reliable archive extraction.
%description -n python3-extractcode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir extractcode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-extractcode usr/lib/python3*/site-packages/extractcode* usr/lib64/python3*/site-packages/extractcode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/extractcode* usr/lib64/python3*/site-packages/extractcode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-extractcode -f %{oreon_filedir}/python3-extractcode.list

%changelog

%autochangelog
