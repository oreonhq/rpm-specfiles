%global source0_hash 8809a4df6fe08279b39a8890669506ed3158e0617855ac9aff098fcbe772ae4c
Name:           python-pyproject-metadata
Version:        0.12.1
Release:        1%{?dist}
Summary:        PEP 621 metadata parsing
License:        MIT
URL:            https://github.com/pypa/pyproject-metadata
Source0:        https://files.pythonhosted.org/packages/source/p/pyproject_metadata/pyproject_metadata-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-pyproject-metadata = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyproject-metadata
Summary:        PEP 621 metadata parsing
# oreon:reqs
Requires:       python3dist(packaging) >= 23.2
# /oreon:reqs
%description -n python3-pyproject-metadata

%prep
%global oreon_srcdir pyproject_metadata-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyproject-metadata usr/lib/python3*/site-packages/pyproject_metadata* usr/lib64/python3*/site-packages/pyproject_metadata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyproject_metadata* usr/lib64/python3*/site-packages/pyproject_metadata* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyproject-metadata -f %{oreon_filedir}/python3-pyproject-metadata.list

%changelog

%autochangelog
