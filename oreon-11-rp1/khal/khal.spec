%global source0_hash 2b51679d80662b2d65e757c509813bd72b496043d789839bfd970f0026da687d
%bcond_with tests
Name:       khal
Version:    0.14.1
Release:        1%{?dist}
Summary:        CLI calendar application
License:    MIT
URL:        https://github.com/pimutils/%{name}
Source0:        https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz
Patch0:     khal-0.8.2-sphinx-docfix.patch
Patch1:     khal-0.13.0-support-py3.14.patch
Patch2:     khal-0.13.0-reduce-setuptools-req.patch
BuildArch:  noarch
Requires:       python3-click >= 3.2
Requires:       python3-click-log >= 0.2.0
Requires:       python3-configobj
Requires:       python3-dateutil
Requires:       python3-icalendar
Requires:       python3-urwid
Requires:       python3-tzlocal
Requires:       python3-pytz
Requires:       python3-pyxdg
Requires:       vdirsyncer >= 0.8.1-2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-khal = %{version}-%{release}
# /oreon:deps
%package -n       python3-khal+proctitle
Summary:        Metapackage for python3-khal proctitle extras
Requires:       python3-khal = %{version}-%{release}
Provides:       python3dist(khal[proctitle]) = %{version}-%{release}

%description -n python3-khal+proctitle
Metapackage for python3-khal proctitle extras.

%package -n       python3-khal+test
Summary:        Metapackage for python3-khal test extras
Requires:       python3-khal = %{version}-%{release}
Provides:       python3dist(khal[test]) = %{version}-%{release}

%description -n python3-khal+test
Metapackage for python3-khal test extras.

%package -n       python3-khal+docs
Summary:        Metapackage for python3-khal docs extras
Requires:       python3-khal = %{version}-%{release}
Requires:       python3dist(sphinx)
Provides:       python3dist(khal[docs]) = %{version}-%{release}

%description -n python3-khal+docs
Metapackage for python3-khal docs extras.

%package -n       python3-khal+all
Summary:        Metapackage for python3-khal all extras
Requires:       python3-khal = %{version}-%{release}
Provides:       python3dist(khal[all]) = %{version}-%{release}

%description -n python3-khal+all
Metapackage for python3-khal all extras.

%description
Khal is a standards based CLI (console) calendar program. CalDAV compatibility
is achieved by using vdir/vdirsyncer as a back-end, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
cd doc
PYTHONPATH=.. make SPHINXBUILD=sphinx-build-3 man html text
cd ..
%install
%pyproject_install
install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r doc/build/man/%{name}.1 "$RPM_BUILD_ROOT%{_mandir}/man1"
rm -vrf doc/build/html/_sources
rm -fv doc/build/html/{.buildinfo,objects.inv}
%oreon_autofiles main

%check

%pyproject_check_import
%if %{with tests}
%tox
%endif
%files

%changelog

%autochangelog
