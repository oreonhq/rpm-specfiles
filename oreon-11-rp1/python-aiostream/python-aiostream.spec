%global source0_hash 32d180b4ab01ebb2fc59eda7fa59f496895a4d07b32fc57537d1dade2514a8a1
Name:           python-aiostream
Version:        0.8.1
Release:        1%{?dist}
Summary:        Generator-based operators for asynchronous iteration
License:        GPL-3.0-or-later
URL:            https://github.com/vxgmichel/aiostream
Source0:        https://files.pythonhosted.org/packages/source/a/aiostream/aiostream-%{version}.tar.gz
BuildArch:      noarch
Patch0:         require-lower-setuptools-version.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 69.5
Requires:       python3-aiostream = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aiostream
Summary:        Generator-based operators for asynchronous iteration
%description -n python3-aiostream

%prep
%global oreon_srcdir aiostream-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiostream usr/lib/python3*/site-packages/aiostream* usr/lib64/python3*/site-packages/aiostream* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiostream* usr/lib64/python3*/site-packages/aiostream* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiostream -f %{oreon_filedir}/python3-aiostream.list

%changelog

%autochangelog
