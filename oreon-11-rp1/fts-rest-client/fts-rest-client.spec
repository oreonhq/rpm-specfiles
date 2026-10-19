%global source0_hash 8c512383f6d71cabe82619b0a719aa04d7ed76304206fe4596133cfc9ce29cae
Name:           fts-rest-client
Version:        3.14.2
Release:        1%{?dist}
Summary:        File Transfer Service (FTS) -- Python3 Client and CLI
License:        Apache-2.0
URL:            https://fts.web.cern.ch/
Source0:        %{name}-%{version}.tar.gz
Requires:       python3
Requires:       python%{python3_pkgversion}-m2crypto
Requires:       python%{python3_pkgversion}-requests
Provides:       python-fts = %{version}-%{release}
Provides:       fts-rest-cli = %{version}-%{release}
Obsoletes:      python-fts < 3.12.0
Obsoletes:      fts-rest-cli < 3.12.0
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
File Transfer Service (FTS) -- Python3 Client and CLI

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
