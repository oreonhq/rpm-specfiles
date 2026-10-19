%global source0_hash d807ceb9bdd6ea7cc0663370dd5568339056b35dc15c26effd1ae267e323acf1
Name:           python-testfixtures
Version:        12.3.0
Release:        1%{?dist}
Summary:        A collection of helpers and mock objects for unit tests and doc tests.
License:        MIT
URL:            https://github.com/Simplistix/testfixtures
Source0:        https://files.pythonhosted.org/packages/source/t/testfixtures/testfixtures-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-testfixtures = %{version}-%{release}
# /oreon:deps
%package -n       python3-testfixtures+django
Summary:        Metapackage for python3-testfixtures django extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(django) >= 4
Requires:       python3dist(django) >= 5.1.3
Provides:       python3dist(testfixtures[django]) = %{version}-%{release}

%description -n python3-testfixtures+django
Metapackage for python3-testfixtures django extras.

%package -n       python3-testfixtures+sybil
Summary:        Metapackage for python3-testfixtures sybil extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(sybil) >= 10.1.0
Provides:       python3dist(testfixtures[sybil]) = %{version}-%{release}

%description -n python3-testfixtures+sybil
Metapackage for python3-testfixtures sybil extras.

%package -n       python3-testfixtures+mock-backport
Summary:        Metapackage for python3-testfixtures mock-backport extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(mock) >= 4.0.3
Provides:       python3dist(testfixtures[mock-backport]) = %{version}-%{release}

%description -n python3-testfixtures+mock-backport
Metapackage for python3-testfixtures mock-backport extras.

%package -n       python3-testfixtures+loguru
Summary:        Metapackage for python3-testfixtures loguru extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(loguru) >= 0.7.3
Provides:       python3dist(testfixtures[loguru]) = %{version}-%{release}

%description -n python3-testfixtures+loguru
Metapackage for python3-testfixtures loguru extras.

%package -n       python3-testfixtures+polars
Summary:        Metapackage for python3-testfixtures polars extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(polars) >= 1.32
Provides:       python3dist(testfixtures[polars]) = %{version}-%{release}

%description -n python3-testfixtures+polars
Metapackage for python3-testfixtures polars extras.

%package -n       python3-testfixtures+pandas
Summary:        Metapackage for python3-testfixtures pandas extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(pandas) >= 2.3.3
Provides:       python3dist(testfixtures[pandas]) = %{version}-%{release}

%description -n python3-testfixtures+pandas
Metapackage for python3-testfixtures pandas extras.

%package -n       python3-testfixtures+numpy
Summary:        Metapackage for python3-testfixtures numpy extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(numpy) >= 2.3.2
Provides:       python3dist(testfixtures[numpy]) = %{version}-%{release}

%description -n python3-testfixtures+numpy
Metapackage for python3-testfixtures numpy extras.

%package -n       python3-testfixtures+structlog
Summary:        Metapackage for python3-testfixtures structlog extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(structlog) >= 24.3.0
Provides:       python3dist(testfixtures[structlog]) = %{version}-%{release}

%description -n python3-testfixtures+structlog
Metapackage for python3-testfixtures structlog extras.

%package -n       python3-testfixtures+pydantic
Summary:        Metapackage for python3-testfixtures pydantic extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(pydantic) >= 2.12.0
Provides:       python3dist(testfixtures[pydantic]) = %{version}-%{release}

%description -n python3-testfixtures+pydantic
Metapackage for python3-testfixtures pydantic extras.

%package -n       python3-testfixtures+twisted
Summary:        Metapackage for python3-testfixtures twisted extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(twisted) >= 22.1
Provides:       python3dist(testfixtures[twisted]) = %{version}-%{release}

%description -n python3-testfixtures+twisted
Metapackage for python3-testfixtures twisted extras.

%package -n       python3-testfixtures+yaml
Summary:        Metapackage for python3-testfixtures yaml extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.3
Provides:       python3dist(testfixtures[yaml]) = %{version}-%{release}

%description -n python3-testfixtures+yaml
Metapackage for python3-testfixtures yaml extras.

%package -n       python3-testfixtures+toml
Summary:        Metapackage for python3-testfixtures toml extras
Requires:       python3-testfixtures = %{version}-%{release}
Requires:       python3dist(tomlkit) >= 0.10.0
Provides:       python3dist(testfixtures[toml]) = %{version}-%{release}

%description -n python3-testfixtures+toml
Metapackage for python3-testfixtures toml extras.

%description

%package -n     python3-testfixtures
Summary:        A collection of helpers and mock objects for unit tests and doc tests.
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.12
# /oreon:reqs
%description -n python3-testfixtures

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir testfixtures-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-testfixtures usr/lib/python3*/site-packages/testfixtures* usr/lib64/python3*/site-packages/testfixtures* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/testfixtures* usr/lib64/python3*/site-packages/testfixtures* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-testfixtures -f %{oreon_filedir}/python3-testfixtures.list

%changelog

%autochangelog
