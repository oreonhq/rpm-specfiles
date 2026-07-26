%global source0_hash a13e49f762e97a291136bb1c4e39e6b026c4275593fb1d9ef9b73e7ef22e559d

%global pypi_name autobahn

Name:           python-%{pypi_name}
Version:        25.12.1
Release:        2%{?dist}
Summary:        Python networking library for WebSocket and WAMP

License:        MIT
URL:            https://autobahn.readthedocs.io/en/latest/
Source0:        %{pypi_source}
# Remove deps on ubjson: it's optionnal and not packaged yet.
Patch0:         remove-ubjson.patch
Patch1:         remove-unpackaged-sphinx-ext.patch

BuildArch:      noarch

%description
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and for writing servers and clients.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist argon2_cffi
BuildRequires:  %py3_dist cffi
BuildRequires:  %py3_dist passlib
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist pytest-asyncio
BuildRequires:  %py3_dist six
BuildRequires:  %py3_dist twisted
BuildRequires:  %py3_dist txaio
BuildRequires:  %py3_dist pynacl
%if 0%{?fedora}
BuildRequires:  %py3_dist cbor2
%endif
BuildRequires:  %py3_dist cryptography
BuildRequires:  %py3_dist hyperlink

%description -n python3-%{pypi_name}
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and for writing servers and clients.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-furo
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-design)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinxext-opengraph)
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(sphinx-autoapi)
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(linkify-it-py)
BuildRequires:  google-roboto-fonts
Requires:       js-jquery
Requires:       google-roboto-fonts

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%pyproject_extras_subpkg -n python3-%{pypi_name} twisted

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Some packages are always outdated...
# setuptools >= 80 is used to detect the license we install the RPM way. Downgrade…
sed -i -e "s/setuptools>=80.9.0/setuptools>=70/g" pyproject.toml
# Remove packages that will try to import attrs (optionnal deps) since in EPEL it's outdated and doesn't allow the import of attrs
# See https://www.attrs.org/en/stable/changelog.html#id11
%if ! 0%{?fedora}
rm -rf autobahn/xbr/test/*
sed -i '\@recursive-include autobahn/xbr/test/catalog/schema@d' MANIFEST.in
sed -i '\@autobahn/xbr/test/profile@d' MANIFEST.in
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
# Disable in case local builder support NVX
export AUTOBAHN_USE_NVX=false
export PYUBJSON_NO_EXTENSION=1
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} twisted

%check
# Don't check imports: importing some files starts to configure autobahn and then trying to
# import other will fails. There are too many modules with issues to be worth it.
#%%pyproject_check_import

# Ignore tests that rely on optional and not packaged deps.
k="${k-}${k+ and }not test_no_memory_arg"
k="${k-}${k+ and }not test_basic"
k="${k-}${k+ and }not test_websocket_custom_loop"
k="${k-}${k+ and }not TestSerializer"
# Skip tests failing with pytest-asyncio >= 0.23.5.post1
# https://github.com/crossbario/autobahn-python/issues/1631
# https://bugzilla.redhat.com/show_bug.cgi?id=2270130
k="${k-}${k+ and }not test_vectors"
k="${k-}${k+ and }not test_authenticator"
k="${k-}${k+ and }not test_valid"
k="${k-}${k+ and }not test_auto_ping"
k="${k-}${k+ and }not test_interpolate_server_status_template"
k="${k-}${k+ and }not test_sendClose"
k="${k-}${k+ and }not test_conflict_SSLContext_with_ws_url"
k="${k-}${k+ and }not test_conflict_SSL_True_with_ws_url"
%if 0%{?fedora}
# Disable tests temporarilly since autobahn doesn't work with the latest version of
# pytest-asyncio which is the default version in fedora now.
#USE_ASYNCIO=1 %%pytest --pyargs autobahn ${k+ -k} "${k-}"
%else
k="${k-}${k+ and }not TestDecimalSerializer"
USE_ASYNCIO=1 %pytest --ignore=xbr/test --pyargs autobahn ${k+ -k} "${k-}"
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/wamp

%files -n python-%{pypi_name}-doc
%license LICENSE

%changelog
%autochangelog
