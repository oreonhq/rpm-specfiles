%global source0_hash 7866dd5b4af551d188b9cda3fab530f1d52af0abc1ad383dbfdd421d03f8d9ba
%global extras daphne,uvicorn,examples
Name:           python-sse-starlette
Version:        3.4.11
Release:        1%{?dist}
Summary:        SSE plugin for Starlette
License:        BSD-3-Clause
URL:            https://github.com/sysid/sse-starlette
Source0:        https://github.com/sysid/sse-starlette/archive/v%{version}/sse-starlette-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sse-starlette = %{version}-%{release}
# /oreon:deps
%package -n       python3-sse-starlette+examples
Summary:        Metapackage for python3-sse-starlette examples extras
Requires:       python3-sse-starlette = %{version}-%{release}
Requires:       python3dist(uvicorn) >= 0.34.0
Requires:       python3dist(fastapi) >= 0.115.12
Requires:       python3dist(pydantic) >= 2
Provides:       python3dist(sse-starlette[examples]) = %{version}-%{release}

%description -n python3-sse-starlette+examples
Metapackage for python3-sse-starlette examples extras.

%package -n       python3-sse-starlette+examples-db
Summary:        Metapackage for python3-sse-starlette examples-db extras
Requires:       python3-sse-starlette = %{version}-%{release}
Requires:       python3dist(sqlalchemy[asyncio]) >= 2.0.41
Requires:       python3dist(aiosqlite) >= 0.21.0
Provides:       python3dist(sse-starlette[examples-db]) = %{version}-%{release}

%description -n python3-sse-starlette+examples-db
Metapackage for python3-sse-starlette examples-db extras.

%package -n       python3-sse-starlette+uvicorn
Summary:        Metapackage for python3-sse-starlette uvicorn extras
Requires:       python3-sse-starlette = %{version}-%{release}
Requires:       python3dist(uvicorn) >= 0.34.0
Provides:       python3dist(sse-starlette[uvicorn]) = %{version}-%{release}

%description -n python3-sse-starlette+uvicorn
Metapackage for python3-sse-starlette uvicorn extras.

%package -n       python3-sse-starlette+granian
Summary:        Metapackage for python3-sse-starlette granian extras
Requires:       python3-sse-starlette = %{version}-%{release}
Requires:       python3dist(granian) >= 2.3.1
Provides:       python3dist(sse-starlette[granian]) = %{version}-%{release}

%description -n python3-sse-starlette+granian
Metapackage for python3-sse-starlette granian extras.

%package -n       python3-sse-starlette+daphne
Summary:        Metapackage for python3-sse-starlette daphne extras
Requires:       python3-sse-starlette = %{version}-%{release}
Requires:       python3dist(daphne) >= 4.2.0
Provides:       python3dist(sse-starlette[daphne]) = %{version}-%{release}

%description -n python3-sse-starlette+daphne
Metapackage for python3-sse-starlette daphne extras.

%description

%package -n     python3-sse-starlette
Summary:        SSE plugin for Starlette
# oreon:reqs
Requires:       python3dist(anyio) >= 4.7.0
Requires:       python3dist(starlette) >= 0.49.1
# /oreon:reqs
%description -n python3-sse-starlette

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sse-starlette-%{version} -p1

# Relax daphne dependency
tomcli set pyproject.toml arrays replace project.optional-dependencies.daphne "daphne>=([0-9]+\.[0-9]+\.[0-9]+)" "daphne>=4.1,<4.3"

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sse-starlette usr/lib/python3*/site-packages/sse_starlette* usr/lib64/python3*/site-packages/sse_starlette* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sse_starlette* usr/lib64/python3*/site-packages/sse_starlette* usr/bin/*

%check

%pyproject_check_import
%pytest --ignore tests/integration/test_multiple_consumers.py
%files
%files -n python3-sse-starlette -f %{oreon_filedir}/python3-sse-starlette.list

%changelog

%autochangelog
