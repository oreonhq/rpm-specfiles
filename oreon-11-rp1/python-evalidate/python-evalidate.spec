%global source0_hash 86b574117c839e7479b04efccd07eb2ef55669bfcbb2bbb59ea1bdf6d1c7d0ab
Name:           python-evalidate
Version:        2.1.4
Release:        1%{?dist}
Summary:        Validation and secure evaluation of untrusted python expressions
License:        MIT
URL:            https://github.com/yaroslaff/evalidate
Source0:        https://files.pythonhosted.org/packages/source/e/evalidate/evalidate-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-evalidate = %{version}-%{release}
# /oreon:deps
%package -n       python3-evalidate+generate
Summary:        Metapackage for python3-evalidate generate extras
Requires:       python3-evalidate = %{version}-%{release}
Provides:       python3dist(evalidate[generate]) = %{version}-%{release}

%description -n python3-evalidate+generate
Metapackage for python3-evalidate generate extras.

%description

%package -n     python3-evalidate
Summary:        Validation and secure evaluation of untrusted python expressions
%description -n python3-evalidate

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir evalidate-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-evalidate usr/lib/python3*/site-packages/evalidate* usr/lib64/python3*/site-packages/evalidate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/evalidate* usr/lib64/python3*/site-packages/evalidate* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-evalidate -f %{oreon_filedir}/python3-evalidate.list

%changelog

%autochangelog
