%global source0_hash 82377eae21716165f2b0b6b632b4c7eddfc0ccf841f378bf6e5401867eb09faa
%global pypi_name orderly-set
%global pypi_version 5.5.0
Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A package containing multiple implementations of Ordered Set
License:        MIT
URL:            https://github.com/seperman/orderly-set
Source0:        https://github.com/seperman/orderly-set/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-orderly-set = %{version}-%{release}
# /oreon:deps
%package -n       python3-orderly-set+coverage
Summary:        Metapackage for python3-orderly-set coverage extras
Requires:       python3-orderly-set = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.6.0
Provides:       python3dist(orderly-set[coverage]) = %{version}-%{release}

%description -n python3-orderly-set+coverage
Metapackage for python3-orderly-set coverage extras.

%package -n       python3-orderly-set+dev
Summary:        Metapackage for python3-orderly-set dev extras
Requires:       python3-orderly-set = %{version}-%{release}
Requires:       python3dist(bump2version) >= 1.0.0
Requires:       python3dist(ipdb) >= 0.13.0
Provides:       python3dist(orderly-set[dev]) = %{version}-%{release}

%description -n python3-orderly-set+dev
Metapackage for python3-orderly-set dev extras.

%package -n       python3-orderly-set+static
Summary:        Metapackage for python3-orderly-set static extras
Requires:       python3-orderly-set = %{version}-%{release}
Requires:       python3dist(flake8) >= 7.1.0
Requires:       python3dist(flake8-pyproject) >= 1.2.3
Provides:       python3dist(orderly-set[static]) = %{version}-%{release}

%description -n python3-orderly-set+static
Metapackage for python3-orderly-set static extras.

%package -n       python3-orderly-set+test
Summary:        Metapackage for python3-orderly-set test extras
Requires:       python3-orderly-set = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.3.0
Requires:       python3dist(pytest-benchmark) >= 5.1.0
Requires:       python3dist(pytest-cov) >= 6.0.0
Requires:       python3dist(python-dotenv) >= 1.0.0
Provides:       python3dist(orderly-set[test]) = %{version}-%{release}

%description -n python3-orderly-set+test
Metapackage for python3-orderly-set test extras.

%package -n       python3-orderly-set+optimize
Summary:        Metapackage for python3-orderly-set optimize extras
Requires:       python3-orderly-set = %{version}-%{release}
Provides:       python3dist(orderly-set[optimize]) = %{version}-%{release}

%description -n python3-orderly-set+optimize
Metapackage for python3-orderly-set optimize extras.

%description
Orderly Set is a package containing multiple implementations of
Ordered Set.

%package -n     python3-%{pypi_name}
Summary:        A package containing multiple implementations of Ordered Set
%description -n python3-%{pypi_name}
Orderly Set is a package containing multiple implementations
of Ordered Set.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n orderly-set-%{pypi_version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/orderly_set* usr/lib64/python3*/site-packages/orderly_set* usr/bin/*

%check

%pytest
%files
%files -n python3-orderly-set -f %{oreon_filedir}/python3-orderly-set.list

%changelog

%autochangelog
