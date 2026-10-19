%global source0_hash aabfd6a328926703d76e24f8913d8c7b4df4c04a487c2eb493a214999abdb8aa
Name:           python-contextualbandits
Version:        0.3.30
Release:        1%{?dist}
Summary:        Python Implementations of Algorithms for Contextual Bandits
License:        ...
URL:            https://github.com/david-cortes/contextualbandits
Source0:        https://files.pythonhosted.org/packages/source/c/contextualbandits/contextualbandits-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1.0
BuildRequires:  python3dist(numpy) >= 2.0.0
Requires:       python3-contextualbandits = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-contextualbandits
Summary:        Python Implementations of Algorithms for Contextual Bandits
%description -n python3-contextualbandits

%prep
%global oreon_srcdir contextualbandits-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-contextualbandits usr/lib/python3*/site-packages/contextualbandits* usr/lib64/python3*/site-packages/contextualbandits* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/contextualbandits* usr/lib64/python3*/site-packages/contextualbandits* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-contextualbandits -f %{oreon_filedir}/python3-contextualbandits.list

%changelog

%autochangelog
