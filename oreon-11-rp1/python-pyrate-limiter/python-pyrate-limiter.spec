%global source0_hash 098345fff3a52b84dee9bcf6973f184c8b3ef8d34e1f4f781ac0773e3984598b
Name:           python-pyrate-limiter
Version:        4.5.0
Release:        1%{?dist}
Summary:        Python rate limiter with pluggable algorithms and backends
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
Source0:        https://files.pythonhosted.org/packages/source/p/pyrate_limiter/pyrate_limiter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyrate-limiter = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyrate-limiter+redis
Summary:        Metapackage for python3-pyrate-limiter redis extras
Requires:       python3-pyrate-limiter = %{version}-%{release}
Requires:       python3dist(redis) >= 6.2.0
Provides:       python3dist(pyrate-limiter[redis]) = %{version}-%{release}

%description -n python3-pyrate-limiter+redis
Metapackage for python3-pyrate-limiter redis extras.

%package -n       python3-pyrate-limiter+postgres
Summary:        Metapackage for python3-pyrate-limiter postgres extras
Requires:       python3-pyrate-limiter = %{version}-%{release}
Requires:       python3dist(psycopg[pool]) >= 3.2.9
Provides:       python3dist(pyrate-limiter[postgres]) = %{version}-%{release}

%description -n python3-pyrate-limiter+postgres
Metapackage for python3-pyrate-limiter postgres extras.

%package -n       python3-pyrate-limiter+filelock
Summary:        Metapackage for python3-pyrate-limiter filelock extras
Requires:       python3-pyrate-limiter = %{version}-%{release}
Requires:       python3dist(filelock) >= 3.0
Provides:       python3dist(pyrate-limiter[filelock]) = %{version}-%{release}

%description -n python3-pyrate-limiter+filelock
Metapackage for python3-pyrate-limiter filelock extras.

%package -n       python3-pyrate-limiter+all
Summary:        Metapackage for python3-pyrate-limiter all extras
Requires:       python3-pyrate-limiter = %{version}-%{release}
Requires:       python3dist(filelock) >= 3.0
Requires:       python3dist(redis) >= 6.2.0
Requires:       python3dist(psycopg[pool]) >= 3.2.9
Provides:       python3dist(pyrate-limiter[all]) = %{version}-%{release}

%description -n python3-pyrate-limiter+all
Metapackage for python3-pyrate-limiter all extras.

%description

%package -n     python3-pyrate-limiter
Summary:        Python rate limiter with pluggable algorithms and backends
%description -n python3-pyrate-limiter

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyrate_limiter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyrate-limiter usr/lib/python3*/site-packages/pyrate_limiter* usr/lib64/python3*/site-packages/pyrate_limiter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyrate_limiter* usr/lib64/python3*/site-packages/pyrate_limiter* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyrate-limiter -f %{oreon_filedir}/python3-pyrate-limiter.list

%changelog

%autochangelog
