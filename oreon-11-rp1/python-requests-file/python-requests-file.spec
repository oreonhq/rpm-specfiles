%global source0_hash f14243d7796c588f3521bd423c5dea2ee4cc730e54a3cac9574d78aca1272576
Name:           python-requests-file
Version:        3.0.1
Release:        1%{?dist}
Summary:        File transport adapter for Requests
License:        ...
URL:            https://codeberg.org/dashea/requests-file
Source0:        https://files.pythonhosted.org/packages/source/r/requests_file/requests_file-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-requests-file = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-requests-file
Summary:        File transport adapter for Requests
# oreon:reqs
Requires:       python3dist(requests) >= 1.0.0
# /oreon:reqs
%description -n python3-requests-file

%prep
%global oreon_srcdir requests_file-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-file usr/lib/python3*/site-packages/requests_file* usr/lib64/python3*/site-packages/requests_file* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_file* usr/lib64/python3*/site-packages/requests_file* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-requests-file -f %{oreon_filedir}/python3-requests-file.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-2
- Prepare for Oreon 11 (RP1)
