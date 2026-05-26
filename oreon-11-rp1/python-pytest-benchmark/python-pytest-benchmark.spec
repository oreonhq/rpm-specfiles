# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 85418c186ac26a9f3cc15d255cd40bb145f8681d0fca044768dd50fa05c8aafe
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global srcname pytest-benchmark

Name: python-%{srcname}
Version: 5.1.0
Release: 5%{?dist}
Summary: A py.test fixture for benchmarking code
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://pytest-benchmark.readthedocs.io
Source: https://github.com/ionelmc/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
This plugin provides a benchmark fixture. This fixture is a callable object
that will benchmark any function passed to it.

Notable features and goals:

  - Sensible defaults and automatic calibration for microbenchmarks
  - Good integration with pytest
  - Comparison and regression tracking
  - Exhausive statistics
  - JSON export}

%description %_description

%package -n python3-%{srcname}
Summary: %summary
Requires: python3-pytest
Requires: python3-cpuinfo

%description -n python3-%{srcname} %_description

%prep
%oreon_verify_sources
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_benchmark

%check
# Tests disabled due to missing dependencies
#%%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst AUTHORS.rst
%{_bindir}/py.test-benchmark
%{_bindir}/pytest-benchmark

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-5
- Prepare for Oreon 11 (RP1)
