%global source0_hash 650ca73b28e64d46a198e3d7ea3f7ee79bfd0404a3030d057addd11e79ef80e3
Name:           python-fastpurge
Version:        1.0.6
Release:        1%{?dist}
Summary:        A client for the Akamai Fast Purge API
License:        GPL-3.0-or-later
URL:            https://release-engineering.github.io/python-fastpurge/
Source0:        https://files.pythonhosted.org/packages/source/f/fastpurge/fastpurge-%{version}.tar.gz
BuildArch:      noarch
Patch: 0001-Use-unittest.mock-on-Python-3.3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastpurge = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fastpurge
Summary:        A client for the Akamai Fast Purge API
%description -n python3-fastpurge

%prep
%global oreon_srcdir fastpurge-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastpurge usr/lib/python3*/site-packages/fastpurge* usr/lib64/python3*/site-packages/fastpurge* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastpurge* usr/lib64/python3*/site-packages/fastpurge* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastpurge -f %{oreon_filedir}/python3-fastpurge.list

%changelog

%autochangelog
