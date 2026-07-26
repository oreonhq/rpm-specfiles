%global source0_hash 4bb59ab4ed202b2139f3e9e6d8d62baa9bdca0f185ba648c5a08304a9d958fb6

Name:           python-icmplib
Version:        3.0.4
Release:        %autorelease
Summary:        An implementation of the ICMP protocol in Python
License:        LGPL-3.0-or-later
URL:            https://github.com/ValentinBELYN/icmplib
# pypi_source tar ball differs from github tag and is lacking docs/examples :(
Source:         https://github.com/ValentinBELYN/icmplib/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
An implementation of the ICMP protocol in Python.}

%description %_description

%package -n     python3-icmplib
Summary:        %{summary}

%description -n python3-icmplib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n icmplib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files icmplib

%check
%pyproject_check_import

%files -n python3-icmplib -f %{pyproject_files}
%license LICENSE
%doc docs/* examples/*.py

%changelog
%autochangelog
