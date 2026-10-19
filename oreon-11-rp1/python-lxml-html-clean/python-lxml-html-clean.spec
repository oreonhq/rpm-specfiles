%global source0_hash e2a4c7d5beedd17cd7b484d848a0571e54baa239a4f9df5546e3acba7f990560
Name:           python-lxml-html-clean
Version:        0.4.5
Release:        1%{?dist}
Summary:        HTML cleaner from lxml project
License:        BSD-3-Clause
URL:            https://lxml-html-clean.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/l/lxml_html_clean/lxml_html_clean-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-lxml-html-clean = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lxml-html-clean
Summary:        HTML cleaner from lxml project
%description -n python3-lxml-html-clean

%prep
%global oreon_srcdir lxml_html_clean-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lxml-html-clean usr/lib/python3*/site-packages/lxml_html_clean* usr/lib64/python3*/site-packages/lxml_html_clean* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lxml_html_clean* usr/lib64/python3*/site-packages/lxml_html_clean* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lxml-html-clean -f %{oreon_filedir}/python3-lxml-html-clean.list

%changelog

%autochangelog
