%global source0_hash 85dbfe747e5b5aed1f1fd41ef5de0c0ab8322227ee308191a44fff12c59c197d
Name:           python-mapclassify
Version:        2.11.0
Release:        1%{?dist}
Summary:        Classification Schemes for Choropleth Maps.
License:        ...
URL:            https://github.com/pysal/mapclassify
Source0:        https://files.pythonhosted.org/packages/source/m/mapclassify/mapclassify-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Use-system-copy-of-Natural-Earth-data.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-mapclassify = %{version}-%{release}
# /oreon:deps
%package -n       python3-mapclassify+speedups
Summary:        Metapackage for python3-mapclassify speedups extras
Requires:       python3-mapclassify = %{version}-%{release}
Requires:       python3dist(numba) >= 0.60
Provides:       python3dist(mapclassify[speedups]) = %{version}-%{release}

%description -n python3-mapclassify+speedups
Metapackage for python3-mapclassify speedups extras.

%package -n       python3-mapclassify+dev
Summary:        Metapackage for python3-mapclassify dev extras
Requires:       python3-mapclassify = %{version}-%{release}
Provides:       python3dist(mapclassify[dev]) = %{version}-%{release}

%description -n python3-mapclassify+dev
Metapackage for python3-mapclassify dev extras.

%package -n       python3-mapclassify+docs
Summary:        Metapackage for python3-mapclassify docs extras
Requires:       python3-mapclassify = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.4.3
Provides:       python3dist(mapclassify[docs]) = %{version}-%{release}

%description -n python3-mapclassify+docs
Metapackage for python3-mapclassify docs extras.

%package -n       python3-mapclassify+spatial
Summary:        Metapackage for python3-mapclassify spatial extras
Requires:       python3-mapclassify = %{version}-%{release}
Provides:       python3dist(mapclassify[spatial]) = %{version}-%{release}

%description -n python3-mapclassify+spatial
Metapackage for python3-mapclassify spatial extras.

%package -n       python3-mapclassify+notebooks
Summary:        Metapackage for python3-mapclassify notebooks extras
Requires:       python3-mapclassify = %{version}-%{release}
Provides:       python3dist(mapclassify[notebooks]) = %{version}-%{release}

%description -n python3-mapclassify+notebooks
Metapackage for python3-mapclassify notebooks extras.

%package -n       python3-mapclassify+tests
Summary:        Metapackage for python3-mapclassify tests extras
Requires:       python3-mapclassify = %{version}-%{release}
Provides:       python3dist(mapclassify[tests]) = %{version}-%{release}

%description -n python3-mapclassify+tests
Metapackage for python3-mapclassify tests extras.

%package -n       python3-mapclassify+all
Summary:        Metapackage for python3-mapclassify all extras
Requires:       python3-mapclassify = %{version}-%{release}
Provides:       python3dist(mapclassify[all]) = %{version}-%{release}

%description -n python3-mapclassify+all
Metapackage for python3-mapclassify all extras.

%description

%package -n     python3-mapclassify
Summary:        Classification Schemes for Choropleth Maps.
# oreon:reqs
Requires:       python3dist(networkx) >= 3.4
Requires:       python3dist(numpy) >= 2.0
Requires:       python3dist(pandas) >= 2.3
Requires:       python3dist(scikit-learn) >= 1.5
Requires:       python3dist(scipy) >= 1.14
# /oreon:reqs
%description -n python3-mapclassify

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mapclassify-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mapclassify usr/lib/python3*/site-packages/mapclassify* usr/lib64/python3*/site-packages/mapclassify* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mapclassify* usr/lib64/python3*/site-packages/mapclassify* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mapclassify -f %{oreon_filedir}/python3-mapclassify.list

%changelog

%autochangelog
