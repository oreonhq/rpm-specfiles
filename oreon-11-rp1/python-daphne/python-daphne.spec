%global source0_hash 5f898e700a1fda7addf1541d7c328606415e96a7bd768405f0463c312fcb31b3

%bcond_without  tests

Name:           python-daphne
Version:        4.2.1
Release:        %autorelease
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD-3-Clause
URL:            https://github.com/django/daphne
Source:         %{pypi_source daphne}
BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
# List test dependencies manually, since the test extra contains many unwanted
# linters, coverage-analysis tools, typecheckers, etc.:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist django}
BuildRequires:  %{py3_dist hypothesis}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
%endif

%global common_description %{expand:
Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP,
developed to power Django Channels.  It supports automatic negotiation of
protocols; there is no need for URL prefixing to determine WebSocket endpoints
versus HTTP endpoints.}

%description %{common_description}

%package -n python3-daphne
Summary:        %{summary}

%description -n python3-daphne %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n daphne-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l daphne twisted

%check
%if %{with tests}
# This test assumes that twisted/plugins/fd_endpoint.py is installed in the
# system site-packages, but we have it in the buildroot site-packages.
k="${k-}${k+ and }not test_fd_endpoint_plugin_installed"
%pytest -k "${k-}"
%else
%pyproject_check_import
%endif

%files -n python3-daphne -f %{pyproject_files}
%doc README.rst CHANGELOG.txt
%{_bindir}/daphne

%changelog
%autochangelog
