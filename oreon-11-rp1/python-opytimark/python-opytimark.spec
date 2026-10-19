%global source0_hash 4daa13c3f8de6a6968411fbc32627c103edfa448042551914570e8ba7f762ae6
Name:           python-opytimark
Version:        3.0.2
Release:        1%{?dist}
Summary:        Python Optimization Benchmarking Functions
License:        Apache-2.0
URL:            https://github.com/gugarosa/opytimark
Source0:        https://files.pythonhosted.org/packages/source/o/opytimark/opytimark-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/2.patch
Patch:          %{url}/commit/7f5f97e9d042d9b9d9acf1cdcc9738fe99c792c5.patch
Patch:          %{url}/commit/25d9adb743c8483c0f2ae41f56c8872fdd44977f.patch
Patch:          %{url}/pull/4.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-opytimark = %{version}-%{release}
# /oreon:deps
%package -n       python3-opytimark+tests
Summary:        Metapackage for python3-opytimark tests extras
Requires:       python3-opytimark = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.10.0
Requires:       python3dist(flake8) >= 7.3.0
Requires:       python3dist(pytest) >= 9.0.0
Provides:       python3dist(opytimark[tests]) = %{version}-%{release}

%description -n python3-opytimark+tests
Metapackage for python3-opytimark tests extras.

%description

%package -n     python3-opytimark
Summary:        Python Optimization Benchmarking Functions
# oreon:reqs
Requires:       python3dist(numpy) >= 2.1.0
# /oreon:reqs
%description -n python3-opytimark

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir opytimark-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opytimark usr/lib/python3*/site-packages/opytimark* usr/lib64/python3*/site-packages/opytimark* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opytimark* usr/lib64/python3*/site-packages/opytimark* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-opytimark -f %{oreon_filedir}/python3-opytimark.list

%changelog

%autochangelog
