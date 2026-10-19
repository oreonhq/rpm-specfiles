%global source0_hash 9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d
Name:           python-httpx-sse
Version:        0.4.3
Release:        1%{?dist}
Summary:        Consume Server-Sent Event (SSE) messages with HTTPX.
License:        MIT
URL:            https://github.com/florimondmanca/httpx-sse
Source0:        https://files.pythonhosted.org/packages/source/h/httpx_sse/httpx_sse-%{version}.tar.gz
Patch:          remove-coverage-options-from-pytest.diff
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-httpx-sse = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-httpx-sse
Summary:        Consume Server-Sent Event (SSE) messages with HTTPX.
%description -n python3-httpx-sse

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir httpx_sse-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httpx-sse usr/lib/python3*/site-packages/httpx_sse* usr/lib64/python3*/site-packages/httpx_sse* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httpx_sse* usr/lib64/python3*/site-packages/httpx_sse* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-httpx-sse -f %{oreon_filedir}/python3-httpx-sse.list

%changelog

%autochangelog
