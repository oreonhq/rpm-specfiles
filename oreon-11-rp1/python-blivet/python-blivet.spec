%global source0_hash db2cd996ed354d47fdc60740d912a102250a0fc469bfe17df6bced649c172e5b
Name:           python-blivet
Version:        3.14.2
Release:        1%{?dist}
Summary:        Python module for system storage configuration
License:        GPL-2.0-or-later
URL:            https://github.com/storaged-project/blivet
Source0:        https://files.pythonhosted.org/packages/source/b/blivet/blivet-%{version}.tar.gz
BuildArch:      noarch
Patch0:        0001-remove-btrfs-plugin.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-blivet = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-blivet
Summary:        Python module for system storage configuration
%description -n python3-blivet

%prep
%global oreon_srcdir blivet-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blivet usr/lib/python3*/site-packages/blivet* usr/lib64/python3*/site-packages/blivet* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blivet* usr/lib64/python3*/site-packages/blivet* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-blivet -f %{oreon_filedir}/python3-blivet.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.13.2-2
- Import
