%global source0_hash e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60
Name:           python-rapidfuzz
Version:        3.14.6
Release:        1%{?dist}
Summary:        rapid fuzzy string matching
License:        MIT
URL:            https://github.com/rapidfuzz/RapidFuzz
Source0:        https://files.pythonhosted.org/packages/source/r/rapidfuzz/rapidfuzz-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(scikit-build-core) >= 0.11
Requires:       python3-rapidfuzz = %{version}-%{release}
# /oreon:deps
%package -n       python3-rapidfuzz+all
Summary:        Metapackage for python3-rapidfuzz all extras
Requires:       python3-rapidfuzz = %{version}-%{release}
Provides:       python3dist(rapidfuzz[all]) = %{version}-%{release}

%description -n python3-rapidfuzz+all
Metapackage for python3-rapidfuzz all extras.

%description

%package -n     python3-rapidfuzz
Summary:        rapid fuzzy string matching
%description -n python3-rapidfuzz

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rapidfuzz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rapidfuzz usr/lib/python3*/site-packages/rapidfuzz* usr/lib64/python3*/site-packages/rapidfuzz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rapidfuzz* usr/lib64/python3*/site-packages/rapidfuzz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rapidfuzz -f %{oreon_filedir}/python3-rapidfuzz.list

%changelog

%autochangelog
