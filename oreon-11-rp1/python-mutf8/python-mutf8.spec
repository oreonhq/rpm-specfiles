%global source0_hash 279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a
Name:           python-mutf8
Version:        1.1.0
Release:        1%{?dist}
Summary:        Fast MUTF-8 encoder _ decoder
License:        MIT
URL:            https://github.com/TkTech/mutf8
Source0:        https://files.pythonhosted.org/packages/source/m/mutf8/mutf8-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-mutf8 = %{version}-%{release}
# /oreon:deps
%package -n       python3-mutf8+test
Summary:        Metapackage for python3-mutf8 test extras
Requires:       python3-mutf8 = %{version}-%{release}
Provides:       python3dist(mutf8[test]) = %{version}-%{release}

%description -n python3-mutf8+test
Metapackage for python3-mutf8 test extras.

%description

%package -n     python3-mutf8
Summary:        Fast MUTF-8 encoder _ decoder
%description -n python3-mutf8

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mutf8-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mutf8 usr/lib/python3*/site-packages/mutf8* usr/lib64/python3*/site-packages/mutf8* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mutf8* usr/lib64/python3*/site-packages/mutf8* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mutf8 -f %{oreon_filedir}/python3-mutf8.list

%changelog

%autochangelog
