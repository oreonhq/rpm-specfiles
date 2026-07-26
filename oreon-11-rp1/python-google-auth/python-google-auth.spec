%global source0_hash 6db96de728bfd7451602509234fbf4126da2b80e78bb780cc2a81ee023639d72

# Not packaged: python-pyjwt
%bcond pyjwt 0
# Not packaged: python-pyu2f
%bcond reauth 0
# Since grpc is a challenging package, it’s helpful to maintain the ability to
# break this dependency.

%if 0%{?rhel}
%bcond grpcio 0
%bcond tests 0
%else
%bcond grpcio 1
%bcond tests 1
%endif

%bcond pytest_localserver %[ %{undefined el10} && %{undefined el9} ]

Name:           python-google-auth
Version:        2.47.0
Release:        1%{?dist}
Epoch:          1
Summary:        Google Authentication Library

License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python
Source:         %{url}/archive/v%{version}/google-auth-library-python-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with grpcio}
# For import-checking google.auth.transport.grpc; see also
# https://github.com/googleapis/google-auth-library-python/issues/1735.
BuildRequires:  %{py3_dist grpcio}
%endif

%if %{with tests}
# Some tests in tests/transport/test_requests.py and
# tests/transport/test_urllib3.py require this.
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n google-auth-library-python-%{version}

# use unittest.mock instead of mock
# https://github.com/googleapis/google-auth-library-python/issues/1055
#
# Needed for https://fedoraproject.org/wiki/Changes/DeprecatePythonMock.
#
# See also https://github.com/googleapis/google-auth-library-python/pull/1786,
# https://github.com/googleapis/google-auth-library-python/pull/1361, but these
# are out of date and upstream has failed to act for months, so we use a more
# “dynamic” sed-patch to avoid constant rebasing
find tests* system_tests -type f -name '*.py' -exec \
    sed -r -i -e 's/^(from )(mock)\b/\1unittest\.\2/' \
        -e 's/^(import mock)/from unittest \1/' '{}' '+'
sed -r -i 's/^([[:blank:]]*)("mock",)$/\1# \2/' setup.py

# Upstream expands dependencies for extras into the testing extra. Omit any
# missing extras from the testing extra.
%if %{without pyjwt}
sed -r -i 's/^([[:blank:]]*)(\*pyjwt_extra_require,)$/\1# \2/' setup.py
%endif
%if %{without reauth}
sed -r -i 's/^([[:blank:]]*)(\*reauth_extra_require,)$/\1# \2/' setup.py
%endif

%if %{without pytest_localserver}
sed -r -i 's/^([[:blank:]]*)("pytest-localserver\b[^"]*",)$/\1# \2/' setup.py
%endif

# We cannot respect version upper bounds that were added for testing:
#   "pyopenssl < 24.3.0",
#   "aiohttp < 3.10.0",
sed -r -i 's/^([[:blank:]]*"(pyopenssl|aiohttp))\b[^"]+(",)$/\1\3/' setup.py

%if %{defined el9}
# We must loosen the lower bound on the cryptography version.
sed -r -i 's/^([[:blank:]]*"cryptography) >= [^"]+(",)$/\1\2/' setup.py
%endif

%generate_buildrequires
%{pyproject_buildrequires \
  -x aiohttp \
  -x enterprise_cert \
  -x pyopenssl \
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
# Requires python-google-cloud-storage, which we don’t really want to add as a
# build dependency.
ignore="${ignore-} --ignore=samples/cloud-client/snippets/snippets_test.py"

# Require additional test data files not in the repository:
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

# TODO: What would it take to fix these?
#   >       loop = loop or asyncio.get_running_loop()
#   E       RuntimeError: no running event loop
k="${k-}${k+ and }not (TestRequestResponse and test_unsupported_session)"
k="${k-}${k+ and }not (TestAuthorizedSession and test_constructor)"
k="${k-}${k+ and }not (TestAuthorizedSession and test_constructor_with_auth_request)"

# TestDecryptPrivateKey::test_success fails with pyOpenSSL 24.3.0+ #1665
# https://github.com/googleapis/google-auth-library-python/issues/1665
k="${k-}${k+ and }not (TestDecryptPrivateKey and test_success)"

%if %{defined el9}
# TODO: We have not tried to investigate these EPEL9-specific failures.

#   ERROR at teardown of TestAsyncAuthorizedSession.test_request_provided_auth_request_success _
#   […]
#   E           ValueError: Async generator fixture didn't stop.Yield only once.
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_request_provided_auth_request_success)"

# E           TypeError: object bool can't be used in 'await' expression
k="${k-}${k+ and }not (TestTimeoutGuard and test_timeout_with_simple_async_task_within_bounds)"
# E           TypeError: object Mock can't be used in 'await' expression
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_delete_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_get_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_patch_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_post_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_http_put_method_success)"
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_request_default_auth_request_success)"
# E       TypeError: 'async for' requires an object with __aiter__ method, got bytes
k="${k-}${k+ and }not (TestAsyncAuthorizedSession and test_request_provided_auth_request_success)"
%endif

%pytest ${ignore-} -k "${k-}" -v
%endif

%files -n python3-google-auth -f %{pyproject_files}

%changelog
%autochangelog
