%global source0_hash 8c512383f6d71cabe82619b0a719aa04d7ed76304206fe4596133cfc9ce29cae

Name:           fts-rest-client
Version:        3.14.2
Release:        5%{?dist}
Summary:        File Transfer Service (FTS) -- Python3 Client and CLI

License:        Apache-2.0
URL:            https://fts.web.cern.ch/
# git clone --depth=1 --branch v3.14.2 https://gitlab.cern.ch/fts/fts-rest-flask.git fts-rest-client-3.14.2
# tar -C fts-rest-client-3.14.2/ -czf fts-rest-client-3.14.2.tar.gz src/cli src/fts3 LICENSE setup.py setup.cfg --transform "s|^|fts-rest-client-3.14.2/|" --show-transformed-names
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python%{python3_pkgversion}-m2crypto
Requires:       python%{python3_pkgversion}-requests

# Replace previous FTS Python2 Client package
Provides:       python-fts = %{version}-%{release}
Provides:       fts-rest-cli = %{version}-%{release}
Obsoletes:      python-fts < 3.12.0
Obsoletes:      fts-rest-cli < 3.12.0

BuildArch:      noarch

%description
File Transfer Service (FTS) -- Python3 Client and CLI

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/fts3/
%{python3_sitelib}/fts*-*.egg-info/
%{_bindir}/fts-rest-*

%changelog
%autochangelog
