%global source0_hash 41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703

%global srcname anyio

%global common_description %{expand:
AnyIO is an asynchronous networking and concurrency library that works on top
of either asyncio or trio.  It implements trio-like structured concurrency (SC)
on top of asyncio, and works in harmony with the native SC of trio itself.}

Name:           python-%{srcname}
Version:        4.12.1
Release:        3%{?dist}
Summary:        Compatibility layer for multiple asynchronous event loop implementations
License:        MIT
URL:            https://github.com/agronholm/anyio
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  tomcli
BuildRequires:	python3dist(trustme) >= 1

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
# We could perhaps generate PDF documentation as a substitute, but instead we
# simply drop the -doc subpackage.
Obsoletes:      python-%{srcname}-doc < 3.7.1-7

%description -n python3-%{srcname} %{common_description}

%pyproject_extras_subpkg -n python3-%{srcname} trio

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# - Disable coverage test requirement
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# - Drop test dependency on python3dist(truststore), not packaged
# - Drop test dependency on python3dist(uvloop), packaged but outdated and
#   FTBFS, https://bugzilla.redhat.com/show_bug.cgi?id=2307494,
#   https://bugzilla.redhat.com/show_bug.cgi?id=2341233
# = Drop test dependency on blockbuster; see
#   https://github.com/cbornet/blockbuster/issues/46 for why we would prefer
#   not to package it
tomcli set pyproject.toml lists delitem \
    dependency-groups.test '(blockbuster|coverage|truststore|uvloop)\b.*'

%generate_buildrequires
%pyproject_buildrequires -x trio -g test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# https://github.com/agronholm/anyio/pull/1020#issuecomment-3477923712
k="${k-}${k+ and }not (TestCapacityLimiter and test_bad_init_value[trio])"

%if v"0%{?python3_version}" >= v"3.15"
# https://github.com/agronholm/anyio/issues/1061
k="${k-}${k+ and }not (TestPath and test_properties)"
k="${k-}${k+ and }not (TestPath and test_is_reserved)"
%endif

%pytest -Wdefault -m "not network" -k "${k-}" -rsx -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
