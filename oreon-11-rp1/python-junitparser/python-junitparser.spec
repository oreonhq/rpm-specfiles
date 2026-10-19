%global source0_hash f824ec1b7afbf2fd3b6813b87967b02fcda750e135d27be17cae497147419a04
Name:           python-junitparser
Version:        5.0.3
Release:        1%{?dist}
Summary:        Manipulates JUnit/xUnit Result XML files
License:        Apache-2.0
URL:            https://github.com/weiwei/junitparser
Source0:        https://files.pythonhosted.org/packages/source/j/junitparser/junitparser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13.0
BuildRequires:  python3dist(uv-build) >= 0.11.7
Requires:       python3-junitparser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-junitparser
Summary:        Manipulates JUnit/xUnit Result XML files
%description -n python3-junitparser

%prep
%global oreon_srcdir junitparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-junitparser usr/lib/python3*/site-packages/junitparser* usr/lib64/python3*/site-packages/junitparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/junitparser* usr/lib64/python3*/site-packages/junitparser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-junitparser -f %{oreon_filedir}/python3-junitparser.list

%changelog

%autochangelog
