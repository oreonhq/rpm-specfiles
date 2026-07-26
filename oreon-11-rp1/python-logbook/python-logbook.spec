%global source0_hash a0ee883a261eb9fb49dbf3d16667220df69b2d37d11ae3769988af59948f8f26

Name:		python-logbook
Version:	1.9.2
Release:	2%{?dist}
Summary:	A logging replacement for Python

License:	BSD-3-Clause
URL:		https://logbook.readthedocs.io
Source0:	https://github.com/getlogbook/logbook/archive/%{version}.tar.gz#/Logbook-%{version}.tar.gz

%description
Logbook is a logging system for Python that replaces the standard library's
logging module. It was designed with both complex and simple applications
and mind and the idea to make logging fun. What makes it fun? What about
getting log messages on your phone or desktop notification system?
Logbook can do that.

%package -n python3-logbook
Summary:	%{summary}

BuildRequires:  gcc
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-sqlalchemy
BuildRequires:	python3-redis
BuildRequires:	python3-zmq
BuildRequires:	python3-brotli
BuildRequires:  python3-Cython
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust-pyo3-devel
BuildRequires:  rust-pyo3-macros-devel
BuildRequires:  rust-indoc-devel
BuildRequires:  rust-unindent-devel

%description -n python3-logbook
Logbook is a logging system for Python that replaces the standard library's
logging module. It was designed with both complex and simple applications
and mind and the idea to make logging fun. What makes it fun? What about
getting log messages on your phone or desktop notification system?
Logbook can do that.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n logbook-%{version}

%cargo_prep
%cargo_generate_buildrequires
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%cargo_license

%install
%pyproject_install
%pyproject_save_files -l logbook

%check
%pytest -k "not test_redis_handler and not test_logged_if_slow and not test_logged_if_slow_reached and not test_logged_if_slow_did_not_reached and not test_logged_if_slow_logger and not test_logged_if_slow_level and not test_logged_if_slow_deprecated and not test_redis_handler"

%files -n python3-logbook -f %{pyproject_files}
%doc CHANGES README.md

%changelog
%autochangelog
