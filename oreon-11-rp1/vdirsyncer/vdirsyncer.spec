%global source0_hash b6ac040b880da6758f65c17a369572f62e7323be8d21cd330c26fa134d1b1373
%bcond tests 0
%bcond old_setuptools 0
%global sum Synchronize calendars and contacts
%global srcname vdirsyncer
%global _docdir_fmt %{name}
Name:       vdirsyncer
Version:    0.21.0
Release:        1%{?dist}
Summary:        Synchronize calendars and contacts
License:    BSD-3-Clause
URL:        https://github.com/pimutils/%{name}
Source0:        https://files.pythonhosted.org/packages/source/v/vdirsyncer/vdirsyncer-%{version}.tar.gz
Patch1000:  vdirsyncer-revert-license-metadata-update.diff
BuildArch:  noarch
Obsoletes:  python2-%{srcname} <= 0.12.1
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
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-vdirsyncer = %{version}-%{release}
# /oreon:deps
%package -n       python3-vdirsyncer+google
Summary:        Metapackage for python3-vdirsyncer google extras
Requires:       python3-vdirsyncer = %{version}-%{release}
Provides:       python3dist(vdirsyncer[google]) = %{version}-%{release}

%description -n python3-vdirsyncer+google
Metapackage for python3-vdirsyncer google extras.

%package -n       python3-vdirsyncer+test
Summary:        Metapackage for python3-vdirsyncer test extras
Requires:       python3-vdirsyncer = %{version}-%{release}
Requires:       python3dist(hypothesis) >= 6.72.0
Requires:       python3dist(hypothesis) < 7.0.0
Provides:       python3dist(vdirsyncer[test]) = %{version}-%{release}

%description -n python3-vdirsyncer+test
Metapackage for python3-vdirsyncer test extras.

%package -n       python3-vdirsyncer+docs
Summary:        Metapackage for python3-vdirsyncer docs extras
Requires:       python3-vdirsyncer = %{version}-%{release}
Requires:       python3dist(sphinx)
Provides:       python3dist(vdirsyncer[docs]) = %{version}-%{release}

%description -n python3-vdirsyncer+docs
Metapackage for python3-vdirsyncer docs extras.

%package -n       python3-vdirsyncer+check
Summary:        Metapackage for python3-vdirsyncer check extras
Requires:       python3-vdirsyncer = %{version}-%{release}
Provides:       python3dist(vdirsyncer[check]) = %{version}-%{release}

%description -n python3-vdirsyncer+check
Metapackage for python3-vdirsyncer check extras.

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

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
export PYTHONPATH=`pwd`
cd docs
make SPHINXBUILD=sphinx-build-3 man html text
cd ..
unset PYTHONPATH
rm -vrf docs/_build/html/_sources
rm -fv docs/_build/html/{.buildinfo,objects.inv}
%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r docs/_build/man/%{name}.1 "$RPM_BUILD_ROOT%{_mandir}/man1"
%oreon_autofiles main usr/lib/python3*/site-packages/vdirsyncer* usr/lib64/python3*/site-packages/vdirsyncer* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%if %{with tests}
sh build.sh tests
%endif
%files
%files -n python3-vdirsyncer -f %{oreon_filedir}/python3-vdirsyncer.list
%files -n vdirsyncer-doc -f %{oreon_filedir}/vdirsyncer-doc.list

%changelog

%autochangelog
