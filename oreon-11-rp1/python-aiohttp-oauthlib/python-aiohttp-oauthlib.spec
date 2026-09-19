%global source0_hash 893cd1a59ddd0c2e4e980e3a544f9710b7c4ffb9e27b4cd038b51fe1d70393b7

Name:           python-aiohttp-oauthlib
Version:        0.1.0
Release:        10%{?dist}
Summary:        This library is a port of requests-oauthlib for aiohttp

License:        ISC
URL:            https://git.sr.ht/~whynothugo/aiohttp-oauthlib
Source:         %{pypi_source aiohttp-oauthlib}

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-aiohttp

%global _description %{expand:
This library is a port of requests-oauthlib for aiohttp}

%description %_description

%package -n python3-aiohttp-oauthlib
Summary:        %{summary}

%description -n python3-aiohttp-oauthlib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n aiohttp-oauthlib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiohttp_oauthlib

%check
%pyproject_check_import

%files -n python3-aiohttp-oauthlib -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
