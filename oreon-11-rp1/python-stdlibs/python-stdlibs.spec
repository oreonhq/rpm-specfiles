%global source0_hash 0da5ac692879757df75fd944ebabfae11b2d6454a2643658699a1c0a1f4bb91a
Name:           python-stdlibs
Version:        2026.9.3
Release:        1%{?dist}
Summary:        List of packages in the stdlib
License:        MIT
URL:            https://stdlibs.omnilib.dev
Source0:        https://files.pythonhosted.org/packages/source/s/stdlibs/stdlibs-%{version}.tar.gz
BuildArch:      noarch
Patch:          stdlibs-use-tomllib.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 4
Requires:       python3-stdlibs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-stdlibs
Summary:        List of packages in the stdlib
%description -n python3-stdlibs

%prep
%global oreon_srcdir stdlibs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stdlibs usr/lib/python3*/site-packages/stdlibs* usr/lib64/python3*/site-packages/stdlibs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stdlibs* usr/lib64/python3*/site-packages/stdlibs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-stdlibs -f %{oreon_filedir}/python3-stdlibs.list

%changelog

%autochangelog
