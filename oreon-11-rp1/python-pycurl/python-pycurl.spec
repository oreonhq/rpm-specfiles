%global source0_hash 9d43013002eab2fd6d0dcc671cd1e9149e2fc1c56d5e796fad94d076d6cb69ef

# test dependencies are not available on el9+
%if 0%{?fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

%global modname pycurl

Name:           python-%{modname}
Version:        7.45.7
Release:        2%{?dist}
Summary:        A Python interface to libcurl

License:        curl OR LGPL-2.1-or-later
URL:            http://pycurl.io
Source0:        https://files.pythonhosted.org/packages/source/p/pycurl/pycurl-7.45.7.tar.gz

# drop link-time vs. run-time TLS backend check (#1446850)
Patch1:         0001-python-pycurl-7.45.1-tls-backend.patch
# skip Kerberos tests on libcurl >= 8.17.0
Patch2:         ea92e3ca230a3ff3d464cb6816102fa157177aca.patch

BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libcurl-full
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-flaky
BuildRequires:  python3-flask
BuildRequires:  python3-pytest
BuildRequires:  vsftpd
%endif

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%global libcurl_sed '/^#define LIBCURL_VERSION "/!d;s/"[^"]*$//;s/.*"//;s/-.*$//;s/$/~/;q'
%global curlver_h /usr/include/curl/curlver.h
%global libcurl_ver %(sed %{libcurl_sed} %{curlver_h} 2>/dev/null || echo 0)

%global _description %{expand:
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}
Requires:       libcurl%{?_isa} >= %{libcurl_ver}

%description -n python3-%{modname} %_description

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{modname}-%{version} -p1

# use %%{python3} instead of python to invoke tests
sed -e 's|python |%{python3} |' -i tests/ext/test-suite.sh
%py3_shebang_fix tests/*.py setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
export PYCURL_SSL_LIBRARY=openssl
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l curl pycurl
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%if %{with tests}
%check
# relax crypto policy for the test-suite to make it pass again (#1863711)
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=XXX
export OPENSSL_CONF=

export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYCURL_SSL_LIBRARY=openssl
export PYCURL_VSFTPD_PATH=vsftpd

export PYTEST_ADDOPTS="--ignore examples -m 'not online'"
%py3_test_envvars make do-test PYTHON='%{python3}' PYTEST="%{__pytest}" PYFLAKES=true
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%doc ChangeLog README.rst examples doc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.45.7-2
- Prepare for Oreon 11 (RP1)
