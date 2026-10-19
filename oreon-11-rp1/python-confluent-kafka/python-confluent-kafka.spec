%global source0_hash 99d1223020e27854e75981333983c5120d64762268f8afcc805fbd62e7de49aa
Name:           python-confluent-kafka
Version:        2.15.1
Release:        1%{?dist}
Summary:        Confluent_s Python client for Apache Kafka
License:        ...
URL:            https://github.com/confluentinc/confluent-kafka-python
Source0:        https://files.pythonhosted.org/packages/source/c/confluent_kafka/confluent_kafka-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62
Requires:       python3-confluent-kafka = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-confluent-kafka
Summary:        Confluent_s Python client for Apache Kafka
%description -n python3-confluent-kafka

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir confluent_kafka-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-confluent-kafka usr/lib/python3*/site-packages/confluent_kafka* usr/lib64/python3*/site-packages/confluent_kafka* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/confluent_kafka* usr/lib64/python3*/site-packages/confluent_kafka* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-confluent-kafka -f %{oreon_filedir}/python3-confluent-kafka.list

%changelog

%autochangelog
