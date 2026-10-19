%global source0_hash d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32
Name:           python-attrs
Version:        26.1.0
Release:        1%{?dist}
Summary:        Classes Without Boilerplate
License:        MIT
URL:            https://github.com/python-attrs/attrs
Source0:        https://files.pythonhosted.org/packages/source/a/attrs/attrs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-fancy-pypi-readme) >= 23.2.0
Requires:       python3-attrs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-attrs
Summary:        Classes Without Boilerplate
%description -n python3-attrs

%prep
%global oreon_srcdir attrs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-attrs usr/lib/python3*/site-packages/attrs* usr/lib64/python3*/site-packages/attrs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/attrs* usr/lib64/python3*/site-packages/attrs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-attrs -f %{oreon_filedir}/python3-attrs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.4.0-1
- Prepare for Oreon 11 (RP1)
