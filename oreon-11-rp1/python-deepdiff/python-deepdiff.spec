%global source0_hash 07e9e366fab4297755153c4eab795ad4ef3cbd0d51660e847f5751c6bd727687
Name:           python-deepdiff
Version:        9.1.0
Release:        1%{?dist}
Summary:        Deep Difference and Search of any Python object/data. Recreate objects by adding adding deltas to each other.
License:        MIT
URL:            https://zepworks.com/deepdiff/
Source0:        https://files.pythonhosted.org/packages/source/d/deepdiff/deepdiff-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-deepdiff = %{version}-%{release}
# /oreon:deps
%package -n       python3-deepdiff+coverage
Summary:        Metapackage for python3-deepdiff coverage extras
Requires:       python3-deepdiff = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.13.5
Provides:       python3dist(deepdiff[coverage]) = %{version}-%{release}

%description -n python3-deepdiff+coverage
Metapackage for python3-deepdiff coverage extras.

%package -n       python3-deepdiff+cli
Summary:        Metapackage for python3-deepdiff cli extras
Requires:       python3-deepdiff = %{version}-%{release}
Requires:       python3dist(click) >= 8.3.1
Requires:       python3dist(pyyaml) >= 6.0.3
Provides:       python3dist(deepdiff[cli]) = %{version}-%{release}

%description -n python3-deepdiff+cli
Metapackage for python3-deepdiff cli extras.

%package -n       python3-deepdiff+dev
Summary:        Metapackage for python3-deepdiff dev extras
Requires:       python3-deepdiff = %{version}-%{release}
Requires:       python3dist(bump2version) >= 1.0.1
Requires:       python3dist(jsonpickle) >= 4.1.1
Requires:       python3dist(ipdb) >= 0.13.13
Requires:       python3dist(numpy) >= 2.4.3
Requires:       python3dist(numpy) >= 2.2.0
Requires:       python3dist(python-dateutil) >= 2.9.0.post0
Requires:       python3dist(orjson) >= 3.11.7
Requires:       python3dist(tomli) >= 2.4.0
Requires:       python3dist(tomli-w) >= 1.2.0
Requires:       python3dist(pandas) >= 3.0.1
Requires:       python3dist(pandas) >= 2.2.0
Requires:       python3dist(polars) >= 1.39.3
Requires:       python3dist(nox) == 2026.2.9
Requires:       python3dist(uuid6) == 2025.0.1
Requires:       python3dist(flit-core) == 3.12.0
Provides:       python3dist(deepdiff[dev]) = %{version}-%{release}

%description -n python3-deepdiff+dev
Metapackage for python3-deepdiff dev extras.

%package -n       python3-deepdiff+docs
Summary:        Metapackage for python3-deepdiff docs extras
Requires:       python3-deepdiff = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.1.3
Requires:       python3dist(sphinx-sitemap) >= 2.9.0
Requires:       python3dist(sphinxemoji) >= 0.3.2
Requires:       python3dist(furo) >= 2024.8.6
Provides:       python3dist(deepdiff[docs]) = %{version}-%{release}

%description -n python3-deepdiff+docs
Metapackage for python3-deepdiff docs extras.

%package -n       python3-deepdiff+static
Summary:        Metapackage for python3-deepdiff static extras
Requires:       python3-deepdiff = %{version}-%{release}
Requires:       python3dist(flake8) >= 7.3.0
Requires:       python3dist(flake8-pyproject) >= 1.2.4
Requires:       python3dist(pydantic) >= 2.12.5
Provides:       python3dist(deepdiff[static]) = %{version}-%{release}

%description -n python3-deepdiff+static
Metapackage for python3-deepdiff static extras.

%package -n       python3-deepdiff+test
Summary:        Metapackage for python3-deepdiff test extras
Requires:       python3-deepdiff = %{version}-%{release}
Requires:       python3dist(pytest) >= 9.0.3
Requires:       python3dist(pytest-benchmark) >= 5.2.3
Requires:       python3dist(pytest-cov) >= 7.1.0
Requires:       python3dist(python-dotenv) >= 1.2.2
Provides:       python3dist(deepdiff[test]) = %{version}-%{release}

%description -n python3-deepdiff+test
Metapackage for python3-deepdiff test extras.

%package -n       python3-deepdiff+optimize
Summary:        Metapackage for python3-deepdiff optimize extras
Requires:       python3-deepdiff = %{version}-%{release}
Provides:       python3dist(deepdiff[optimize]) = %{version}-%{release}

%description -n python3-deepdiff+optimize
Metapackage for python3-deepdiff optimize extras.

%description

%package -n     python3-deepdiff
Summary:        Deep Difference and Search of any Python object/data. Recreate objects by adding adding deltas to each other.
# oreon:reqs
Requires:       python3dist(cachebox) < 6
Requires:       python3dist(cachebox) >= 5.2
Requires:       python3dist(orderly-set) < 6
Requires:       python3dist(orderly-set) >= 5.5.0
# /oreon:reqs
%description -n python3-deepdiff

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir deepdiff-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-deepdiff usr/lib/python3*/site-packages/deepdiff* usr/lib64/python3*/site-packages/deepdiff* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/deepdiff* usr/lib64/python3*/site-packages/deepdiff* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-deepdiff -f %{oreon_filedir}/python3-deepdiff.list

%changelog

%autochangelog
