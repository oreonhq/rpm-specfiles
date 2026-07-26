%global source0_hash feb1a533500a95c14fd155733a1056fe359192553d82c07c6ba04fcbfc40b12d

# invoke with "--with tests" to enable tests, currently disabled
# as we need to package both wsgi_intercept and pytest-localserver
# for them to work. Will also need BR: pystest once the two
# above packages exist in Fedora
%bcond tests 0

%if (%{defined fedora} && 0%{?fedora} <= 42) || (%{defined rhel} && 0%{?rhel} <= 10)
# setuptools < 77 does not support PEP 639
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

%global sum Synchronize calendars and contacts
%global srcname vdirsyncer
# Share doc between python- and python3-
%global _docdir_fmt %{name}

Name:       vdirsyncer
Version:    0.20.0
Release:    4%{?dist}
Summary:    %{sum}

License:    BSD-3-Clause
URL:        https://github.com/pimutils/%{name}
Source:     %{pypi_source}
# conditional patches
Patch1000:  vdirsyncer-revert-license-metadata-update.diff

BuildArch:  noarch
Obsoletes:  python2-%{srcname} <= 0.12.1

BuildRequires:  make
BuildRequires:  python3-click >= 5.0
BuildRequires:  python3-click-log >= 0.4
BuildRequires:  python3-click-threading >= 0.4.0
BuildRequires:  python3-devel
BuildRequires:  python3-icalendar
BuildRequires:  python3-lxml
BuildRequires:  python3-requests >= 2.10
BuildRequires:  python3-requests-toolbelt >= 0.4.0
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-aiohttp-oauthlib
BuildRequires:  python3-trustme
BuildRequires:  python3-pytest-httpserver
BuildRequires:  python3-pytest-localserver

Requires:       python3-click >= 5.0
Requires:       python3-click-log >= 0.4
Requires:       python3-click-threading >= 0.4.0
Requires:       python3-icalendar
Requires:       python3-lxml >= 3.1
Requires:       python3-requests >= 2.10
Requires:       python3-requests-toolbelt >= 0.4.0
Requires:       python3-aiohttp-oauthlib
Requires:       python3-vdirsyncer = %{version}
Requires:       sqlite

%description
vdirsyncer synchronizes your calendars and address books between two entities.
The supported protocols are CalDAV, CardDAV, arbitrary HTTP resources and some
more.

It aims to be for CalDAV and CardDAV what OfflineIMAP is for IMAP.

%package -n python3-%{srcname}
Summary:        %{sum}

Requires:       python3-click >= 5.0
Requires:       python3-click-log >= 0.4
Requires:       python3-click-threading >= 0.4.0
Requires:       python3-icalendar
Requires:       python3-lxml >= 3.1
Requires:       python3-requests >= 2.10
Requires:       python3-requests-toolbelt >= 0.4.0
Requires:       python3-aiohttp-oauthlib

%description -n python3-%{srcname}
vdirsyncer synchronizes your calendars and address books between two entities.
The supported protocols are CalDAV, CardDAV, arbitrary HTTP resources and some
more.

It aims to be for CalDAV and CardDAV what OfflineIMAP is for IMAP.
This package contains the python3 modules.

%package doc
Summary:        Documentation for vdirsyncer

%description doc
The vdirsyncer-doc package provides all the documentation
for the vdirsyncer calendar/address-book synchronization utility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%autopatch -p1 -M 999
%if %{with old_setuptools}
%autopatch -p1 1000
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
# From: https://athoscr.fedorapeople.org/packaging/python-setuptools_scm_git_archive.spec
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

# Custom sphinx docs need to import vdirsyncer classes from the untarred
# source tree
export PYTHONPATH=`pwd`
cd docs
# NOT using smp_mflags because sphinx cannot really cope with it
# i.e. one out of 20 builds will misteriously fail
make SPHINXBUILD=sphinx-build-3 man html text
cd ..
unset PYTHONPATH
# Remove extra copy of text docs
rm -vrf docs/_build/html/_sources
rm -fv docs/_build/html/{.buildinfo,objects.inv}

%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
# From: https://athoscr.fedorapeople.org/packaging/python-setuptools_scm_git_archive.spec
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l %{srcname}

install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r docs/_build/man/%{name}.1 "$RPM_BUILD_ROOT%{_mandir}/man1"

%check
%pyproject_check_import

%if %{with tests}
sh build.sh tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS.rst README.rst CONTRIBUTING.rst

%files
%license LICENSE
%{_bindir}/vdirsyncer
%{_mandir}/man1/%{name}.1.*

# Still one rpmlint warning due to BZ 1107813
# W: wrong-file-end-of-line-encoding /usr/share/doc/vdirsyncer-doc/html/_static/jquery.js
%files doc
%doc docs/_build/html docs/_build/text

%changelog
%autochangelog
