%global source0_hash 49f2e1f8051f2885719beb1b77e312b5a27c3e4b60f0b045a388f194d995e068

%global _description \
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

Name:           python-aiohttp-socks
Version:        0.10.1
Release:        %autorelease
Summary:        SOCKS proxy connector for aiohttp

License:        Apache-2.0
URL:            https://pypi.org/project/aiohttp-socks/
Source:         %{pypi_source aiohttp_socks}

BuildArch:      noarch

%description %{_description}

%package -n python3-aiohttp-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-aiohttp-socks %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n aiohttp_socks-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiohttp_socks

%files -n python3-aiohttp-socks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
