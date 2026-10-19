%global source0_hash 006870b3b4e40547232ad12c3bb4faec91bbbe0659aafaa3b7fa48a112c4ee97
Name:           python-botocore
Version:        1.43.106
Release:        1%{?dist}
Summary:        Low-level, data-driven core of boto 3.
License:        Apache-2.0
URL:            https://github.com/boto/botocore
Source0:        https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-botocore = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-botocore
Summary:        Low-level, data-driven core of boto 3.
%description -n python3-botocore

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir botocore-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-botocore usr/lib/python3*/site-packages/botocore* usr/lib64/python3*/site-packages/botocore* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/botocore* usr/lib64/python3*/site-packages/botocore* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-botocore -f %{oreon_filedir}/python3-botocore.list

%changelog

%autochangelog
