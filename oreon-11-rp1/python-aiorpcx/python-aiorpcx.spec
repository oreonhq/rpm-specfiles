%global source0_hash 2302d827796d52aa87a457e204a59c6e5bb307792cd31379a9c85f6494a4a59a

Name:      python-aiorpcx
Version:   0.24.0
Release:   6%{?dist}
Summary:   Generic async RPC implementation

# https://github.com/kyuupichan/aiorpcX/issues/11
# aiorpcx/curio.py is BSD, rest is MIT
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:   LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:       https://pypi.org/project/aiorpcX/
Source:    %{pypi_source aiorpcx}

BuildArch: noarch

%global _description %{expand:
Transport, protocol and framing-independent async RPC client
and server implementation.}

%description %_description

%package -n python3-aiorpcx
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-aiorpcx %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n aiorpcx-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-aiorpcx
%doc README.rst
%license LICENCE
%{python3_sitelib}/aiorpcx/
%{python3_sitelib}/aiorpcX-*.egg-info/

%changelog
%autochangelog
