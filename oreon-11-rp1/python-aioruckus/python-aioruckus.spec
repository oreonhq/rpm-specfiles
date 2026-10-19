%global source0_hash fe3697ad9364344384485202b2dae373d5e8bf499d4bff674d12fa8397d53893
Name:           python-aioruckus
Version:        0.49
Release:        1%{?dist}
Summary:        Python API to interact with Ruckus Unleashed and ZoneDirector devices
License:        0BSD
URL:            https://github.com/ms264556/aioruckus
Source0:        https://files.pythonhosted.org/packages/source/a/aioruckus/aioruckus-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aioruckus = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aioruckus
Summary:        Python API to interact with Ruckus Unleashed and ZoneDirector devices
# oreon:reqs
Requires:       python3dist(aiohttp) >= 3.14.3
Requires:       python3dist(aiohttp) >= 3.9.5
Requires:       python3dist(cryptography) >= 41.0.7
Requires:       python3dist(cryptography) >= 48.0.1
Requires:       python3dist(typing-extensions) >= 4.5.0
Requires:       python3dist(xmltodict) >= 0.13.0
Requires:       python3dist(xmltodict) >= 1.0.4
# /oreon:reqs
%description -n python3-aioruckus

%prep
%global oreon_srcdir aioruckus-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aioruckus usr/lib/python3*/site-packages/aioruckus* usr/lib64/python3*/site-packages/aioruckus* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aioruckus* usr/lib64/python3*/site-packages/aioruckus* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aioruckus -f %{oreon_filedir}/python3-aioruckus.list

%changelog

%autochangelog
