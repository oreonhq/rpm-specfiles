%global source0_hash cd19cfa41fcee212f9ed2499b9368a4cef29e0f0935340e96789d026f78ec0be

%bcond bootstrap 0

%global docs    %[%{without bootstrap} && 0%{?fedora}]
%global giturl  https://github.com/mongodb/mongo-python-driver

Name:           python-pymongo
Version:        4.13.2
Release:        4%{?dist}

License:        Apache-2.0
Summary:        Python driver for MongoDB
URL:            https://pymongo.readthedocs.io/en/stable/
VCS:            git:%{giturl}.git
Source0:        https://github.com/mongodb/mongo-python-driver/archive/4.13.2/pymongo-4.13.2.tar.gz
# Don't fail tests on python 3.14 deprecation warnings
# Downstream patch
Patch0:         pymongo-nonfatal-warnings.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
%if 0%{docs}
BuildRequires:  python3-furo
BuildRequires:  python3-sphinx
%endif

%description
The Python driver for MongoDB.


%package doc
# Apache-2.0: the content.  Other licenses are due to files copied in by Sphinx.
# _static/basic.css: BSD-2-Clause
# _static/debug.css: MIT
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/scripts: MIT
# _static/searchtools.js: BSD-2-Clause
# _static/skeleton.css: MIT
# _static/sphinx_highlight.js: BSD-2-Clause
# _static/styles: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Summary:        Documentation for python-pymongo

%description doc
Documentation for python-pymongo.


%package -n python3-bson
# All code is Apache-2.0 except bson/time64*.{c,h} which is MIT
License:        Apache-2.0 AND MIT
Summary:        Python bson library

%description -n python3-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.  This package
contains the python3 version of this module.


%package -n python3-pymongo
Summary:        Python driver for MongoDB
Requires:       python3-bson%{?_isa} = %{version}-%{release}

%description -n python3-pymongo
The Python driver for MongoDB.  This package contains the python3 version of
this module.


%package -n python3-pymongo-gridfs
Summary:        Python GridFS driver for MongoDB
Requires:       python3-pymongo%{?_isa} = %{version}-%{release}

%description -n python3-pymongo-gridfs
GridFS is a storage specification for large objects in MongoDB.  This package
contains the python3 version of this module.


# Some extras cannot be supported due to missing dependencies:
# - pymongo-auth-aws: needed for aws and encryption extras
# - pymongocrypt: needed for encryption extra
# - pykerberos: needed for gssapi extra
# No snappy on i686
%ifarch %{ix86}
%pyproject_extras_subpkg -n python3-pymongo ocsp zstd
%else
%pyproject_extras_subpkg -n python3-pymongo ocsp snappy zstd
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n mongo-python-driver-%{version} -p1

# Permit use of pytest-asyncio 0.23
sed -i '/pytest-asyncio/s/0\.24\.0/0.23.0/' requirements/test.txt


%generate_buildrequires
%ifarch %{ix86}
%pyproject_buildrequires -x ocsp,test,zstd
%else
%pyproject_buildrequires -x ocsp,snappy,test,zstd
%endif


%build
export PYMONGO_C_EXT_MUST_BUILD=1
%pyproject_wheel

%if 0%{docs}
export PYTHONPATH=$PWD
%make_build -C doc html
rm doc/_build/html/.buildinfo
%endif


%install
%pyproject_install
%pyproject_save_files -L pymongo


%check
# Skip tests that require network/nameservers
%pytest -v \
  --deselect=test/asynchronous/test_client.py::AsyncClientUnitTest::test_connection_timeout_ms_propagates_to_DNS_resolver \
  --deselect=test/asynchronous/test_client.py::AsyncClientUnitTest::test_detected_environment_logging \
  --deselect=test/asynchronous/test_client.py::AsyncClientUnitTest::test_detected_environment_warning \
  --deselect=test/test_client.py::ClientUnitTest::test_connection_timeout_ms_propagates_to_DNS_resolver \
  --deselect=test/test_client.py::ClientUnitTest::test_detected_environment_logging \
  --deselect=test/test_client.py::ClientUnitTest::test_detected_environment_warning \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_10_all_dns_selected \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_11_all_dns_selected \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_12_new_dns_randomly_selected \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_addition \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_dns_failures \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_dns_record_lookup_empty \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_does_not_flipflop \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_empty_seedlist \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_erroring_seedlist \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_removal \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_replace_both_with_one \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_replace_both_with_two \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_replace_one \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_srv_service_name \
  --deselect=test/test_srv_polling.py::TestSrvPolling::test_srv_waits_to_poll \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_10_all_dns_selected \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_11_all_dns_selected \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_12_new_dns_randomly_selected \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_addition \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_dns_failures \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_dns_record_lookup_empty \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_does_not_flipflop \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_empty_seedlist \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_erroring_seedlist \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_removal \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_replace_both_with_one \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_replace_both_with_two \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_replace_one \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_srv_service_name \
  --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_srv_waits_to_poll \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_custom_srvServiceName \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_invalid_type_for_srvMaxHosts \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_negative_integer_for_srvMaxHosts \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_positive_srvMaxHosts_and_loadBalanced=false \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_srvMaxHosts \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_srvMaxHosts=0_and_loadBalanced=true \
  --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_srvMaxHosts=0_and_replicaSet \


%files doc
%license LICENSE
%if 0%{docs}
%doc doc/_build/html/*
%endif


%files -n python3-bson
%license LICENSE
%doc README.md
%{python3_sitearch}/bson


%files -n python3-pymongo -f %{pyproject_files}
%license LICENSE
%doc README.md


%files -n python3-pymongo-gridfs
%license LICENSE
%doc README.md
%{python3_sitearch}/gridfs


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.2-4
- Prepare for Oreon 11 (RP1)
