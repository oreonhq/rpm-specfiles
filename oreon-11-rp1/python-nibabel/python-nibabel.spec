%global source0_hash d5f4b9076a13178ae7f7acf18c8dbd503ee1c4d5c0c23b85df7be87efcbb49da
Name:           python-nibabel
Version:        5.4.2
Release:        1%{?dist}
Summary:        Access a multitude of neuroimaging data formats
License:        MIT
URL:            https://nipy.org/nibabel
Source0:        https://files.pythonhosted.org/packages/source/n/nibabel/nibabel-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/pull/1391.patch
Patch:          %{forgeurl}/commit/ac0b38851ad9505c863b56e64c2c4131cf97847c.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27
Requires:       python3-nibabel = %{version}-%{release}
# /oreon:deps
%package -n       python3-nibabel+all
Summary:        Metapackage for python3-nibabel all extras
Requires:       python3-nibabel = %{version}-%{release}
Provides:       python3dist(nibabel[all]) = %{version}-%{release}

%description -n python3-nibabel+all
Metapackage for python3-nibabel all extras.

%package -n       python3-nibabel+indexed_gzip
Summary:        Metapackage for python3-nibabel indexed_gzip extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(indexed-gzip) >= 1.6
Provides:       python3dist(nibabel[indexed_gzip]) = %{version}-%{release}

%description -n python3-nibabel+indexed_gzip
Metapackage for python3-nibabel indexed_gzip extras.

%package -n       python3-nibabel+dicom
Summary:        Metapackage for python3-nibabel dicom extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(pydicom) >= 2.3
Provides:       python3dist(nibabel[dicom]) = %{version}-%{release}

%description -n python3-nibabel+dicom
Metapackage for python3-nibabel dicom extras.

%package -n       python3-nibabel+dicomfs
Summary:        Metapackage for python3-nibabel dicomfs extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(pillow) >= 8.4
Provides:       python3dist(nibabel[dicomfs]) = %{version}-%{release}

%description -n python3-nibabel+dicomfs
Metapackage for python3-nibabel dicomfs extras.

%package -n       python3-nibabel+minc2
Summary:        Metapackage for python3-nibabel minc2 extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(h5py) >= 3.8
Provides:       python3dist(nibabel[minc2]) = %{version}-%{release}

%description -n python3-nibabel+minc2
Metapackage for python3-nibabel minc2 extras.

%package -n       python3-nibabel+spm
Summary:        Metapackage for python3-nibabel spm extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.11
Provides:       python3dist(nibabel[spm]) = %{version}-%{release}

%description -n python3-nibabel+spm
Metapackage for python3-nibabel spm extras.

%package -n       python3-nibabel+viewers
Summary:        Metapackage for python3-nibabel viewers extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(matplotlib) >= 3.7
Provides:       python3dist(nibabel[viewers]) = %{version}-%{release}

%description -n python3-nibabel+viewers
Metapackage for python3-nibabel viewers extras.

%package -n       python3-nibabel+zstd
Summary:        Metapackage for python3-nibabel zstd extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(backports.zstd) >= 1.1
Provides:       python3dist(nibabel[zstd]) = %{version}-%{release}

%description -n python3-nibabel+zstd
Metapackage for python3-nibabel zstd extras.

%package -n       python3-nibabel+test
Summary:        Metapackage for python3-nibabel test extras
Requires:       python3-nibabel = %{version}-%{release}
Requires:       python3dist(pytest) >= 8
Requires:       python3dist(pytest-doctestplus) >= 1.4
Requires:       python3dist(pytest-cov) >= 6
Requires:       python3dist(pytest-httpserver) >= 1.0.7
Requires:       python3dist(pytest-xdist) >= 3.5
Requires:       python3dist(coverage[toml]) >= 7.2
Provides:       python3dist(nibabel[test]) = %{version}-%{release}

%description -n python3-nibabel+test
Metapackage for python3-nibabel test extras.

%package -n       python3-nibabel+doc
Summary:        Metapackage for python3-nibabel doc extras
Requires:       python3-nibabel = %{version}-%{release}
Provides:       python3dist(nibabel[doc]) = %{version}-%{release}

%description -n python3-nibabel+doc
Metapackage for python3-nibabel doc extras.

%package -n       python3-nibabel+dev
Summary:        Metapackage for python3-nibabel dev extras
Requires:       python3-nibabel = %{version}-%{release}
Provides:       python3dist(nibabel[dev]) = %{version}-%{release}

%description -n python3-nibabel+dev
Metapackage for python3-nibabel dev extras.

%package -n       python3-nibabel+doctest
Summary:        Metapackage for python3-nibabel doctest extras
Requires:       python3-nibabel = %{version}-%{release}
Provides:       python3dist(nibabel[doctest]) = %{version}-%{release}

%description -n python3-nibabel+doctest
Metapackage for python3-nibabel doctest extras.

%package -n       python3-nibabel+style
Summary:        Metapackage for python3-nibabel style extras
Requires:       python3-nibabel = %{version}-%{release}
Provides:       python3dist(nibabel[style]) = %{version}-%{release}

%description -n python3-nibabel+style
Metapackage for python3-nibabel style extras.

%package -n       python3-nibabel+typing
Summary:        Metapackage for python3-nibabel typing extras
Requires:       python3-nibabel = %{version}-%{release}
Provides:       python3dist(nibabel[typing]) = %{version}-%{release}

%description -n python3-nibabel+typing
Metapackage for python3-nibabel typing extras.

%description

%package -n     python3-nibabel
Summary:        Access a multitude of neuroimaging data formats
# oreon:reqs
Requires:       python3dist(importlib-resources) >= 5.12
Requires:       python3dist(numpy) >= 1.25
Requires:       python3dist(packaging) >= 20
Requires:       python3dist(typing-extensions) >= 4.6
# /oreon:reqs
%description -n python3-nibabel

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir nibabel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nibabel usr/lib/python3*/site-packages/nibabel* usr/lib64/python3*/site-packages/nibabel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nibabel* usr/lib64/python3*/site-packages/nibabel* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nibabel -f %{oreon_filedir}/python3-nibabel.list

%changelog

%autochangelog
