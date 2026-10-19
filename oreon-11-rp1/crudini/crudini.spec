%global source0_hash 66c8b9f1303862923aeac200d655da81d025b852f1bf122fa7608b0f51ffd1fa
Name:           crudini
Version:        0.9.6
Release:        4%{?dist}
Summary:        A utility for manipulating ini files
License:        GPL-2.0-only
URL:            https://github.com/pixelb/%{name}
Source0:        https://github.com/pixelb/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-iniparse >= 0.3.2
Patch0:         crudini-el6.patch
Patch1:         crudini-py2.patch
Patch2:         crudini-py3.patch
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  grep
BuildRequires:  python3-devel
BuildRequires:  python3-iniparse
BuildRequires:  python3-setuptools
# /oreon:deps
%description
A utility for easily handling ini files from the command line and shell
scripts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P2 -p1

%build

%install
install -p -D -m 0755 %{name}.py %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%check

pushd tests
LC_ALL=en_US.utf8 ./test.sh
popd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
