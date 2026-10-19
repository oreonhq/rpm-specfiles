%global source0_hash 324cba7513cd4187ee92b2eef21f071714e45be062458c8b157bd7e0c81103e3
Name:           python-rich-click
Version:        1.9.9
Release:        1%{?dist}
Summary:        Format click help output nicely with rich
License:        ...
URL:            https://github.com/ewels/rich-click
Source0:        https://files.pythonhosted.org/packages/source/r/rich_click/rich_click-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
Requires:       python3-rich-click = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rich-click
Summary:        Format click help output nicely with rich
# oreon:reqs
Requires:       python3dist(click) >= 8
Requires:       python3dist(rich) >= 12
Requires:       python3dist(typing-extensions) >= 4
# /oreon:reqs
%description -n python3-rich-click

%prep
%global oreon_srcdir rich_click-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rich-click usr/lib/python3*/site-packages/rich_click* usr/lib64/python3*/site-packages/rich_click* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rich_click* usr/lib64/python3*/site-packages/rich_click* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rich-click -f %{oreon_filedir}/python3-rich-click.list

%changelog

%autochangelog
