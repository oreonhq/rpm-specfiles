%global source0_hash 669ee27120ae71589f638fe3a167d6ea54f8633f5ab1b282551bd7a7c9510dfa
Summary:        Text file format converters
Name: dos2unix
Version: 7.5.7
Release:        1%{?dist}
License: BSD-3-Clause
URL: https://waterlander.net/dos2unix.html
Source0:        https://waterlander.net/dos2unix/files/%{name}-%{version}.tar.gz
Provides: unix2dos = %{version}-%{release}
Obsoletes: unix2dos < 5.1-1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-Test-Harness
BuildRequires:  perl-Test-Simple
# /oreon:deps
%description
Convert text files with DOS or Mac line endings to Unix line endings and
vice versa.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%make_build LDFLAGS="%{build_ldflags}" prefix=%{_prefix}
%install
%make_install prefix=%{_prefix}
rm -rf %{buildroot}%{_docdir}
%find_lang %{name} --with-man --all-name
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5.3-3
- Prepare for Oreon 11 (RP1)
