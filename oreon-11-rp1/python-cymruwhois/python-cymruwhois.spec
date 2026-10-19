%global source0_hash 357bd4beaab4c857062984cfd6b85606e3ff6b39e6e5420f428961ab2a9f2434
Name:           python-cymruwhois
Version:        1.6
Release:        1%{?dist}
Summary:        Client for the whois.cymru.com service
License:        MIT
URL:            http://packages.python.org/cymruwhois/
Source0:        https://github.com/JustinAzoff/python-cymruwhois/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cymruwhois = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cymruwhois
Summary:        Client for the whois.cymru.com service
%description -n python3-cymruwhois

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
# Remove shebang
sed -i '/env python/d' cymruwhois.py

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 docs/cymruwhois.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles python3-cymruwhois usr/lib/python3*/site-packages/cymruwhois* usr/lib64/python3*/site-packages/cymruwhois* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cymruwhois* usr/lib64/python3*/site-packages/cymruwhois* usr/bin/*

%check

%pyproject_check_import
%pytest --ignore=tests/test_common_lookups.py --ignore=tests/test_doctest.py
%files
%files -n python3-cymruwhois -f %{oreon_filedir}/python3-cymruwhois.list

%changelog

%autochangelog
