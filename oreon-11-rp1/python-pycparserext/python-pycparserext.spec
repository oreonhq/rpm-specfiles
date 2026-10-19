%global source0_hash 33c9b724e7e78832075b3eb0d8569f5def5b9667944d22b6651d828796dc512a
Name:           python-pycparserext
Version:        2026.1
Release:        1%{?dist}
Summary:        Extensions for pycparser
License:        MIT
URL:            https://github.com/inducer/pycparserext
Source0:        https://files.pythonhosted.org/packages/source/p/pycparserext/pycparserext-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pycparserext = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pycparserext
Summary:        Extensions for pycparser
# oreon:reqs
Requires:       python3dist(pycparser) >= 3.0
# /oreon:reqs
%description -n python3-pycparserext

%prep
%global oreon_srcdir pycparserext-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pycparserext usr/lib/python3*/site-packages/pycparserext* usr/lib64/python3*/site-packages/pycparserext* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycparserext* usr/lib64/python3*/site-packages/pycparserext* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pycparserext -f %{oreon_filedir}/python3-pycparserext.list

%changelog

%autochangelog
