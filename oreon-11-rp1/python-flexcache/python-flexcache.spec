%global source0_hash 18743bd5a0621bfe2cf8d519e4c3bfdf57a269c15d1ced3fb4b64e0ff4600656

Name:           python-flexcache
Version:        0.3
Release:        %autorelease
Summary:        Cache on disk the result of expensive calculations

License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexcache
Source:         %{pypi_source flexcache}

# Increase the value of FS_SLEEP in the tests (fix #4)
# https://github.com/hgrecco/flexcache/pull/5
#
# Fixes:
#
# test_name_by_paths fails flakily on ppc64le and s390x
# https://github.com/hgrecco/flexcache/issues/4
Patch:          %{url}/pull/5.patch

# We remove flexcache.testsuite manually in %%install.

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# See the test extra in pyproject.toml. We list test dependencies manually
# since we do not want pytest-cov
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters)
# and the other pytest plugins are spurious
# (https://github.com/hgrecco/flexacache/pull/3).
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
A robust and extensible package to cache on disk the result of expensive
calculations.}

%description %{common_description}

%package -n python3-flexcache
Summary:        %{summary}

%description -n python3-flexcache %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n flexcache-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flexcache
rm -rvf '%{buildroot}%{python3_sitelib}/flexcache/testsuite'
sed -r -i '/\/flexcache\/testsuite/d' %{pyproject_files}

%check
%pytest

%files -n python3-flexcache -f %{pyproject_files}
%doc README.rst
%doc CHANGES

%changelog
%autochangelog
