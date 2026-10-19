%global source0_hash 03392d30e3a561b493e728c776799238b484c1648b2ed1a04182831ae8d7d7ce
Name:           python-sphinx-gallery
Version:        0.22.0
Release:        1%{?dist}
Summary:        A Sphinx extension that builds an HTML gallery of examples from any set of Python scripts.
License:        ...
URL:            https://github.com/sphinx-gallery/sphinx-gallery
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_gallery/sphinx_gallery-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm) >= 7
Requires:       python3-sphinx-gallery = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-gallery+animations
Summary:        Metapackage for python3-sphinx-gallery animations extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Provides:       python3dist(sphinx-gallery[animations]) = %{version}-%{release}

%description -n python3-sphinx-gallery+animations
Metapackage for python3-sphinx-gallery animations extras.

%package -n       python3-sphinx-gallery+dev
Summary:        Metapackage for python3-sphinx-gallery dev extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Requires:       python3dist(jupyterlite-sphinx) >= 0.17.1
Provides:       python3dist(sphinx-gallery[dev]) = %{version}-%{release}

%description -n python3-sphinx-gallery+dev
Metapackage for python3-sphinx-gallery dev extras.

%package -n       python3-sphinx-gallery+jupyterlite
Summary:        Metapackage for python3-sphinx-gallery jupyterlite extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Provides:       python3dist(sphinx-gallery[jupyterlite]) = %{version}-%{release}

%description -n python3-sphinx-gallery+jupyterlite
Metapackage for python3-sphinx-gallery jupyterlite extras.

%package -n       python3-sphinx-gallery+parallel
Summary:        Metapackage for python3-sphinx-gallery parallel extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Provides:       python3dist(sphinx-gallery[parallel]) = %{version}-%{release}

%description -n python3-sphinx-gallery+parallel
Metapackage for python3-sphinx-gallery parallel extras.

%package -n       python3-sphinx-gallery+recommender
Summary:        Metapackage for python3-sphinx-gallery recommender extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Provides:       python3dist(sphinx-gallery[recommender]) = %{version}-%{release}

%description -n python3-sphinx-gallery+recommender
Metapackage for python3-sphinx-gallery recommender extras.

%package -n       python3-sphinx-gallery+show-api-usage
Summary:        Metapackage for python3-sphinx-gallery show-api-usage extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Provides:       python3dist(sphinx-gallery[show-api-usage]) = %{version}-%{release}

%description -n python3-sphinx-gallery+show-api-usage
Metapackage for python3-sphinx-gallery show-api-usage extras.

%package -n       python3-sphinx-gallery+show-memory
Summary:        Metapackage for python3-sphinx-gallery show-memory extras
Requires:       python3-sphinx-gallery = %{version}-%{release}
Provides:       python3dist(sphinx-gallery[show-memory]) = %{version}-%{release}

%description -n python3-sphinx-gallery+show-memory
Metapackage for python3-sphinx-gallery show-memory extras.

%description

%package -n     python3-sphinx-gallery
Summary:        A Sphinx extension that builds an HTML gallery of examples from any set of Python scripts.
# oreon:reqs
Requires:       python3dist(sphinx) >= 6
# /oreon:reqs
%description -n python3-sphinx-gallery

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_gallery-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-gallery usr/lib/python3*/site-packages/sphinx_gallery* usr/lib64/python3*/site-packages/sphinx_gallery* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_gallery* usr/lib64/python3*/site-packages/sphinx_gallery* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-gallery -f %{oreon_filedir}/python3-sphinx-gallery.list

%changelog

%autochangelog
