%global source0_hash 6940ccd06f435b44a0d27864359eda9c8c3e4c5ceaf8f43cf994280796f3296c
Name:           python-drgn
Version:        0.2.0
Release:        1%{?dist}
Summary:        Programmable debugger
License:        LGPL-2.1-or-later
URL:            https://github.com/osandov/drgn/issues
Source0:        https://files.pythonhosted.org/packages/source/d/drgn/drgn-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-drgn = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-drgn
Summary:        Programmable debugger
%description -n python3-drgn

%prep
%global oreon_srcdir drgn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-drgn usr/lib/python3*/site-packages/drgn* usr/lib64/python3*/site-packages/drgn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/drgn* usr/lib64/python3*/site-packages/drgn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-drgn -f %{oreon_filedir}/python3-drgn.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.0-1
- Prepare for Oreon 11 (RP1)
