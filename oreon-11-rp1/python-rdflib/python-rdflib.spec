%global source0_hash 6c831288d5e4a5a7ece85d0ccde9877d512a3d0f02d7c06455d00d6d0ea379df
Name:           python-rdflib
Version:        7.6.0
Release:        1%{?dist}
Summary:        RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.
License:        BSD-3-Clause
URL:            https://github.com/RDFLib/rdflib
Source0:        https://files.pythonhosted.org/packages/source/r/rdflib/rdflib-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Fix-py3.14-test-failure-due-to-NotImplemented-change.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.4.0
Requires:       python3-rdflib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rdflib
Summary:        RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.
%description -n python3-rdflib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rdflib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rdflib usr/lib/python3*/site-packages/rdflib* usr/lib64/python3*/site-packages/rdflib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rdflib* usr/lib64/python3*/site-packages/rdflib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rdflib -f %{oreon_filedir}/python3-rdflib.list

%changelog

%autochangelog
