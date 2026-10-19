%global source0_hash 64f60f7a0d15c85876b76b5f79246ed8c27bf5f79e5753ec88287145884661ab
Name:           python-ifcfg
Version:        0.24
Release:        1%{?dist}
Summary:        Python ifconfig wrapper for Unix/Linux/MacOSX + ipconfig for Windows
License:        ...
URL:            https://github.com/ftao/python-ifcfg
Source0:        https://files.pythonhosted.org/packages/source/i/ifcfg/ifcfg-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-0.21-drop-nose.patch
Patch1:         %{name}-rm-python-mock-usage.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ifcfg = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ifcfg
Summary:        Python ifconfig wrapper for Unix/Linux/MacOSX + ipconfig for Windows
%description -n python3-ifcfg

%prep
%global oreon_srcdir ifcfg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ifcfg usr/lib/python3*/site-packages/ifcfg* usr/lib64/python3*/site-packages/ifcfg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ifcfg* usr/lib64/python3*/site-packages/ifcfg* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ifcfg -f %{oreon_filedir}/python3-ifcfg.list

%changelog

%autochangelog
