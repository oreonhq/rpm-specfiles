%global source0_hash c982176754e8274f5aec00eaa65986cf205cb5fc898c2f917eead00d221f2adc

Name:           python-requests-exoscale-auth
Version:        1.1.2
Release:        19%{?dist}
Summary:        Exoscale APIs support for Python-Requests

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/exoscale/requests-exoscale-auth
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Exoscale APIs support for Python-Requests}

%description %_description

%package -n python3-requests-exoscale-auth
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%description -n python3-requests-exoscale-auth %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n requests-exoscale-auth-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files exoscale_auth

%check
%pytest

%files -n python3-requests-exoscale-auth -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
