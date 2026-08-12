%global source0_hash 1c39ffb3dfc71547f8af88bb247bb9feffc12545b032a882cd245295ac49e845

Name:           python-aiohappyeyeballs
Version:        2.6.1
Release:        %autorelease
Summary:        Happy Eyeballs for asyncio

License:        PSF-2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
# The GitHub archive contains CHANGELOG.md and other ancillary files that the
# PyPI sdist lacks.
Source:         %{url}/archive/v%{version}/aiohappyeyeballs-%{version}.tar.gz

# Downstream-only: remove pytest options for coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-remove-pytest-options-for-coverage-a.patch
# chore(deps-dev): bump pytest-asyncio from 0.26.0 to 1.1.0
# https://github.com/aio-libs/aiohappyeyeballs/pull/181
# Cherry-picked to v2.6.1, without changes to poetry.lock.
Patch:          0001-chore-deps-dev-bump-pytest-asyncio-from-0.26.0-to-1..patch


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}

%global common_description %{expand:
This library exists to allow connecting with Happy Eyeballs (RFC 8305) when you
already have a list of addrinfo and not a DNS name.

The stdlib version of loop.create_connection() will only work when you pass in
an unresolved name which is not a good fit when using DNS caching or resolving
names via another method such as zeroconf.}

%description %{common_description}

%package -n     python3-aiohappyeyeballs
Summary:        %{summary}

%description -n python3-aiohappyeyeballs %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n aiohappyeyeballs-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L aiohappyeyeballs

%check
%pytest

%files -n python3-aiohappyeyeballs -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
