%global source0_hash f6535b4e73766ea745606f8a9b16080efa69e5756cda5f7b9d1457dd9515d99a

%global srcname whisper
%global sum Whisper is a file-based time-series database format for Graphite

Name:           python-whisper
Version:        1.1.10
Release:        12%{?dist}
Summary:        %{sum}

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/graphite-project/whisper

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source10:       rrd2whisper.1
Source11:       whisper-create.1
Source12:       whisper-dump.1
Source13:       whisper-fetch.1
Source14:       whisper-info.1
Source15:       whisper-merge.1
Source16:       whisper-resize.1
Source17:       whisper-set-aggregation-method.1
Source18:       whisper-update.1
Source19:       whisper-fill.1

Patch0:         python-whisper-1.1.10-whisper-resize-test-fix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Whisper is a fixed-size database, similar in design and purpose to RRD
(round-robin-database). It provides fast, reliable storage of numeric
data over time. Whisper allows for higher resolution (seconds per point)
of recent data to degrade into lower resolutions for long-term retention
of historical data.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Python%{python3_pkgversion} version of the Graphite whisper module

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# remove .py suffix
for i in %{buildroot}%{_bindir}/*.py; do
    mv ${i} ${i%%.py}
done

# man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE10} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE11} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE12} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE13} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE14} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE15} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE16} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE17} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE18} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE19} %{buildroot}%{_mandir}/man1

%check
%{__python3} test_whisper.py

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/find-corrupt-whisper-files
%{_bindir}/rrd2whisper
%{_bindir}/update-storage-times
%{_bindir}/whisper-auto-resize
%{_bindir}/whisper-auto-update
%{_bindir}/whisper-create
%{_bindir}/whisper-dump
%{_bindir}/whisper-diff
%{_bindir}/whisper-fetch
%{_bindir}/whisper-fill
%{_bindir}/whisper-info
%{_bindir}/whisper-merge
%{_bindir}/whisper-resize
%{_bindir}/whisper-set-aggregation-method
%{_bindir}/whisper-set-xfilesfactor
%{_bindir}/whisper-update
%{_mandir}/man1/rrd2whisper.1*
%{_mandir}/man1/whisper-create.1*
%{_mandir}/man1/whisper-dump.1*
%{_mandir}/man1/whisper-fetch.1*
%{_mandir}/man1/whisper-fill.1*
%{_mandir}/man1/whisper-info.1*
%{_mandir}/man1/whisper-merge.1*
%{_mandir}/man1/whisper-resize.1*
%{_mandir}/man1/whisper-set-aggregation-method.1*
%{_mandir}/man1/whisper-update.1*

%changelog
%autochangelog
