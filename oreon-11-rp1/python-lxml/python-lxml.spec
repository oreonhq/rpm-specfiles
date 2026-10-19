%global source0_hash 45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21
Name:           python-lxml
Version:        6.1.3
Release:        1%{?dist}
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
License:        BSD-3-Clause
URL:            https://github.com/lxml/lxml
Source0:        https://files.pythonhosted.org/packages/source/l/lxml/lxml-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 3.3
BuildRequires:  python3dist(cython) >= 3.2.9
Requires:       python3-lxml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lxml
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
%description -n python3-lxml

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lxml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lxml usr/lib/python3*/site-packages/lxml* usr/lib64/python3*/site-packages/lxml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lxml* usr/lib64/python3*/site-packages/lxml* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lxml -f %{oreon_filedir}/python3-lxml.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.2-1
- Prepare for Oreon 11 (RP1)
