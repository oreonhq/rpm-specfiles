%global source0_hash 98cc52cdbe058458e945ae87d4fd5a73186497ffa545ee6e98372f8599a5bd34

Name:           python-pyrate-limiter
Version:        2.10.0
Epoch:          1
Release:        %autorelease
Summary:        The request rate limiter using Leaky-bucket algorithm
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
Source0:        %{pypi_source pyrate_limiter}

BuildArch:      noarch
BuildRequires:  python3-devel

# Multiple packages are needed to run tests on this library that are either not packaged for Fedora,
# or are way too old.
# Without those, over 300 tests fail. So I will disable the tests until the situation changes.
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_running_tests
# django-redis = "^5.0.0"
# Currently too old:
# https://bugzilla.redhat.com/show_bug.cgi?id=1445556
# BuildRequires:  %%{py3_dist django-redis} >= 5
# fakeredis = "^1.1.0"
# Not yet packaged:
# BuildRequires:  %%{py3_dist fakeredis} >= 1.1
# pytest-cov = "^4.1.0"
# Too old...
# BuildRequires:  %%{py3_dist pytest-cov} >= 4.1
# Hard dependancy on a specific version of the package (Submitted upstream as a possible problem?)
# coverage = "6"
# BuildRequires:  %%{py3_dist coverage} = 6

%global _description \
The request rate limiter using Leaky-bucket algorithm.

%description %{_description}

%package -n python3-pyrate-limiter
Summary:        %{summary}

%description -n python3-pyrate-limiter %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pyrate_limiter-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyrate_limiter

%check
%pyproject_check_import

%files -n python3-pyrate-limiter -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
