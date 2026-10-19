%global source0_hash 72d2fda61b23babe862018729be73c8b0dc12e3e6601f36f6e65d905e249f4db
Name:           python-jellyfish
Version:        1.2.1
Release:        1%{?dist}
Summary:        ...
License:        MIT
URL:            https://jellyfish.jpt.sh/
Source0:        https://files.pythonhosted.org/packages/source/j/jellyfish/jellyfish-%{version}.tar.gz
Patch0:         fix-build.patch
Patch1:         test-only-python-implementation.diff
Patch2:         nocimplementation-fix-0.9.1.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 0.14
Requires:       python3-jellyfish = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jellyfish
Summary:        ...
%description -n python3-jellyfish

%prep
%global oreon_srcdir jellyfish-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jellyfish usr/lib/python3*/site-packages/jellyfish* usr/lib64/python3*/site-packages/jellyfish* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jellyfish* usr/lib64/python3*/site-packages/jellyfish* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jellyfish -f %{oreon_filedir}/python3-jellyfish.list

%changelog

%autochangelog
