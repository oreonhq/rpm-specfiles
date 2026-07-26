%global source0_hash 04fc21de858863560423e79c822f405225f829afd8e5d62293099fbef341f9e8

%global srcname flent

Name:             flent
Version:          2.2.0
Release:          8%{?dist}
Summary:          FLExible Network Tester for bufferbloat testing and more

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later
URL:              https://flent.org/
Source0:          %{pypi_source}

BuildArch:        noarch
BuildRequires:    python3-devel python3-sphinx desktop-file-utils libappstream-glib python3-setuptools make
Recommends:       python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-QtPy
Requires:         fping netperf golang-github-heistp-irtt

%description
The FLExible Network Tester is a Python wrapper to run multiple simultaneous
netperf/iperf/ping instances and aggregate the results.

Tests are specified as config files (which are really Python), and
various parsers for tool output are supplied. At the moment, parsers for
netperf in -D mode, iperf in csv mode and ping/ping6 in -D mode are
supplied, as well as a generic parser for commands that just outputs a
single number.

Several commands can be run in parallel and, provided they output
timestamped values, (which netperf ping and iperf do, the latter with a
small patch, available in the misc/ directory), the test data points can
be aligned with each other in time, interpolating differences between
the actual measurement points. This makes it possible to graph (e.g.)
ping times before, during and after a link is loaded.

%package doc
Summary:          Documentation for Flent: The FLExible Network Tester
BuildArch:        noarch

%description doc
Documentation for users of The FLExible Network Tester

The FLExible Network Tester is a Python wrapper to run multiple simultaneous
netperf/iperf/ping instances and aggregate the results.

Tests are specified as config files (which are really Python), and
various parsers for tool output are supplied. At the moment, parsers for
netperf in -D mode, iperf in csv mode and ping/ping6 in -D mode are
supplied, as well as a generic parser for commands that just outputs a
single number.

Several commands can be run in parallel and, provided they output
timestamped values, (which netperf ping and iperf do, the latter with a
small patch, available in the misc/ directory), the test data points can
be aligned with each other in time, interpolating differences between
the actual measurement points. This makes it possible to graph (e.g.)
ping times before, during and after a link is loaded.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%make_build -C doc/ html PYTHON=%{__python3} SPHINXBUILD=sphinx-build-3
rm -f doc/_build/html/index.html doc/_build/html/.buildinfo

%install
%pyproject_install

%check
%make_build test PYTHON=%{__python3}
desktop-file-validate %{buildroot}/%{_datadir}/applications/flent.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%{python3_sitelib}/flent
%{python3_sitelib}/%{srcname}-*.dist-info/
%{_bindir}/flent
%{_bindir}/flent-gui
%{_datadir}/applications/flent.desktop
%{_datadir}/mime/packages/flent-mime.xml
%{_metainfodir}/flent.appdata.xml
%{_mandir}/man1/flent.1.gz
%doc README.rst CHANGES.md BUGS batchfile.example flentrc.example flent-paper.batch misc/
%license LICENSE

%files doc
%doc doc/_build/html

%changelog
%autochangelog
