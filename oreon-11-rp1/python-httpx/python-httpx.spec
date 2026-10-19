%global source0_hash 61fe412dd34b6d95197feb9dbfb6a6e2c749197b67287b2f75925ec257bb41ae
%bcond tests 1
Name:           python-httpx
Version:        0.28.1
Release:        1%{?dist}
Summary:        Next-generation HTTP client for Python
License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
Source0:        https://github.com/encode/httpx/archive/%{version}/httpx-%{version}.tar.gz
Patch:          %{url}/pull/3773.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-httpx = %{version}-%{release}
# /oreon:deps
%package -n       python3-httpx+brotli
Summary:        Metapackage for python3-httpx brotli extras
Requires:       python3-httpx = %{version}-%{release}
Provides:       python3dist(httpx[brotli]) = %{version}-%{release}

%description -n python3-httpx+brotli
Metapackage for python3-httpx brotli extras.

%package -n       python3-httpx+cli
Summary:        Metapackage for python3-httpx cli extras
Requires:       python3-httpx = %{version}-%{release}
Requires:       python3dist(click) == 8.*
Requires:       python3dist(pygments) == 2.*
Requires:       python3dist(rich) >= 10
Requires:       python3dist(rich) < 14
Provides:       python3dist(httpx[cli]) = %{version}-%{release}

%description -n python3-httpx+cli
Metapackage for python3-httpx cli extras.

%package -n       python3-httpx+http2
Summary:        Metapackage for python3-httpx http2 extras
Requires:       python3-httpx = %{version}-%{release}
Requires:       python3dist(h2) >= 3
Requires:       python3dist(h2) < 5
Provides:       python3dist(httpx[http2]) = %{version}-%{release}

%description -n python3-httpx+http2
Metapackage for python3-httpx http2 extras.

%package -n       python3-httpx+socks
Summary:        Metapackage for python3-httpx socks extras
Requires:       python3-httpx = %{version}-%{release}
Requires:       python3dist(socksio) == 1.*
Provides:       python3dist(httpx[socks]) = %{version}-%{release}

%description -n python3-httpx+socks
Metapackage for python3-httpx socks extras.

%package -n       python3-httpx+zstd
Summary:        Metapackage for python3-httpx zstd extras
Requires:       python3-httpx = %{version}-%{release}
Requires:       python3dist(zstandard) >= 0.18.0
Provides:       python3dist(httpx[zstd]) = %{version}-%{release}

%description -n python3-httpx+zstd
Metapackage for python3-httpx zstd extras.

%description

%package -n     python3-httpx
Summary:        Next-generation HTTP client for Python
# oreon:reqs
Requires:       python3dist(httpcore) == 1.*
# /oreon:reqs
%description -n python3-httpx
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%{_bindir}/httpx
%{_mandir}/man1/httpx.1*

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n httpx-%{version} -p1
# allow newer rich
# upstream bumps this version by version (see e.g. https://github.com/encode/httpx/pull/3541)
sed -i 's/rich>=10,<14/rich>=10/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    PATH="${PATH-}:%{buildroot}%{_bindir}" \
    PYTHONDONTWRITEBYTECODE=1 \
    help2man --no-info --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/httpx.1' httpx
%oreon_autofiles python3-httpx usr/lib/python3*/site-packages/httpx* usr/lib64/python3*/site-packages/httpx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httpx* usr/lib64/python3*/site-packages/httpx* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
k="${k-}${k+ and }not client"
k="${k-}${k+ and }not test_api"
k="${k-}${k+ and }not test_config"
k="${k-}${k+ and }not test_exceptions"
k="${k-}${k+ and }not test_main"
k="${k-}${k+ and }not test_timeouts"
k="${k-}${k+ and }not test_utils"
%pytest -m 'not network' -k "${k-}" -v
%endif
%files
%files -n python3-httpx -f %{oreon_filedir}/python3-httpx.list

%changelog

%autochangelog
