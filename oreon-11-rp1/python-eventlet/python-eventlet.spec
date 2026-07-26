%global source0_hash 290852db0065d78cec17a821b78c8a51cafb820a792796a354592ae4d5fceeb0

%global srcname eventlet
%global _description %{expand:
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using co-routines to make the non-blocking
io operations appear blocking at the source code level.}

%bcond_without tests

Name:           python-%{srcname}
Version:        0.40.3
Release:        3%{?dist}
Summary:        Highly concurrent networking library
License:        MIT

URL:            https://eventlet.net
Source:         %pypi_source %{srcname}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

Patch0: 0001-Update-pyzmq-and-psycopg2-binary-versions.patch

%description -n python3-%{srcname} %{_description}

%package -n python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}

%description -n python3-%{srcname}-doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

sed -i '/ *pip install -e.*/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv},docs

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%tox -e docs

%check
%if %{with tests}
# Disable setting up dns (we have no /etc/resolv.conf in mock)
export EVENTLET_NO_GREENDNS=yes
%tox -e %{default_toxenv} -- -- -k 'not test_clear and not test_noraise_dns_tcp and not test_raise_dns_tcp and not test_dns_methods_are_green and not test_fork_after_monkey_patch and not test_send_timeout'
%else
%pyproject_check_import -e eventlet.green.* -e eventlet.hubs.pyevent -e eventlet.support.* -e eventlet.zipkin.*
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS NEWS

%files -n python3-%{srcname}-doc
%license LICENSE
%doc doc/build/html

%changelog
%autochangelog
