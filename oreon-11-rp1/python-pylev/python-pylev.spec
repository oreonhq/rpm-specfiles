%global source0_hash 9e77e941042ad3a4cc305dcdf2b2dec1aec2fbe3dd9015d2698ad02b173006d1
Name:           python-pylev
Version:        1.4.0
Release:        1%{?dist}
Summary:        A pure Python Levenshtein implementation that_s not freaking GPL_d.
License:        ...
URL:            http://github.com/toastdriven/pylev
Source0:        https://files.pythonhosted.org/packages/source/p/pylev/pylev-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-pylev = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pylev
Summary:        A pure Python Levenshtein implementation that_s not freaking GPL_d.
%description -n python3-pylev

%prep
%global oreon_srcdir pylev-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pylev usr/lib/python3*/site-packages/pylev* usr/lib64/python3*/site-packages/pylev* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pylev* usr/lib64/python3*/site-packages/pylev* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pylev -f %{oreon_filedir}/python3-pylev.list

%changelog

%autochangelog
