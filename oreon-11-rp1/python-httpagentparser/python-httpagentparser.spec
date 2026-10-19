%global source0_hash 23bcaf09325b17af7634283ca64da23f485c5d83b9481ff6d88413a7c5bc6de9
Name:           python-httpagentparser
Version:        1.9.9
Release:        1%{?dist}
Summary:        Extracts OS Browser etc information from http user agent string
License:        ...
URL:            https://github.com/shon/httpagentparser
Source0:        https://files.pythonhosted.org/packages/source/h/httpagentparser/httpagentparser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-httpagentparser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-httpagentparser
Summary:        Extracts OS Browser etc information from http user agent string
%description -n python3-httpagentparser

%prep
%global oreon_srcdir httpagentparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httpagentparser usr/lib/python3*/site-packages/httpagentparser* usr/lib64/python3*/site-packages/httpagentparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httpagentparser* usr/lib64/python3*/site-packages/httpagentparser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-httpagentparser -f %{oreon_filedir}/python3-httpagentparser.list

%changelog

%autochangelog
