%global source0_hash 747dce5da58741af7e9336595bac1335b0632f64dfa1007ae9e9634fbad56678
Name:           python-pyone
Version:        7.3.80
Release:        1%{?dist}
Summary:        Python Bindings for OpenNebula XML-RPC API
License:        Apache-2.0
URL:            http://opennebula.io
Source0:        https://files.pythonhosted.org/packages/source/p/pyone/pyone-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyone = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyone+build
Summary:        Metapackage for python3-pyone build extras
Requires:       python3-pyone = %{version}-%{release}
Provides:       python3dist(pyone[build]) = %{version}-%{release}

%description -n python3-pyone+build
Metapackage for python3-pyone build extras.

%description

%package -n     python3-pyone
Summary:        Python Bindings for OpenNebula XML-RPC API
%description -n python3-pyone

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyone-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyone usr/lib/python3*/site-packages/pyone* usr/lib64/python3*/site-packages/pyone* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyone* usr/lib64/python3*/site-packages/pyone* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyone -f %{oreon_filedir}/python3-pyone.list

%changelog

%autochangelog
