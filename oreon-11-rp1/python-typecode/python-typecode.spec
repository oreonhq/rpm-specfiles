%global source0_hash 42b9477d7d05ba5668768dae46c2d2700d503b6e3791d2cd8003b5d10d0ea330
Name:           python-typecode
Version:        30.2.0
Release:        1%{?dist}
Summary:        Comprehensive filetype and mimetype detection using libmagic and Pygments.
License:        Apache-2.0
URL:            https://github.com/aboutcode-org/typecode
Source0:        https://files.pythonhosted.org/packages/source/t/typecode/typecode-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 50
Requires:       python3-typecode = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-typecode
Summary:        Comprehensive filetype and mimetype detection using libmagic and Pygments.
%description -n python3-typecode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir typecode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-typecode usr/lib/python3*/site-packages/typecode* usr/lib64/python3*/site-packages/typecode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/typecode* usr/lib64/python3*/site-packages/typecode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-typecode -f %{oreon_filedir}/python3-typecode.list

%changelog

%autochangelog
