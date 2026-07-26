%global source0_hash 4dc881a815f1c50449e63255f1f1aff12b2cdf588edbaa5137a3828c01955825

# Created by pyp2rpm-3.3.10

Name:           python-xapian-haystack
Version:        3.1.0
Release:        11%{?dist}
Summary:        A Xapian backend for Haystack

License:        GPL-2.0-only
URL:            https://github.com/notanumber/xapian-haystack
Source0:        %{url}/archive/%{version}/xapian-haystack-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Xapian backend for Django-Haystack}

%description %_description

%package -n     python3-xapian-haystack
Summary:        %{summary}

Requires:       python3-xapian >= 1.4
%description -n python3-xapian-haystack %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n xapian-haystack-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-xapian-haystack
%license LICENSE
%doc README.rst
%pycached %{python3_sitelib}/xapian_backend.py
%{python3_sitelib}/xapian_haystack-%{version}.dist-info/

%changelog
%autochangelog
