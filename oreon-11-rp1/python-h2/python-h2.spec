%global source0_hash 4e866ffb1a869ae14dd9b5e6beb5c24a13da0495ad72b65925ded182521c1516
Name:           python-h2
Version:        4.4.1
Release:        1%{?dist}
Summary:        Pure-Python HTTP/2 protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/h2/
Source0:        https://files.pythonhosted.org/packages/source/h/h2/h2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82
BuildRequires:  python3dist(wheel) >= 0.46.3
Requires:       python3-h2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-h2
Summary:        Pure-Python HTTP/2 protocol implementation
# oreon:reqs
Requires:       python3dist(hpack) < 5
Requires:       python3dist(hpack) >= 4.2
Requires:       python3dist(hyperframe) < 7
Requires:       python3dist(hyperframe) >= 6.1
# /oreon:reqs
%description -n python3-h2

%prep
%global oreon_srcdir h2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-h2 usr/lib/python3*/site-packages/h2* usr/lib64/python3*/site-packages/h2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/h2* usr/lib64/python3*/site-packages/h2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-h2 -f %{oreon_filedir}/python3-h2.list

%changelog

%autochangelog
