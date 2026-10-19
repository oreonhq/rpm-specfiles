%global source0_hash fb7e8facda7749c2fa5fa5dc241c0adc302da3d31d588964a2570db501aa49e5
%define python3dist(name) python3-%{name}
Name:           linkchecker
Version:        10.6.0
Release:        1%{?dist}
Summary:        Check HTML documents for broken links
License:        GPL-2.0-or-later
URL:            https://linkcheck.github.io/linkchecker/
Source0:        https://files.pythonhosted.org/packages/source/L/LinkChecker/LinkChecker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.8.0
BuildRequires:  python3dist(setuptools-scm) >= 7.1.0
Requires:       python3-linkchecker = %{version}-%{release}
# /oreon:deps
%description
LinkChecker is a website validator. LinkChecker checks links in web documents or full websites.

Features:
- Recursive and multithreaded checking and site crawling
- Output in colored or normal text, HTML, SQL, CSV, XML or a sitemap graph in 
different formats
- HTTP/1.1, HTTPS, FTP, mailto: and local file links support
- Restriction of link checking with regular expression filters for URLs
- Proxy support
- Username/password authorization for HTTP and FTP
- Honors robots.txt exclusion protocol
- Cookie support
- HTML5 support
- A command line and web interface
- Various check plugins available

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir LinkChecker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
