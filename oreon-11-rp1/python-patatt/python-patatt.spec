%global source0_hash c226b5e7e449a4981b827c48e2586a928fa45b690af19a3892b9279b334f2551
Name:           python-patatt
Version:        0.8.0
Release:        1%{?dist}
Summary:        A simple library to add cryptographic attestation to patches sent via email
License:        MIT-0
URL:            https://git.kernel.org/pub/scm/utils/patatt/patatt.git/about/
Source0:        https://files.pythonhosted.org/packages/source/p/patatt/patatt-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-patatt = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-patatt
Summary:        A simple library to add cryptographic attestation to patches sent via email
# oreon:reqs
Requires:       python3dist(pynacl) < 2.0
Requires:       python3dist(pynacl) >= 1.5
# /oreon:reqs
%description -n python3-patatt

%prep
%global oreon_srcdir patatt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-patatt usr/lib/python3*/site-packages/patatt* usr/lib64/python3*/site-packages/patatt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/patatt* usr/lib64/python3*/site-packages/patatt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-patatt -f %{oreon_filedir}/python3-patatt.list

%changelog

%autochangelog
