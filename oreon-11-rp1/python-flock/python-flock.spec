%global source0_hash 5c8fcecb0a360bf73945068bb21f5f31946d946d796e07cc6b4e90a09ffb997a

Name:           python-flock
Version:        0.1
Release:        42%{?dist}
Summary:        Flock object for with statement

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/misli/python-flock
Source:         http://github.srcurl.net/misli/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Flock object uses fcntl.flock to lock (resp. unlock)
file descriptor (fd) with operation (op)
when entering (resp. leaving) runtime context related to it.

%package     -n python3-flock
Summary:        Flock object for with statement

%description -n python3-flock
Flock object uses fcntl.flock to lock (resp. unlock)
file descriptor (fd) with operation (op)
when entering (resp. leaving) runtime context related to it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-flock
%doc README.md LICENSE
%{python3_sitelib}/flock.py
%{python3_sitelib}/__pycache__/flock.*
%{python3_sitelib}/flock-%{version}-py3.*.egg-info

%changelog
%autochangelog
