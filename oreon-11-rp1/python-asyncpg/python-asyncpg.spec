%global source0_hash c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735
%bcond uvloop 0
Name:           python-asyncpg
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Version:        0.31.0
Release:        1%{?dist}
License:        Apache-2.0 AND 0BSD AND PSF-2.0
URL:            https://github.com/MagicStack/asyncpg
Source0:        https://files.pythonhosted.org/packages/source/a/asyncpg/asyncpg-%{version}.tar.gz
%global common_description %{expand:
asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL
server binary protocol for use with Python’s asyncio framework. You can read
more about asyncpg in an introductory blog post
http://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python/.}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  krb5-workstation
BuildRequires:  libpq-devel
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
BuildRequires:  pythoncapi-compat-static
BuildRequires:  tomcli
# /oreon:deps
%description %{common_description}

%package -n     python3-asyncpg
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Obsoletes:      %{name}-doc < 0.27.0-5
%description -n python3-asyncpg %{common_description}

%prep

%autosetup -p1
# Remove pre-generated C sources from Cython to ensure they are re-generated
# and not used in the build. Note that recordobj.c is not a generated source,
# and must not be removed!
find asyncpg -type f -name '*.c' ! -name 'recordobj.c' -print -delete

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem \
    'dependency-groups.test' '(flake8|mypy)\b.*'

# Do not upper-bound the Python interpreter version for the uvloop test
# dependency. First, a missing uvloop breaks the test if we do not adjust the
# uvloop bcond; second, we may have a working python3-uvloop packaged even if
# there is no corresponding binary wheel on PyPI. We use sed since "tomcli set
# ... lists replace ..." only supports a fixed replacement string.
sed -r -i "s/('uvloop\\b.*);.*'/\\1'/" pyproject.toml
%if %{without uvloop}
tomcli set pyproject.toml lists delitem 'dependency-groups.test' '(uvloop)\b.*'
%endif

# Unbundle pythoncapi-compat.
ln -svf /usr/include/pythoncapi_compat.h \
    asyncpg/protocol/record/pythoncapi_compat.h

%build -p

export ASYNCPG_BUILD_CYTHON_ALWAYS=1
%install
%pyproject_install
%oreon_autofiles python3-asyncpg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -rf asyncpg
ln -s %{buildroot}%{python3_sitearch}/asyncpg/
k="${k-}${k+ and }not TestFlake8"
k="${k-}${k+ and }not test_executemany_server_failure_during_writes"
%if v"0%{?python3_version}" >= v"3.15"
k="${k-}${k+ and }not (TestPool and test_pool_handles_transaction_exit_in_asyncgen_2)"
%endif
PYTHONASYNCIODEBUG=1 %pytest -k "${k-}"
%pytest -k "${k-}"
%if %{with uvloop}
USE_UVLOOP=1 %pytest -k "${k-}"
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-asyncpg -f %{oreon_filedir}/python3-asyncpg.list

%changelog

%autochangelog
