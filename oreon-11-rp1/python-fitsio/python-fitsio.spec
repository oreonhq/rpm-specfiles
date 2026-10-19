%global source0_hash 92a02f0e63d539d85ca5a185ae0cc8d40029270858275964ee2539ee0136f0c3
Name:           python-fitsio
Version:        1.4.2
Release:        1%{?dist}
Summary:        A full featured python library to read from and write to FITS files.
License:        GPL-2.0-or-later
URL:            https://github.com/esheldon/fitsio
Source0:        https://files.pythonhosted.org/packages/source/f/fitsio/fitsio-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) >= 1.7
BuildRequires:  python3dist(setuptools) >= 78
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-fitsio = %{version}-%{release}
# /oreon:deps
%package -n       python3-fitsio+dev
Summary:        Metapackage for python3-fitsio dev extras
Requires:       python3-fitsio = %{version}-%{release}
Provides:       python3dist(fitsio[dev]) = %{version}-%{release}

%description -n python3-fitsio+dev
Metapackage for python3-fitsio dev extras.

%description

%package -n     python3-fitsio
Summary:        A full featured python library to read from and write to FITS files.
# oreon:reqs
Requires:       python3dist(numpy) >= 1.7
# /oreon:reqs
%description -n python3-fitsio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fitsio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fitsio usr/lib/python3*/site-packages/fitsio* usr/lib64/python3*/site-packages/fitsio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fitsio* usr/lib64/python3*/site-packages/fitsio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fitsio -f %{oreon_filedir}/python3-fitsio.list

%changelog

%autochangelog
