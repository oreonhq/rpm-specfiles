%global source0_hash 0fcb57545848be86992e128218fd96dd87a6769ffdb1a968dff79632b85604d0
Name:           python-websocket-client
Version:        1.9.2
Release:        1%{?dist}
Summary:        WebSocket client for Python with low level API options
License:        Apache-2.0
URL:            https://github.com/websocket-client/websocket-client/
Source0:        https://files.pythonhosted.org/packages/source/w/websocket_client/websocket_client-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-websocket-client = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-websocket-client
Summary:        WebSocket client for Python with low level API options
%description -n python3-websocket-client

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir websocket_client-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-websocket-client usr/lib/python3*/site-packages/websocket_client* usr/lib64/python3*/site-packages/websocket_client* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/websocket_client* usr/lib64/python3*/site-packages/websocket_client* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-websocket-client -f %{oreon_filedir}/python3-websocket-client.list

%changelog

%autochangelog
