%global source0_hash 82ea88a7ec3d42f2cd77364c881bcf5dbfce5636d0d9aeb187b45124db703416

%global pypi_name certbot-dns-plesk

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        18%{?dist}
Summary:        Plesk DNS Authenticator plugin for Certbot

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://pypi.org/project/%{pypi_name}
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Plesk DNS Authenticator plugin for Certbot
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:       %{pypi_name} = %{version}-%{release}
%endif
# Recommend the CLI as that will be the interface most use
Recommends:     certbot

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files certbot_dns_plesk

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
