%global source0_hash f7a5f88ee194ed6c5aa36d14593fbfb20c5d7bb8f3f5bc57734288d45a5abe26
Name:           python-readability-lxml
Version:        0.9
Release:        1%{?dist}
Summary:        fast html to text parser _article readability tool_ with python 3 support
License:        Apache-2.0
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/r/readability_lxml/readability_lxml-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-readability-lxml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-readability-lxml
Summary:        fast html to text parser _article readability tool_ with python 3 support
%description -n python3-readability-lxml

%prep
%global oreon_srcdir readability_lxml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-readability-lxml usr/lib/python3*/site-packages/readability_lxml* usr/lib64/python3*/site-packages/readability_lxml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/readability_lxml* usr/lib64/python3*/site-packages/readability_lxml* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-readability-lxml -f %{oreon_filedir}/python3-readability-lxml.list

%changelog

%autochangelog
