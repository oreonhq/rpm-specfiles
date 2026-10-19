%global source0_hash 7ec6b7e51f1a3a09af6ccd8f1b54c9e5cd95da347e340b88bac933c4d9fa7f63
Name:           python-puzpy
Version:        0.6.1
Release:        1%{?dist}
Summary:        python crossword puzzle library
License:        MIT
URL:            https://github.com/alexdej/puzpy.git
Source0:        https://files.pythonhosted.org/packages/source/p/puzpy/puzpy-%{version}.tar.gz
BuildArch:      noarch
Patch:          puzpy-drop-unneeded-deps.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-puzpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-puzpy+dev
Summary:        Metapackage for python3-puzpy dev extras
Requires:       python3-puzpy = %{version}-%{release}
Provides:       python3dist(puzpy[dev]) = %{version}-%{release}

%description -n python3-puzpy+dev
Metapackage for python3-puzpy dev extras.

%package -n       python3-puzpy+publish
Summary:        Metapackage for python3-puzpy publish extras
Requires:       python3-puzpy = %{version}-%{release}
Provides:       python3dist(puzpy[publish]) = %{version}-%{release}

%description -n python3-puzpy+publish
Metapackage for python3-puzpy publish extras.

%description

%package -n     python3-puzpy
Summary:        python crossword puzzle library
%description -n python3-puzpy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir puzpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-puzpy usr/lib/python3*/site-packages/puzpy* usr/lib64/python3*/site-packages/puzpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/puzpy* usr/lib64/python3*/site-packages/puzpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-puzpy -f %{oreon_filedir}/python3-puzpy.list

%changelog

%autochangelog
