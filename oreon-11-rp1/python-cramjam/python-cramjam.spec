%global source0_hash 75187b77a84b1f457f9555604775b70d04102af312224d03c873da59011bba31
Name:           python-cramjam
Version:        2.12.1
Release:        1%{?dist}
Summary:        ...
License:        ...
URL:            https://github.com/milesgranger/pyrus-cramjam
Source0:        https://files.pythonhosted.org/packages/source/c/cramjam/cramjam-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) >= 0.14
Requires:       python3-cramjam = %{version}-%{release}
# /oreon:deps
%package -n       python3-cramjam+dev
Summary:        Metapackage for python3-cramjam dev extras
Requires:       python3-cramjam = %{version}-%{release}
Requires:       python3dist(black) == 26.3.1
Requires:       python3dist(pytest) >= 9.0.3
Requires:       python3dist(hypothesis) >= 6.165.10
Provides:       python3dist(cramjam[dev]) = %{version}-%{release}

%description -n python3-cramjam+dev
Metapackage for python3-cramjam dev extras.

%description

%package -n     python3-cramjam
Summary:        ...
%description -n python3-cramjam

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cramjam-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cramjam usr/lib/python3*/site-packages/cramjam* usr/lib64/python3*/site-packages/cramjam* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cramjam* usr/lib64/python3*/site-packages/cramjam* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cramjam -f %{oreon_filedir}/python3-cramjam.list

%changelog

%autochangelog
