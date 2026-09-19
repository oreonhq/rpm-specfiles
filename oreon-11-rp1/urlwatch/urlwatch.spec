%global source0_hash 112e037db9142256b19eb0af7073db688bb60a9dc34d14e548b282ff72521f3e

Name:           urlwatch
Version:        2.29
Release:        4%{?dist}
Summary:        A tool for monitoring webpages for updates

License:        LicenseRef-Callaway-BSD
URL:            http://thpinfo.com/2008/urlwatch/
Source0:        https://github.com/thp/urlwatch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)
# Build deps for testing
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pycodestyle)

Requires:  python3dist(platformdirs)
Requires:  python3dist(html2text)
Requires:  python3dist(keyring)
Requires:  python3dist(lxml)
Requires:  python3dist(minidb)
Requires:  python3dist(pyyaml)
Requires:  python3dist(requests)

%description
This script is intended to help you watch URLs and get notified (via
email or in your terminal) of any changes. The change notification
will include the URL that has changed and a unified diff of what has
changed.

The script supports the use of a filtering hook function to strip
trivially-varying elements of a webpage.

Basic features

* Simple configuration (text file, one URL per line)
* Easily hackable (clean Python implementation)
* Can run as a cronjob and mail changes to you
* Always outputs only plaintext - no HTML mails :)
* Supports removing noise (always-changing website parts)
* Example hooks to filter content in Python

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd .
cd docs
sphinx-build -M html source ../build
rm ../build/html/.buildinfo
popd

%install
%pyproject_install

%check
# test_filter_documentation requires jq and pdftotext which are not packaged in Fedora
%pytest lib/urlwatch/tests -k "not test_filter_documentation"

%files
%doc CHANGELOG.md README.md build/html/*
%license COPYING
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{_datadir}/%{name}/examples/
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.dist-info

%changelog
%autochangelog
