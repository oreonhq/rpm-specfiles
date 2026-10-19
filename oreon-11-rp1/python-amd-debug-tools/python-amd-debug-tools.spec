%global source0_hash 1fde40c0ab168ae387463e4ca310b62958498d74d14e20f20e3fc61c134839ef
Name:           python-amd-debug-tools
Version:        0.2.21
Release:        1%{?dist}
Summary:        debug tools for AMD systems
License:        MIT
URL:            https://web.git.kernel.org/pub/scm/linux/kernel/git/superm1/amd-debug-tools.git/
Source0:        https://files.pythonhosted.org/packages/source/a/amd_debug_tools/amd_debug_tools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-amd-debug-tools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-amd-debug-tools
Summary:        debug tools for AMD systems
%description -n python3-amd-debug-tools

%prep
%global oreon_srcdir amd_debug_tools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-amd-debug-tools usr/lib/python3*/site-packages/amd_debug_tools* usr/lib64/python3*/site-packages/amd_debug_tools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/amd_debug_tools* usr/lib64/python3*/site-packages/amd_debug_tools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-amd-debug-tools -f %{oreon_filedir}/python3-amd-debug-tools.list

%changelog

%autochangelog
