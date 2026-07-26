%global source0_hash e9e0b33efa8fa20d817dd78dfd9e4cdb3967c8a5d3cb5a783be1ee81c4a89c7c

Name:          python-jsonrpclib
Version:       0.4.3.2
Release:       17%{?dist}
Summary:       JSON-RPC v2.0 client library for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           http://github.com/tcalmant/jsonrpclib/
Source0:       %{pypi_source jsonrpclib-pelix}

BuildArch:     noarch
BuildRequires: python3-devel

%global _description %{expand:
This library is an implementation of the JSON-RPC specification. It supports
both the original 1.0 specification, as well as the new (proposed)
2.0 specification, which includes batch submission, keyword arguments, etc.

This library is licensed under the terms of the Apache Software License 2.0.}

%description %_description

%package -n python3-jsonrpclib
Summary: %{summary}

%description -n python3-jsonrpclib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jsonrpclib-pelix-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files jsonrpclib

%files -n python3-jsonrpclib -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
