# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ce50fc533ac02f489a2b183a0c156672c376ecb2091b1127bc7efba2975fff27
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond pyjwt 1
%bcond reauth 0

%if 0%{?rhel}
%bcond grpcio 0
%bcond tests 0
%else
%bcond grpcio 0
%bcond tests 0
%endif

%bcond pytest_localserver %[ %{undefined el10} && %{undefined el9} ]

Name:           python-google-auth
Version:        2.59.1
Release:        1%{?dist}
Epoch:          1
Summary:        Google Authentication Library

License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth
Source0:        %{pypi_source google_auth}

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

%if %{with grpcio}
BuildRequires:  %{py3_dist grpcio}
%endif

%if %{with tests}
BuildRequires:  %{py3_dist certifi}
%endif

%global common_description %{expand:
This library simplifies using Google’s various server-to-server authentication
mechanisms to access Google APIs.}

%description %{common_description}

%package -n python3-google-auth
Summary:       %{summary}

%description -n python3-google-auth %{common_description}

%pyproject_extras_subpkg -n python3-google-auth aiohttp
%pyproject_extras_subpkg -n python3-google-auth enterprise_cert
%pyproject_extras_subpkg -n python3-google-auth pyopenssl
%if %{with pyjwt}
%pyproject_extras_subpkg -n python3-google-auth pyjwt
%endif
%if %{with reauth}
%pyproject_extras_subpkg -n python3-google-auth reauth
%endif
%pyproject_extras_subpkg -n python3-google-auth requests
%pyproject_extras_subpkg -n python3-google-auth urllib3

%prep
%oreon_sha256
%autosetup -p1 -n google_auth-%{version}

find tests* -type f -name '*.py' -exec \
    sed -r -i -e 's/^(from )(mock)\b/\1unittest\.\2/' \
        -e 's/^(import mock)/from unittest \1/' '{}' '+'
sed -r -i 's/^([[:blank:]]*)("mock",)$/\1# \2/' setup.py

%if %{without pyjwt}
sed -r -i 's/^([[:blank:]]*)(\*pyjwt_extra_require,)$/\1# \2/' setup.py
%endif
%if %{without reauth}
sed -r -i 's/^([[:blank:]]*)(\*reauth_extra_require,)$/\1# \2/' setup.py
%endif

%if %{without pytest_localserver}
sed -r -i 's/^([[:blank:]]*)("pytest-localserver\b[^"]*",)$/\1# \2/' setup.py
%endif

sed -r -i 's/^([[:blank:]]*"(pyopenssl|aiohttp))\b[^"]+(",)$/\1\3/' setup.py

%if %{defined el9}
sed -r -i 's/^([[:blank:]]*"cryptography) >= [^"]+(",)$/\1\2/' setup.py
%endif

%generate_buildrequires
%{pyproject_buildrequires \
  -x aiohttp \
  -x enterprise_cert \
  -x pyopenssl \
%if %{with grpcio}
  -x grpc \
%endif
%if %{with pyjwt}
  -x pyjwt \
%endif
%if %{with reauth}
  -x reauth \
%endif
  -x requests \
%if %{with tests}
  -x testing \
%endif
  -x urllib3}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l google

%check
%if %{with grpcio}
%pyproject_check_import
%else
%pyproject_check_import -e google.auth.transport.grpc
%endif

%if %{with tests}
ignore="${ignore-} --ignore=samples/cloud-client/snippets/snippets_test.py"

ignore="${ignore-} --ignore=system_tests"

%if %{without pyjwt}
k="${k-}${k+ and }not test_verify_token_jwk"
%endif

%if %{without reauth}
ignore="${ignore-} --ignore=tests/oauth2/test_challenges.py"
%endif

%if %{without pytest_localserver}
ignore="${ignore-} --ignore=tests/transport/compliance.py"
ignore="${ignore-} --ignore=tests/transport/test__http_client.py"
ignore="${ignore-} --ignore=tests/transport/test_requests.py"
ignore="${ignore-} --ignore=tests/transport/test_urllib3.py"
ignore="${ignore-} --ignore=tests_async/transport/async_compliance.py"
ignore="${ignore-} --ignore=tests_async/transport/test_aiohttp_requests.py"
%endif

k="${k-}${k+ and }not (TestRequestResponse and test_unsupported_session)"
k="${k-}${k+ and }not (TestAuthorizedSession and test_constructor)"
k="${k-}${k+ and }not (TestAuthorizedSession and test_constructor_with_auth_request)"

k="${k-}${k+ and }not (TestDecryptPrivateKey and test_success)"

%if %{defined el9}

k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_request_provided_auth_request_success)"

k="${k-}${k+ and }not (TestTimeoutGuard and test_timeout_with_simple_async_task_within_bounds)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_delete_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_get_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_patch_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_post_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_put_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_request_default_auth_request_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_request_provided_auth_request_success)"
%endif

%pytest ${ignore-} -k "${k-}" -v
%endif

%files -n python3-google-auth -f %{pyproject_files}

%changelog
%autochangelog
