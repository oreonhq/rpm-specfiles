%global source0_hash f5f970ab04efad85c24714321fcc91613fcb64ef2a892a13167df2f3e59199fa
Name:           python-scikit-image
Version:        0.26.0
Release:        1%{?dist}
Summary:        Image processing in Python
License:        ...
URL:            https://scikit-image.org
Source0:        https://files.pythonhosted.org/packages/source/s/scikit_image/scikit_image-%{version}.tar.gz
Patch: https://github.com/scikit-image/scikit-image/pull/7808.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0.8
BuildRequires:  python3dist(lazy-loader) >= 0.4
BuildRequires:  python3dist(meson-python) >= 0.16
BuildRequires:  python3dist(numpy) >= 2.0
BuildRequires:  python3dist(pythran) >= 0.16
Requires:       python3-scikit-image = %{version}-%{release}
# /oreon:deps
%package -n       python3-scikit-image+build
Summary:        Metapackage for python3-scikit-image build extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(meson-python) >= 0.16
Requires:       python3dist(ninja) >= 1.11.1.1
Requires:       python3dist(cython) >= 3.0.8
Requires:       python3dist(pythran) >= 0.16
Requires:       python3dist(numpy) >= 2.0
Requires:       python3dist(spin) == 0.13
Requires:       python3dist(build) >= 1.2.1
Provides:       python3dist(scikit-image[build]) = %{version}-%{release}

%description -n python3-scikit-image+build
Metapackage for python3-scikit-image build extras.

%package -n       python3-scikit-image+data
Summary:        Metapackage for python3-scikit-image data extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(pooch) >= 1.6.0
Provides:       python3dist(scikit-image[data]) = %{version}-%{release}

%description -n python3-scikit-image+data
Metapackage for python3-scikit-image data extras.

%package -n       python3-scikit-image+developer
Summary:        Metapackage for python3-scikit-image developer extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(docstub) == 0.3.0.post0
Provides:       python3dist(scikit-image[developer]) = %{version}-%{release}

%description -n python3-scikit-image+developer
Metapackage for python3-scikit-image developer extras.

%package -n       python3-scikit-image+asv
Summary:        Metapackage for python3-scikit-image asv extras
Requires:       python3-scikit-image = %{version}-%{release}
Provides:       python3dist(scikit-image[asv]) = %{version}-%{release}

%description -n python3-scikit-image+asv
Metapackage for python3-scikit-image asv extras.

%package -n       python3-scikit-image+docs
Summary:        Metapackage for python3-scikit-image docs extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.0
Requires:       python3dist(sphinx-gallery[parallel]) >= 0.18
Requires:       python3dist(numpydoc) >= 1.7
Requires:       python3dist(matplotlib) >= 3.7
Requires:       python3dist(dask[array]) >= 2023.2.0
Requires:       python3dist(pandas) >= 2.0
Requires:       python3dist(seaborn) >= 0.11
Requires:       python3dist(pooch) >= 1.6
Requires:       python3dist(tifffile) >= 2022.8.12
Requires:       python3dist(intersphinx-registry) >= 0.2411.14
Requires:       python3dist(plotly) >= 5.20
Requires:       python3dist(kaleido) == 0.2.1
Requires:       python3dist(scikit-learn) >= 1.2
Requires:       python3dist(sphinx-design) >= 0.5
Requires:       python3dist(pydata-sphinx-theme) >= 0.16
Requires:       python3dist(pywavelets) >= 1.6
Requires:       python3dist(pytest-doctestplus) >= 1.6.0
Provides:       python3dist(scikit-image[docs]) = %{version}-%{release}

%description -n python3-scikit-image+docs
Metapackage for python3-scikit-image docs extras.

%package -n       python3-scikit-image+optional
Summary:        Metapackage for python3-scikit-image optional extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(scikit-learn) >= 1.2
Requires:       python3dist(pyamg) >= 5.2
Provides:       python3dist(scikit-image[optional]) = %{version}-%{release}

%description -n python3-scikit-image+optional
Metapackage for python3-scikit-image optional extras.

%package -n       python3-scikit-image+optional_free_threaded
Summary:        Metapackage for python3-scikit-image optional_free_threaded extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(astropy) >= 6.0
Requires:       python3dist(dask[array]) >= 2023.2.0
Requires:       python3dist(matplotlib) >= 3.7
Requires:       python3dist(pooch) >= 1.6.0
Requires:       python3dist(pywavelets) >= 1.6
Provides:       python3dist(scikit-image[optional_free_threaded]) = %{version}-%{release}

%description -n python3-scikit-image+optional_free_threaded
Metapackage for python3-scikit-image optional_free_threaded extras.

%package -n       python3-scikit-image+test
Summary:        Metapackage for python3-scikit-image test extras
Requires:       python3-scikit-image = %{version}-%{release}
Requires:       python3dist(numpydoc) >= 1.7
Requires:       python3dist(pooch) >= 1.6.0
Requires:       python3dist(pytest) >= 8.3
Requires:       python3dist(pytest-cov) >= 2.11.0
Requires:       python3dist(pytest-doctestplus) >= 1.6.0
Provides:       python3dist(scikit-image[test]) = %{version}-%{release}

%description -n python3-scikit-image+test
Metapackage for python3-scikit-image test extras.

%description

%package -n     python3-scikit-image
Summary:        Image processing in Python
# oreon:reqs
Requires:       python3dist(imageio) >= 2.33
Requires:       python3dist(lazy-loader) >= 0.4
Requires:       python3dist(networkx) >= 3.0
Requires:       python3dist(numpy) >= 1.24
Requires:       python3dist(packaging) >= 21
Requires:       python3dist(pillow) >= 10.1
Requires:       python3dist(scipy) >= 1.11.4
Requires:       python3dist(tifffile) >= 2022.8.12
# /oreon:reqs
%description -n python3-scikit-image

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir scikit_image-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scikit-image usr/lib/python3*/site-packages/scikit_image* usr/lib64/python3*/site-packages/scikit_image* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scikit_image* usr/lib64/python3*/site-packages/scikit_image* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-scikit-image -f %{oreon_filedir}/python3-scikit-image.list

%changelog

%autochangelog
