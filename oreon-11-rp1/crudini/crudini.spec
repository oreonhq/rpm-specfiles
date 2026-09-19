%global source0_hash 66c8b9f1303862923aeac200d655da81d025b852f1bf122fa7608b0f51ffd1fa

Name:           crudini
Version:        0.9.6
Release:        4%{?dist}
Summary:        A utility for manipulating ini files

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/pixelb/%{name}
Source0:        https://github.com/pixelb/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  diffutils
BuildRequires:  grep
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
BuildRequires:  python2-devel
BuildRequires:  python-iniparse
Requires:       python-iniparse
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-iniparse >= 0.3.2
Requires:       python3-iniparse >= 0.3.2
%endif

Patch0:         crudini-el6.patch
Patch1:         crudini-py2.patch
Patch2:         crudini-py3.patch

%description
A utility for easily handling ini files from the command line and shell
scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%if 0%{?rhel} == 6
%patch -P0 -p1
%endif
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
%patch -P1 -p1
%else
%patch -P2 -p1
%endif

%build

%install
install -p -D -m 0755 %{name}.py %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
pushd tests
LC_ALL=en_US.utf8 ./test.sh
popd

%files
%doc README.md COPYING TODO NEWS example.ini
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
%autochangelog
