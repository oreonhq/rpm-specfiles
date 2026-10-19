%global source0_hash 1eb415c4756210e278675225ff1d6b2659e09f832b567aa35d807a94a311c3f4
%bcond extras %{undefined rhel}
Name:               python-oauthlib
Version:            4.0.0
Release:        1%{?dist}
Summary:        An implementation of the OAuth request-signing logic
License:            BSD-3-Clause
URL:                https://github.com/oauthlib/oauthlib
Source0:        https://github.com/oauthlib/oauthlib/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-oauthlib = %{version}-%{release}
# /oreon:deps
%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%package -n python3-oauthlib
Summary:        An implementation of the OAuth request-signing logic
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
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir oauthlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oauthlib usr/lib/python3*/site-packages/oauthlib* usr/lib64/python3*/site-packages/oauthlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oauthlib* usr/lib64/python3*/site-packages/oauthlib* usr/bin/*

%check

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
%files
%files -n python3-oauthlib -f %{oreon_filedir}/python3-oauthlib.list

%changelog

%autochangelog
