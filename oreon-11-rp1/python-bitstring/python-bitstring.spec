%global source0_hash e682ac522bb63e041d16cbc9d0ca86a4f00194db16d0847c7efe066f836b2e37
Name:           python-bitstring
Version:        4.4.0
Release:        1%{?dist}
Summary:        Simple construction, analysis and modification of binary data.
License:        MIT
URL:            https://github.com/scott-griffiths/bitstring
Source0:        https://files.pythonhosted.org/packages/source/b/bitstring/bitstring-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-bitstring = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bitstring
Summary:        Simple construction, analysis and modification of binary data.
# oreon:reqs
Requires:       python3dist(bitarray) < 4.0
Requires:       python3dist(bitarray) >= 3.0.0
Requires:       python3dist(tibs) < 0.6
Requires:       python3dist(tibs) >= 0.5.6
# /oreon:reqs
%description -n python3-bitstring

%prep
%global oreon_srcdir bitstring-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bitstring usr/lib/python3*/site-packages/bitstring* usr/lib64/python3*/site-packages/bitstring* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bitstring* usr/lib64/python3*/site-packages/bitstring* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bitstring -f %{oreon_filedir}/python3-bitstring.list

%changelog

%autochangelog
