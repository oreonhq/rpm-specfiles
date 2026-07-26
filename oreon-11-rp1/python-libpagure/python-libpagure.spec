%global source0_hash af48a3fe5069d3714f6669a4714874380928954a390320e092871696bae7cbd6

%global modname libpagure

Name:           python-libpagure
Version:        0.22
Release:        10%{?dist}
Summary:        A Python library for Pagure APIs
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/libpagure/
Source0:        https://pagure.io/releases/libpagure/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
A Python library for Pagure APIs

%description %_description

%package -n python3-libpagure
Summary:        A Python library for Pagure APIs
%{?python_provide:%python_provide python3-libpagure}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:  python3-requests

%description -n python3-libpagure
A Python library for Pagure APIs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-libpagure
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/libpagure*/

%changelog
%autochangelog
