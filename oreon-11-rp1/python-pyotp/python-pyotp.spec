%global source0_hash d01e9703443616b03c57c700b5cbffd56a1f929c1b0f8f03131bc78c1fca9d3f
Name:           python-pyotp
Version:        2.10.0
Release:        1%{?dist}
Summary:        Python One Time Password Library
License:        MIT
URL:            https://github.com/pyauth/pyotp
Source0:        https://files.pythonhosted.org/packages/source/p/pyotp/pyotp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyotp = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyotp+test
Summary:        Metapackage for python3-pyotp test extras
Requires:       python3-pyotp = %{version}-%{release}
Provides:       python3dist(pyotp[test]) = %{version}-%{release}

%description -n python3-pyotp+test
Metapackage for python3-pyotp test extras.

%description

%package -n     python3-pyotp
Summary:        Python One Time Password Library
%description -n python3-pyotp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyotp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyotp usr/lib/python3*/site-packages/pyotp* usr/lib64/python3*/site-packages/pyotp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyotp* usr/lib64/python3*/site-packages/pyotp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyotp -f %{oreon_filedir}/python3-pyotp.list

%changelog

%autochangelog
