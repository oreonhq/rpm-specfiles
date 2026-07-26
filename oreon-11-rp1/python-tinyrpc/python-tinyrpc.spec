%global source0_hash 9a66a389d526f657d57d5e4ab2376e0dc559bdf9c8cc09d0c12c3e8eacd4ba93

%global library tinyrpc
%global module tinyrpc

Name:       python-%{library}
Version:    1.1.7
Release:    7%{?dist}
Summary:    A modular RPC library
License:    MIT
URL:        https://github.com/mbr/%{library}

# tarball in pypy does not include tests
Source0:    https://github.com/mbr/%{library}/archive/%{version}.tar.gz

BuildArch:  noarch

%description
tinyrpc is a library for making and handling RPC calls in python.

%package -n python-%{library}-doc
Summary:   Documentation for tinyrpc library

%description -n python-%{library}-doc
Documentation for tinyrpc library

%package -n python3-%{library}
Summary:    A modular RPC library

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-gevent
BuildRequires:  python3-msgpack
BuildRequires:  python3-pika
BuildRequires:  python3-werkzeug
BuildRequires:  python3-zmq

%description -n python3-%{library}
tinyrpc is a library for making and handling RPC calls in python.

# gevent-websocket and jsonext are old and unmaintained
%pyproject_extras_subpkg -n python3-%{library} gevent
#        'httpclient': ['requests', 'websocket-client', 'gevent-websocket'],
#pyproject_extras_subpkg -n python3-%{library} httpclient
%pyproject_extras_subpkg -n python3-%{library} msgpack
%pyproject_extras_subpkg -n python3-%{library} rabbitmq
%pyproject_extras_subpkg -n python3-%{library} wsgi
%pyproject_extras_subpkg -n python3-%{library} zmq

%package -n python3-%{library}-tests
Summary:    Tests for python3-tinyrpc library

# Requirements are not generated automatically
Requires:  python3-gevent
Requires:  python3-msgpack
Requires:  python3-pika
Requires:  python3-werkzeug
Requires:  python3-zmq
Requires:  python3-%{library} = %{version}-%{release}

%description -n python3-%{library}-tests
Tests for  python3-tinyrpc library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{library}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Fix doc build with latest Sphinx
sed -i "s#'https://docs.python.org/3/': None#'python': ('https://docs.python.org/3', None)#" docs/conf.py
sed -i "s#'https://pyzmq.readthedocs.io/en/latest/': None#'pyzmq': ('https://pyzmq.readthedocs.io/en/latest/', None)#" docs/conf.py
sed -i "s#'http://docs.python-requests.org/en/latest/': None#'python-requests': ('http://docs.python-requests.org/en/latest/', None)#" docs/conf.py
sed -i "s#'http://werkzeug.pocoo.org/docs/': None#'werkzeug': ('http://werkzeug.pocoo.org/docs/', None)#" docs/conf.py
sed -i "s#'http://www.gevent.org/': None#'gevent': ('http://www.gevent.org/', None)#" docs/conf.py

# generate html docs
sphinx-build docs build/sphinx/html
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{module}
# Move tests
mkdir -p %{buildroot}%%{python3_sitelib}/%{library}/tests
mv %{buildroot}%{python3_sitelib}/tests %{buildroot}%{python3_sitelib}/%{library}/tests

%check
%pytest -rs -v

%files -n python-%{library}-doc
%license LICENSE
%doc build/sphinx/html README.rst

%files -n python3-%{library} -f %{pyproject_files}
%license LICENSE

%files -n python3-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests

%changelog
%autochangelog
