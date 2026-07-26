%global source0_hash 60fbefacfaf54de5df6ea0ddad663ecbf62fca6af319d5e5e020c543dd76b059

%global srcname rq
%bcond_without tests

Name:           python-%{srcname}
Version:        2.6.1
Release:        1%{?dist}
Summary:        Simple, lightweight, library for creating background jobs, and processing them

License:        BSD-2-Clause
URL:            https://python-rq.org
Source:         https://github.com/rq/rq/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Backport upstream fixes for python3.14 multiprocessing
Patch: https://github.com/rq/rq/pull/2359.patch
Patch: https://github.com/rq/rq/commit/df29cf6.patch
Patch: https://github.com/rq/rq/commit/615525b.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil
BuildRequires:  redis
%endif

%global _description %{expand:
RQ (Redis Queue) is a simple Python library for queueing jobs
and processing them in the background with workers.
It is backed by Redis and it is designed to have a low barrier to entry.
It should be integrated in your web stack easily.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}
Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%{_bindir}/redis-server --bind 127.0.0.1 --port 6379 &
REDIS_SERVER_PID=$!
# Set the default timezone to UTC otherwise unit tests fail.
export TZ=UTC
%pytest -v
%{_bindir}/redis-cli shutdown nosave force now
# Wait for redis-server termination (the command above is async)
wait $REDIS_SERVER_PID
%endif

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker

%changelog
%autochangelog
