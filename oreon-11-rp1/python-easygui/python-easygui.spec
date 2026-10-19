%global source0_hash d653ff79ee1f42f63b5a090f2f98ce02335d86ad8963b3ce2661805cafe99a04
Name:           python-easygui
Version:        0.98.3
Release:        1%{?dist}
Summary:        EasyGUI is a module for very simple, very easy GUI programming in Python.  EasyGUI is different from other GUI generators in that EasyGUI is NOT event-driven.  Instead, all GUI interactions are invoked by simple function calls.
License:        ...
URL:            https://github.com/robertlugg/easygui
Source0:        https://files.pythonhosted.org/packages/source/e/easygui/easygui-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-easygui = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-easygui
Summary:        EasyGUI is a module for very simple, very easy GUI programming in Python.  EasyGUI is different from other GUI generators in that EasyGUI is NOT event-driven.  Instead, all GUI interactions are invoked by simple function calls.
%description -n python3-easygui

%prep
%global oreon_srcdir easygui-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-easygui usr/lib/python3*/site-packages/easygui* usr/lib64/python3*/site-packages/easygui* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/easygui* usr/lib64/python3*/site-packages/easygui* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-easygui -f %{oreon_filedir}/python3-easygui.list

%changelog

%autochangelog
