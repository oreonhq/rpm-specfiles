%global source0_hash 7d406171c8928a5e6db6d21e6effb90fc4a0c28e904a084095e37c97fd755431
Name:           python-fslpy
Version:        3.29.1
Release:        1%{?dist}
Summary:        FSL Python library
License:        ...
URL:            https://git.fmrib.ox.ac.uk/fsl/fslpy/
Source0:        https://files.pythonhosted.org/packages/source/f/fslpy/fslpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fslpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-fslpy+extra
Summary:        Metapackage for python3-fslpy extra extras
Requires:       python3-fslpy = %{version}-%{release}
Requires:       python3dist(indexed-gzip) >= 0.7
Requires:       python3dist(wxpython) >= 4
Requires:       python3dist(trimesh) >= 2.37.29
Requires:       python3dist(rtree) >= 0.8.3
Requires:       python3dist(pillow) >= 3.2.0
Provides:       python3dist(fslpy[extra]) = %{version}-%{release}

%description -n python3-fslpy+extra
Metapackage for python3-fslpy extra extras.

%package -n       python3-fslpy+doc
Summary:        Metapackage for python3-fslpy doc extras
Requires:       python3-fslpy = %{version}-%{release}
Provides:       python3dist(fslpy[doc]) = %{version}-%{release}

%description -n python3-fslpy+doc
Metapackage for python3-fslpy doc extras.

%package -n       python3-fslpy+test
Summary:        Metapackage for python3-fslpy test extras
Requires:       python3-fslpy = %{version}-%{release}
Provides:       python3dist(fslpy[test]) = %{version}-%{release}

%description -n python3-fslpy+test
Metapackage for python3-fslpy test extras.

%package -n       python3-fslpy+style
Summary:        Metapackage for python3-fslpy style extras
Requires:       python3-fslpy = %{version}-%{release}
Provides:       python3dist(fslpy[style]) = %{version}-%{release}

%description -n python3-fslpy+style
Metapackage for python3-fslpy style extras.

%description

%package -n     python3-fslpy
Summary:        FSL Python library
# oreon:reqs
Requires:       python3dist(h5py) >= 2.9
Requires:       python3dist(nibabel) >= 5.4
Requires:       python3dist(numpy) >= 1
Requires:       python3dist(scipy) >= 0.18
# /oreon:reqs
%description -n python3-fslpy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fslpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fslpy usr/lib/python3*/site-packages/fslpy* usr/lib64/python3*/site-packages/fslpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fslpy* usr/lib64/python3*/site-packages/fslpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fslpy -f %{oreon_filedir}/python3-fslpy.list

%changelog

%autochangelog
