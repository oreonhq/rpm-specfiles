%global source0_hash e567b55d169211d4d499c73307350da15df5d38248e60bae559609570c42ef55
Name:           python-iso3166
Version:        3.0.0
Release:        1%{?dist}
Summary:        Self-contained ISO 3166-1 country definitions.
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/i/iso3166/iso3166-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13.0
BuildRequires:  python3dist(uv-build) >= 0.12.5
Requires:       python3-iso3166 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-iso3166
Summary:        Self-contained ISO 3166-1 country definitions.
%description -n python3-iso3166

%prep
%global oreon_srcdir iso3166-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-iso3166 usr/lib/python3*/site-packages/iso3166* usr/lib64/python3*/site-packages/iso3166* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/iso3166* usr/lib64/python3*/site-packages/iso3166* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-iso3166 -f %{oreon_filedir}/python3-iso3166.list

%changelog

%autochangelog
