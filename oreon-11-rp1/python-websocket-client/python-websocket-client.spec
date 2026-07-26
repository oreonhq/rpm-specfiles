%global source0_hash 3239df9f44da632f96012472805d40a23281a991027ce11d2f45a6f24ac4c3da

%global common_description %{expand:
websocket-client is a WebSocket client for Python.  It provides access to low
level APIs for WebSockets.  websocket-client implements version hybi-13 of the
WebSocket protocol.  This client does not currently support the
permessage-deflate extension from RFC 7692.}

Name:               python-websocket-client
Version:            1.8.0
Release:            8%{?dist}
Summary:            WebSocket client for python
License:            Apache-2.0
URL:                https://github.com/websocket-client/websocket-client
BuildArch:          noarch
Source:             %{pypi_source websocket_client}

# https://github.com/websocket-client/websocket-client/pull/998
Patch:              0001-Include-pytest-in-test-extra.patch

%description %{common_description}

%package -n python3-websocket-client
Summary:            %{summary}
BuildRequires:      python3-devel

%description -n python3-websocket-client %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n websocket_client-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l websocket

%check
%pytest -v websocket/tests

%files -n python3-websocket-client -f %{pyproject_files}
%doc README.md ChangeLog
%{_bindir}/wsdump

%changelog
%autochangelog
