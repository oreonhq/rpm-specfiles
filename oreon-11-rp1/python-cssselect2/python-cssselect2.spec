%global source0_hash 83b0d820ef589dabaf693289b647c2f5b410f76d285f56deba911ffa75a7b9d1
Name:           python-cssselect2
Version:        0.10.1
Release:        1%{?dist}
Summary:        CSS selectors for Python ElementTree
License:        ...
URL:            https://doc.courtbouillon.org/cssselect2/
Source0:        https://files.pythonhosted.org/packages/source/c/cssselect2/cssselect2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-cssselect2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-cssselect2+doc
Summary:        Metapackage for python3-cssselect2 doc extras
Requires:       python3-cssselect2 = %{version}-%{release}
Provides:       python3dist(cssselect2[doc]) = %{version}-%{release}

%description -n python3-cssselect2+doc
Metapackage for python3-cssselect2 doc extras.

%package -n       python3-cssselect2+test
Summary:        Metapackage for python3-cssselect2 test extras
Requires:       python3-cssselect2 = %{version}-%{release}
Provides:       python3dist(cssselect2[test]) = %{version}-%{release}

%description -n python3-cssselect2+test
Metapackage for python3-cssselect2 test extras.

%description

%package -n     python3-cssselect2
Summary:        CSS selectors for Python ElementTree
%description -n python3-cssselect2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cssselect2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cssselect2 usr/lib/python3*/site-packages/cssselect2* usr/lib64/python3*/site-packages/cssselect2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cssselect2* usr/lib64/python3*/site-packages/cssselect2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cssselect2 -f %{oreon_filedir}/python3-cssselect2.list

%changelog

%autochangelog
