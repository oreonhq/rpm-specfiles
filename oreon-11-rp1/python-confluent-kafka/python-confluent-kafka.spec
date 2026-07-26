%global source0_hash 201c6182304c5864c8a1b1aae2f99bf51fa332017abbec05a3a1fb2ff242c41d

%global sname confluent-kafka
%global pypi_name confluent-kafka

Name:           python-%{sname}
Version:        2.4.0
Release:        6%{?dist}
Summary:        Confluent's Apache Kafka client for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/confluentinc/confluent-kafka-python
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

%description
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%package -n     python3-%{sname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{sname}}
BuildRequires:  gcc
BuildRequires:  librdkafka-devel
BuildRequires:  python3-devel
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# https://github.com/confluentinc/confluent-kafka-python/issues/508
#BuildRequires:  python3dist(pytest)
BuildRequires:  python3-setuptools

Requires:       python3-fastavro
Requires:       python3-requests
Requires:       librdkafka >= 2.4.0
%description -n python3-%{sname}
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{sname}.egg-info

%build
%py3_build

%install
%py3_install
# Remove license file installed in weird place
rm -f  %{buildroot}/%{_prefix}/LICENSE.txt

%check
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# So just import test
%py3_check_import confluent_kafka
#py.test-3 -v --ignore=tests/integration ./tests/

%files -n python3-%{sname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/confluent_kafka
%{python3_sitearch}/confluent_kafka-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
