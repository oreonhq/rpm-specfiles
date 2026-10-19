%global source0_hash 0236b0567513356e7b1679d20f1eba704d18221347a355b4bfde6b1385f31b66
Name:           python-justbases
Version:        0.15.3
Release:        1%{?dist}
Summary:        conversion of ints and rationals to any base
License:        LGPL-2.1-or-later
URL:            https://github.com/mulkieran/justbases
Source0:        https://files.pythonhosted.org/packages/source/j/justbases/justbases-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-justbases = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-justbases
Summary:        conversion of ints and rationals to any base
%description -n python3-justbases

%prep
%global oreon_srcdir justbases-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-justbases usr/lib/python3*/site-packages/justbases* usr/lib64/python3*/site-packages/justbases* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/justbases* usr/lib64/python3*/site-packages/justbases* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-justbases -f %{oreon_filedir}/python3-justbases.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.2-1
- Prepare for Oreon 11 (RP1)
