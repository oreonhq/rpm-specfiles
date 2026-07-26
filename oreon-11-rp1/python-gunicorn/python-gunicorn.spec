%global source0_hash f014447a0101dc57e294f6c18ca6b40227a4c90e9bdb586042628030cba004ec

%global srcname gunicorn
%global _description %{expand:
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It is a
pre-fork worker model. The Gunicorn server is broadly compatible with various
web frameworks, simply implemented, light on server resources, and fairly
speedy.}
%bcond extras 1

Name:           python-%{srcname}
Version:        23.0.0
Release:        7%{?dist}
Summary:        Python WSGI HTTP Server
License:        MIT
URL:            https://gunicorn.org/
Source:         %pypi_source %{srcname}
# distro-specific, not upstreamable
Patch:          0001-use-dev-log-for-syslog.patch
BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Obsoletes:      python3-%{srcname}+eventlet < 21.2.0-8

%description -n python3-%{srcname} %{_description}

%package doc
Summary:        Documentation for the %{name} package
BuildRequires:  make

%description doc
Documentation for the %{name} package.

%if %{with extras}
# There are a few extras that we're not creating subpackages for:
# tornado: described upstream as "not recommended"
# gthread: no additional dependencies
%pyproject_extras_subpkg -n python3-%{srcname} gevent setproctitle
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p 1
# disable code coverage checks
sed -e '/--cov=gunicorn --cov-report=xml/d' -i pyproject.toml
sed -e '/coverage/d' -e '/pytest-cov/d' -i requirements_test.txt
sed -e '/addopts/d' -i setup.cfg
sed -e '/eventlet/d' -i requirements_test.txt
%if %{without extras}
sed -e '/gevent/d' -i requirements_test.txt
%endif

%generate_buildrequires
%pyproject_buildrequires requirements_dev.txt

%build
%pyproject_wheel
%make_build -C docs html

%install
%pyproject_install
%pyproject_save_files %{srcname}
# symlink extra executable names
ln -s %{_bindir}/gunicorn %{buildroot}%{_bindir}/gunicorn-3
ln -s %{_bindir}/gunicorn %{buildroot}%{_bindir}/gunicorn-%{python3_version}

%check
%pytest --verbose tests -k "not geventlet%{!?with_extras: and not ggevent}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc NOTICE README.rst THANKS
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3
%{_bindir}/%{srcname}-%{python3_version}

%files doc
%license LICENSE
%doc docs/build/html/*

%changelog
%autochangelog
