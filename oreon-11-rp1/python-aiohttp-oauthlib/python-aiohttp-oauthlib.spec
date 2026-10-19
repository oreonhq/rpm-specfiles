%global source0_hash 893cd1a59ddd0c2e4e980e3a544f9710b7c4ffb9e27b4cd038b51fe1d70393b7
Name:           python-aiohttp-oauthlib
Version:        0.1.0
Release:        1%{?dist}
Summary:        This library is a port of requests-oauthlib for aiohttp
License:        ISC
URL:            https://git.sr.ht/~whynothugo/aiohttp-oauthlib
Source0:        https://files.pythonhosted.org/packages/source/a/aiohttp-oauthlib/aiohttp-oauthlib-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-aiohttp
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aiohttp-oauthlib = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-aiohttp-oauthlib
Summary:        This library is a port of requests-oauthlib for aiohttp
%description -n python3-aiohttp-oauthlib

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir aiohttp-oauthlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiohttp-oauthlib usr/lib/python3*/site-packages/aiohttp_oauthlib* usr/lib64/python3*/site-packages/aiohttp_oauthlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiohttp_oauthlib* usr/lib64/python3*/site-packages/aiohttp_oauthlib* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-aiohttp-oauthlib -f %{oreon_filedir}/python3-aiohttp-oauthlib.list

%changelog

%autochangelog
