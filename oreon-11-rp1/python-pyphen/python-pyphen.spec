%global source0_hash dbae6fbbe4f01cb206108b43573d857c67107be9d0e38eb1b08d6fa2210634a7
Name:           python-pyphen
Version:        0.18.1
Release:        1%{?dist}
Summary:        Pure Python module to hyphenate text
License:        ...
URL:            https://www.courtbouillon.org/pyphen
Source0:        https://files.pythonhosted.org/packages/source/p/pyphen/pyphen-%{version}.tar.gz
BuildArch:      noarch
Patch1:         %{name}-strip-optional-dependencies.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pyphen = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyphen+doc
Summary:        Metapackage for python3-pyphen doc extras
Requires:       python3-pyphen = %{version}-%{release}
Provides:       python3dist(pyphen[doc]) = %{version}-%{release}

%description -n python3-pyphen+doc
Metapackage for python3-pyphen doc extras.

%package -n       python3-pyphen+test
Summary:        Metapackage for python3-pyphen test extras
Requires:       python3-pyphen = %{version}-%{release}
Provides:       python3dist(pyphen[test]) = %{version}-%{release}

%description -n python3-pyphen+test
Metapackage for python3-pyphen test extras.

%description

%package -n     python3-pyphen
Summary:        Pure Python module to hyphenate text
%description -n python3-pyphen

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyphen-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyphen usr/lib/python3*/site-packages/pyphen* usr/lib64/python3*/site-packages/pyphen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyphen* usr/lib64/python3*/site-packages/pyphen* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyphen -f %{oreon_filedir}/python3-pyphen.list

%changelog

%autochangelog
