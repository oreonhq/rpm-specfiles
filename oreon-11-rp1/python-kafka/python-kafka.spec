%global source0_hash 6664428c18c61f23d76077269d83c01a56e32f14560b31d9df7eaa7585532830

# tests are enabled by default
%bcond_without test

%global mod_name kafka
%global project_name %{mod_name}-python
%global with_doc 1

Name:             python-%{mod_name}
Version:          2.2.15
Release:          5%{?dist}
Summary:          Pure Python client for Apache Kafka

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://github.com/dpkp/%{project_name}
Source0:          https://github.com/dpkp/%{project_name}/archive/refs/tags/%{version}.tar.gz
# License file for jslibs using in -doc subpkg
Source1:          LICENSE_doc

BuildArch:        noarch
BuildRequires:    pyproject-rpm-macros
BuildRequires:    python3-devel
BuildRequires:    python3-pip
BuildRequires:    python3-wheel

%if %{with test}
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-mock
BuildRequires:    python3-pytest-timeout
BuildRequires:    python3-snappy
BuildRequires:    python3-lz4
BuildRequires:    python3-zstandard
BuildRequires:    python3-xxhash
%endif

%global _description %{expand:
This module provides low-level protocol support for Apache Kafka as well as
high-level consumer and producer classes. Request batching is supported by the
protocol as well as broker-aware request routing. Gzip and Snappy compression
is also supported for message sets.}

%description %{_description}

%package -n python3-%{mod_name}
Summary:          %{summary}

%description -n python3-%{mod_name} %_description

%if %{with_doc}
%package -n python-%{mod_name}-doc
Summary:          Documentation for Pure Python client for Apache Kafka
BuildRequires:    make
BuildRequires:    python3-sphinx_rtd_theme
# BSD for sphinx. MIT for jquery.js and underscore.js.
License:          Apache-2.0 AND BSD-2-Clause AND MIT

%description -n python-%{mod_name}-doc
Documentation for Pure Python client for Apache Kafka.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{project_name}-%{version}
install -m 644 %{SOURCE1} %{_builddir}/%{project_name}-%{version}/LICENSE_doc

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
%if %{with_doc}
%make_build doc
rm -rf docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
install -pm 755 kafka/record/_crc32c.py %{buildroot}/%{python3_sitelib}/%{mod_name}/record/_crc32c.py
# Uses the py3_shebang_fix macro manually because pyproject_install macro
# doesn't automatically changes the Python shebangs.
%py3_shebang_fix %{buildroot}/%{python3_sitelib}/%{mod_name}/record/_crc32c.py
%pyproject_save_files '*' +auto

# Ignores integrational tests requiring network access and tests requiring
# crc32c that is required only for the test and is not packaged in Fedora.
%check
%pytest --ignore="test/record/test_util.py" test

%files -n python3-%{mod_name} -f %{pyproject_files}
%doc AUTHORS.md CHANGES.md README.rst
%license LICENSE

%if %{with_doc}
%files -n python-%{mod_name}-doc
%doc docs/_build/html
%license LICENSE LICENSE_doc
%endif

# LZ4 is an optional compression lib for python-kafka.
# Snappy is an optional compression lib for python-kafka.
%pyproject_extras_subpkg -n python3-kafka lz4 snappy

# ZSTD is an optional compression lib for python-kafka.
# Needs to write the zstd subpackage section manually because
# zstd's extras_requires causes an incorrect dependency.
%package -n python3-%{mod_name}+zstd
Summary: Metapackage for python3-kafka: zstd extras
Requires: python3-kafka = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: python%{python3_version}dist(zstandard)
Provides: python-kafka+zstd = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_version}-kafka+zstd = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_version}dist(kafka-python[zstd]) = %{?epoch:%{epoch}:}%{version}
Provides: python3dist(kafka-python[zstd]) = %{?epoch:%{epoch}:}%{version}

%description -n python3-kafka+zstd
This is a metapackage bringing in zstd extras requires for python3-kafka.
It makes sure the dependencies are installed.

%files -n python3-kafka+zstd

%changelog
%autochangelog
