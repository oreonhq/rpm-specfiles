%global source0_hash 1cad8860aa0ecf9567125381e4430046526246e075224350a6a624addac05f5e
%bcond tests 1
Name:           python-loguru
Version:        0.7.3
Release:        1%{?dist}
Summary:        Python logging made (stupidly) simple
License:        MIT
URL:            https://github.com/Delgan/loguru
Source0:        https://github.com/Delgan/loguru/archive/%{version}/loguru-%{version}.tar.gz
Patch:          0001-Fix-deprecation-warning-raised-by-tests-with-Python-.patch
Patch:          %{url}/commit/84023e2bd8339de95250470f422f096edcb8f7b7.patch
BuildArch:      noarch
%global common_description %{expand:
Loguru is a library which aims to bring enjoyable logging in Python.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3
Requires:       python3-loguru = %{version}-%{release}
# /oreon:deps
%package -n       python3-loguru+dev
Summary:        Metapackage for python3-loguru dev extras
Requires:       python3-loguru = %{version}-%{release}
Requires:       python3dist(pre-commit) == 4.0.1
Requires:       python3dist(tox) == 3.27.1
Requires:       python3dist(tox) == 4.23.2
Requires:       python3dist(pytest) == 6.1.2
Requires:       python3dist(pytest) == 8.3.2
Requires:       python3dist(pytest-cov) == 2.12.1
Requires:       python3dist(pytest-cov) == 5.0.0
Requires:       python3dist(pytest-cov) == 6.0.0
Requires:       python3dist(pytest-mypy-plugins) == 1.9.3
Requires:       python3dist(pytest-mypy-plugins) == 3.1.0
Requires:       python3dist(colorama) == 0.4.5
Requires:       python3dist(colorama) == 0.4.6
Requires:       python3dist(freezegun) == 1.1.0
Requires:       python3dist(freezegun) == 1.5.0
Requires:       python3dist(exceptiongroup) == 1.1.3
Requires:       python3dist(mypy) == v0.910
Requires:       python3dist(mypy) == v0.971
Requires:       python3dist(mypy) == v1.4.1
Requires:       python3dist(mypy) == v1.13.0
Requires:       python3dist(sphinx) == 8.1.3
Requires:       python3dist(sphinx-rtd-theme) == 3.0.2
Requires:       python3dist(myst-parser) == 4.0.0
Requires:       python3dist(build) == 1.2.2
Requires:       python3dist(twine) == 6.0.1
Provides:       python3dist(loguru[dev]) = %{version}-%{release}

%description -n python3-loguru+dev
Metapackage for python3-loguru dev extras.

%description %{common_description}

%package -n     python3-loguru
Summary:        Python logging made (stupidly) simple
# oreon:reqs
Requires:       python3dist(aiocontextvars) >= 0.2.0
Requires:       python3dist(colorama) >= 0.3.4
Requires:       python3dist(win32-setctime) >= 1.0.0
# /oreon:reqs
%description -n python3-loguru %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir loguru-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-loguru usr/lib/python3*/site-packages/loguru* usr/lib64/python3*/site-packages/loguru* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/loguru* usr/lib64/python3*/site-packages/loguru* usr/bin/*

%check

%if %{with tests}
ignore="${ignore-} --ignore=tests/typesafety/test_logger.yml"
%pytest ${ignore-} -k "${k-}" -rs
%endif
%files
%files -n python3-loguru -f %{oreon_filedir}/python3-loguru.list

%changelog

%autochangelog
