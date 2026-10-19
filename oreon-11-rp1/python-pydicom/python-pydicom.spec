%global source0_hash 5942bfc2d72c6fa4b3b5b62c527f54b7f2355f21d6f5d296df6bb30188df6a4f
Name:           python-pydicom
Version:        3.0.2
Release:        1%{?dist}
Summary:        A pure Python package for reading and writing DICOM data
License:        MIT
URL:            https://github.com/pydicom/pydicom
Source0:        https://files.pythonhosted.org/packages/source/p/pydicom/pydicom-%{version}.tar.gz
BuildArch:      noarch
Patch:          pydicom-3.0.1-endian-numpy.patch
Patch:          pydicom-3.0.1-endian-pillow.patch
Patch:          https://github.com/pydicom/pydicom/pull/2173/commits/016abf0fa18a6f578a55d9816084f901a9809367.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pydicom = %{version}-%{release}
# /oreon:deps
%package -n       python3-pydicom+docs
Summary:        Metapackage for python3-pydicom docs extras
Requires:       python3-pydicom = %{version}-%{release}
Provides:       python3dist(pydicom[docs]) = %{version}-%{release}

%description -n python3-pydicom+docs
Metapackage for python3-pydicom docs extras.

%package -n       python3-pydicom+dev
Summary:        Metapackage for python3-pydicom dev extras
Requires:       python3-pydicom = %{version}-%{release}
Requires:       python3dist(black) == 24.8.0
Requires:       python3dist(mypy) == 1.11.2
Requires:       python3dist(ruff) == 0.6.3
Requires:       python3dist(pyfakefs) >= 6.1.6
Provides:       python3dist(pydicom[dev]) = %{version}-%{release}

%description -n python3-pydicom+dev
Metapackage for python3-pydicom dev extras.

%package -n       python3-pydicom+basic
Summary:        Metapackage for python3-pydicom basic extras
Requires:       python3-pydicom = %{version}-%{release}
Provides:       python3dist(pydicom[basic]) = %{version}-%{release}

%description -n python3-pydicom+basic
Metapackage for python3-pydicom basic extras.

%package -n       python3-pydicom+pixeldata
Summary:        Metapackage for python3-pydicom pixeldata extras
Requires:       python3-pydicom = %{version}-%{release}
Provides:       python3dist(pydicom[pixeldata]) = %{version}-%{release}

%description -n python3-pydicom+pixeldata
Metapackage for python3-pydicom pixeldata extras.

%package -n       python3-pydicom+gpl-license
Summary:        Metapackage for python3-pydicom gpl-license extras
Requires:       python3-pydicom = %{version}-%{release}
Provides:       python3dist(pydicom[gpl-license]) = %{version}-%{release}

%description -n python3-pydicom+gpl-license
Metapackage for python3-pydicom gpl-license extras.

%description

%package -n     python3-pydicom
Summary:        A pure Python package for reading and writing DICOM data
%description -n python3-pydicom

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pydicom-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydicom usr/lib/python3*/site-packages/pydicom* usr/lib64/python3*/site-packages/pydicom* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydicom* usr/lib64/python3*/site-packages/pydicom* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydicom -f %{oreon_filedir}/python3-pydicom.list

%changelog

%autochangelog
