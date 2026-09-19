%global source0_hash 357bd4beaab4c857062984cfd6b85606e3ff6b39e6e5420f428961ab2a9f2434

Name:           python-cymruwhois
Version:        1.6
Release:        %autorelease
Summary:        Client for the whois.cymru.com service

License:        MIT
URL:            http://packages.python.org/cymruwhois/
Source:         https://github.com/JustinAzoff/python-cymruwhois/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Perform lookups by ip address and return ASN, Country Code, and Netblock Owner::

>>> import socket
>>> ip = socket.gethostbyname("www.google.com")
>>> from cymruwhois import Client
>>> c=Client()
>>> r=c.lookup(ip)
>>> print r.asn
15169
>>> print r.owner
GOOGLE - Google Inc.}

%description %_description

%package -n     python3-cymruwhois
Summary:        %{summary}

%description -n python3-cymruwhois %_description

%pyproject_extras_subpkg -n python3-cymruwhois cache

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
# Remove shebang
sed -i '/env python/d' cymruwhois.py

%generate_buildrequires
%pyproject_buildrequires -x cache

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cymruwhois
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 docs/cymruwhois.1 %{buildroot}%{_mandir}/man1/

%check
%pyproject_check_import
# Do not use tests that require network access or building html
# documentation
%pytest --ignore=tests/test_common_lookups.py --ignore=tests/test_doctest.py

%files -n python3-cymruwhois -f %{pyproject_files}
%{_bindir}/cymruwhois
%{_mandir}/man1/cymruwhois.1*

%changelog
%autochangelog
