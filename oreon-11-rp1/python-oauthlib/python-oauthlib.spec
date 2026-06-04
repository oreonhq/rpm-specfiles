%global source0_hash eb93759adad48251a472c5d20fbce3e08ee53fcec2909a22448d48c9fa100ea0

# RHEL does not include pyjwt, blinker needed for extras
%bcond extras %{undefined rhel}

Name:               python-oauthlib
Version:            3.3.1
Release:            1%{?dist}
Summary:            An implementation of the OAuth request-signing logic

License:            BSD-3-Clause
URL:                https://github.com/oauthlib/oauthlib

Source0:        https://github.com/oauthlib/oauthlib/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:          noarch

%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%package -n python3-oauthlib
Summary:            %{summary}

BuildRequires:      python3-devel
BuildRequires:      python3-pytest

%description -n python3-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%if %{with extras}
%pyproject_extras_subpkg -n python3-oauthlib rsa,signedtoken,signals
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n oauthlib-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_extras:-x rsa,signedtoken,signals}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files oauthlib

%check
# enable SHA-1 signatures for RSA tests
# also see https://github.com/pyca/cryptography/pull/6931 and rhbz#2060343
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
%if %{without extras}
echo 'import pytest; __getattr__ = lambda _: pytest.skip("this test needs jwt")' > jwt.py
%endif
%{pytest} \
%if %{without extras}
  --ignore tests/oauth1/rfc5849/test_signatures.py \
  --ignore tests/oauth2/rfc6749/clients/test_service_application.py \
  --ignore tests/oauth2/rfc6749/clients/test_web_application.py \
  --ignore tests/oauth2/rfc6749/clients/test_mobile_application.py \
  --ignore tests/oauth2/rfc6749/clients/test_legacy_application.py \
  --ignore tests/oauth2/rfc6749/clients/test_backend_application.py \
  --ignore tests/oauth2/rfc6749/test_parameters.py \
%endif
  %{nil}

%files -n python3-oauthlib -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.1-1
- Prepare for Oreon 11 (RP1)
