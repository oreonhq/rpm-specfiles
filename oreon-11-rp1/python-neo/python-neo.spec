%global source0_hash 5485668c5ab4fc9e384e5e645edc9e560987374d24ba8b53665b7a93cd4dcd37
Name:           python-neo
Version:        0.14.5
Release:        1%{?dist}
Summary:        Neo is a package for representing electrophysiology data in Python, together with support for reading a wide range of neurophysiology file formats
License:        BSD-3-Clause
URL:            https://neuralensemble.org/neo
Source0:        https://files.pythonhosted.org/packages/source/n/neo/neo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78.0.2
Requires:       python3-neo = %{version}-%{release}
# /oreon:deps
%package -n       python3-neo+iocache
Summary:        Metapackage for python3-neo iocache extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(joblib) >= 1.0.0
Provides:       python3dist(neo[iocache]) = %{version}-%{release}

%description -n python3-neo+iocache
Metapackage for python3-neo iocache extras.

%package -n       python3-neo+test
Summary:        Metapackage for python3-neo test extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.0.0
Requires:       python3dist(setuptools) < 81
Requires:       python3dist(joblib) >= 1.0.0
Requires:       python3dist(zugbruecke) >= 0.2
Provides:       python3dist(neo[test]) = %{version}-%{release}

%description -n python3-neo+test
Metapackage for python3-neo test extras.

%package -n       python3-neo+docs
Summary:        Metapackage for python3-neo docs extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(numpy) >= 2.0
Provides:       python3dist(neo[docs]) = %{version}-%{release}

%description -n python3-neo+docs
Metapackage for python3-neo docs extras.

%package -n       python3-neo+dev
Summary:        Metapackage for python3-neo dev extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[dev]) = %{version}-%{release}

%description -n python3-neo+dev
Metapackage for python3-neo dev extras.

%package -n       python3-neo+igorproio
Summary:        Metapackage for python3-neo igorproio extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[igorproio]) = %{version}-%{release}

%description -n python3-neo+igorproio
Metapackage for python3-neo igorproio extras.

%package -n       python3-neo+kwikio
Summary:        Metapackage for python3-neo kwikio extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[kwikio]) = %{version}-%{release}

%description -n python3-neo+kwikio
Metapackage for python3-neo kwikio extras.

%package -n       python3-neo+neomatlabio
Summary:        Metapackage for python3-neo neomatlabio extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.0.0
Provides:       python3dist(neo[neomatlabio]) = %{version}-%{release}

%description -n python3-neo+neomatlabio
Metapackage for python3-neo neomatlabio extras.

%package -n       python3-neo+nixio
Summary:        Metapackage for python3-neo nixio extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(nixio) >= 1.5.0
Provides:       python3dist(neo[nixio]) = %{version}-%{release}

%description -n python3-neo+nixio
Metapackage for python3-neo nixio extras.

%package -n       python3-neo+tiffio
Summary:        Metapackage for python3-neo tiffio extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[tiffio]) = %{version}-%{release}

%description -n python3-neo+tiffio
Metapackage for python3-neo tiffio extras.

%package -n       python3-neo+edf
Summary:        Metapackage for python3-neo edf extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[edf]) = %{version}-%{release}

%description -n python3-neo+edf
Metapackage for python3-neo edf extras.

%package -n       python3-neo+ced
Summary:        Metapackage for python3-neo ced extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[ced]) = %{version}-%{release}

%description -n python3-neo+ced
Metapackage for python3-neo ced extras.

%package -n       python3-neo+nwb
Summary:        Metapackage for python3-neo nwb extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[nwb]) = %{version}-%{release}

%description -n python3-neo+nwb
Metapackage for python3-neo nwb extras.

%package -n       python3-neo+maxwell
Summary:        Metapackage for python3-neo maxwell extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[maxwell]) = %{version}-%{release}

%description -n python3-neo+maxwell
Metapackage for python3-neo maxwell extras.

%package -n       python3-neo+biocam
Summary:        Metapackage for python3-neo biocam extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[biocam]) = %{version}-%{release}

%description -n python3-neo+biocam
Metapackage for python3-neo biocam extras.

%package -n       python3-neo+med
Summary:        Metapackage for python3-neo med extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(dhn-med-py) < 2.0
Provides:       python3dist(neo[med]) = %{version}-%{release}

%description -n python3-neo+med
Metapackage for python3-neo med extras.

%package -n       python3-neo+plexon2
Summary:        Metapackage for python3-neo plexon2 extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(zugbruecke) >= 0.2
Provides:       python3dist(neo[plexon2]) = %{version}-%{release}

%description -n python3-neo+plexon2
Metapackage for python3-neo plexon2 extras.

%package -n       python3-neo+neuralynx
Summary:        Metapackage for python3-neo neuralynx extras
Requires:       python3-neo = %{version}-%{release}
Provides:       python3dist(neo[neuralynx]) = %{version}-%{release}

%description -n python3-neo+neuralynx
Metapackage for python3-neo neuralynx extras.

%package -n       python3-neo+all
Summary:        Metapackage for python3-neo all extras
Requires:       python3-neo = %{version}-%{release}
Requires:       python3dist(joblib) >= 1.0.0
Requires:       python3dist(nixio) >= 1.5.0
Requires:       python3dist(scipy) >= 1.0.0
Requires:       python3dist(zugbruecke) >= 0.2
Provides:       python3dist(neo[all]) = %{version}-%{release}

%description -n python3-neo+all
Metapackage for python3-neo all extras.

%description

%package -n     python3-neo
Summary:        Neo is a package for representing electrophysiology data in Python, together with support for reading a wide range of neurophysiology file formats
# oreon:reqs
Requires:       python3dist(numpy) >= 1.25.2
Requires:       python3dist(quantities) >= 0.16.4
# /oreon:reqs
%description -n python3-neo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir neo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-neo usr/lib/python3*/site-packages/neo* usr/lib64/python3*/site-packages/neo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/neo* usr/lib64/python3*/site-packages/neo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-neo -f %{oreon_filedir}/python3-neo.list

%changelog

%autochangelog
