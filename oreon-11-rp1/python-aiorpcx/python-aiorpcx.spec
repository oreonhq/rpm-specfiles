%global source0_hash 940fa250ea5e9fd372d4c6acdc20dcb603bd1960ca324759d29864a4aaf64570
Name:           python-aiorpcx
Version:        0.25.0
Release:        1%{?dist}
Summary:        Generic async RPC implementation, including JSON-RPC
License:        MIT
URL:            https://github.com/kyuupichan/aiorpcX
Source0:        https://files.pythonhosted.org/packages/source/a/aiorpcx/aiorpcx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aiorpcx = %{version}-%{release}
# /oreon:deps
%package -n       python3-aiorpcx+ws
Summary:        Metapackage for python3-aiorpcx ws extras
Requires:       python3-aiorpcx = %{version}-%{release}
Requires:       python3dist(websockets) >= 14.0
Provides:       python3dist(aiorpcx[ws]) = %{version}-%{release}

%description -n python3-aiorpcx+ws
Metapackage for python3-aiorpcx ws extras.

%description

%package -n     python3-aiorpcx
Summary:        Generic async RPC implementation, including JSON-RPC
%description -n python3-aiorpcx

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir aiorpcx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiorpcx usr/lib/python3*/site-packages/aiorpcx* usr/lib64/python3*/site-packages/aiorpcx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiorpcx* usr/lib64/python3*/site-packages/aiorpcx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiorpcx -f %{oreon_filedir}/python3-aiorpcx.list

%changelog

%autochangelog
