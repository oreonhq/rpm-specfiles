%global source0_hash ef4e2caa38169e3fbbc4164764a060d1877a6692519a4bed82521328eeb0d9aa
Name:           python-ase
Version:        3.29.0
Release:        1%{?dist}
Summary:        Atomic Simulation Environment
License:        LGPL-2.1-or-later
URL:            https://ase-lib.org/
Source0:        https://files.pythonhosted.org/packages/source/a/ase/ase-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-ase = %{version}-%{release}
# /oreon:deps
%package -n       python3-ase+docs
Summary:        Metapackage for python3-ase docs extras
Requires:       python3-ase = %{version}-%{release}
Provides:       python3dist(ase[docs]) = %{version}-%{release}

%description -n python3-ase+docs
Metapackage for python3-ase docs extras.

%package -n       python3-ase+test
Summary:        Metapackage for python3-ase test extras
Requires:       python3-ase = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.4.0
Requires:       python3dist(pytest-xdist) >= 3.2.0
Provides:       python3dist(ase[test]) = %{version}-%{release}

%description -n python3-ase+test
Metapackage for python3-ase test extras.

%package -n       python3-ase+spglib
Summary:        Metapackage for python3-ase spglib extras
Requires:       python3-ase = %{version}-%{release}
Requires:       python3dist(spglib) >= 1.9
Provides:       python3dist(ase[spglib]) = %{version}-%{release}

%description -n python3-ase+spglib
Metapackage for python3-ase spglib extras.

%package -n       python3-ase+lint
Summary:        Metapackage for python3-ase lint extras
Requires:       python3-ase = %{version}-%{release}
Provides:       python3dist(ase[lint]) = %{version}-%{release}

%description -n python3-ase+lint
Metapackage for python3-ase lint extras.

%description

%package -n     python3-ase
Summary:        Atomic Simulation Environment
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.5.2
Requires:       python3dist(numpy) >= 1.21.6
Requires:       python3dist(scipy) >= 1.8.1
Requires:       python3dist(typing-extensions) >= 4.13.1
# /oreon:reqs
%description -n python3-ase

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ase-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ase usr/lib/python3*/site-packages/ase* usr/lib64/python3*/site-packages/ase* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ase* usr/lib64/python3*/site-packages/ase* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ase -f %{oreon_filedir}/python3-ase.list

%changelog

%autochangelog
