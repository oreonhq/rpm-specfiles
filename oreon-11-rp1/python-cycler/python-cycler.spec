%global source0_hash 88bb128f02ba341da8ef447245a9e138fae777f6a23943da4540077d3601eb1c
Name:           python-cycler
Version:        0.12.1
Release:        1%{?dist}
Summary:        Composable style cycles
License:        ...
URL:            https://matplotlib.org/cycler/
Source0:        https://files.pythonhosted.org/packages/source/c/cycler/cycler-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-cycler = %{version}-%{release}
# /oreon:deps
%package -n       python3-cycler+docs
Summary:        Metapackage for python3-cycler docs extras
Requires:       python3-cycler = %{version}-%{release}
Provides:       python3dist(cycler[docs]) = %{version}-%{release}

%description -n python3-cycler+docs
Metapackage for python3-cycler docs extras.

%package -n       python3-cycler+tests
Summary:        Metapackage for python3-cycler tests extras
Requires:       python3-cycler = %{version}-%{release}
Provides:       python3dist(cycler[tests]) = %{version}-%{release}

%description -n python3-cycler+tests
Metapackage for python3-cycler tests extras.

%description

%package -n     python3-cycler
Summary:        Composable style cycles
%description -n python3-cycler

%prep
%global oreon_srcdir cycler-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cycler usr/lib/python3*/site-packages/cycler* usr/lib64/python3*/site-packages/cycler* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cycler* usr/lib64/python3*/site-packages/cycler* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cycler -f %{oreon_filedir}/python3-cycler.list

%changelog

%autochangelog
