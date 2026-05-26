# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9ee17553b7febd1a0c1253b3b62ab5d79607eb6163c8fb943470a8893c31d4fa
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global pypi_name botocore
%bcond_without tests

Name:           python-%{pypi_name}
# NOTICE - Updating this package requires updating python-boto3
Version:        1.42.70
Release:        1%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        Apache-2.0
URL:            https://github.com/boto/botocore
Source0:        https://files.pythonhosted.org/packages/source/b/botocore/botocore-1.42.70.tar.gz

BuildArch:      noarch

%global _description %{expand:
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        Low-level, data-driven core of boto 3
BuildRequires:  python3-devel
%if %{with tests}
# For tests:
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pytest
%if %{undefined rhel}
BuildRequires:  python3-pytest-xdist
%endif
%endif
Provides:       bundled(python3-six) = 1.16.0
Provides:       bundled(python3-requests) = 2.7.0

%description -n python3-%{pypi_name} %{_description}

%prep
%oreon_verify_sources
%autosetup -n %{pypi_name}-%{version} -p1
# Remove online tests
rm -vr tests/integration
# This test tried to import tests/cmd-runner which failed as the code was
# unable to import "botocore". I'm not 100% sure why this happened but for now
# just exclude this one test and run all the other functional tests.
rm -vr tests/functional/leak

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%if %{with tests}
# test_lru_cache_weakref fails with Python 3.14 - temporarily skip
# Reported: https://github.com/boto/botocore/issues/3482
%pytest %{!?rhel:-n auto} -k "not test_lru_cache_weakref"
%else
%pyproject_check_import -e botocore.crt.auth -e botocore.vendored*
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.42.70-1
- Prepare for Oreon 11 (RP1)
