%global source0_hash 28a4b0d9f9179da4e44c567b9c01f818b070a20827115fffd96f760dcfa0f3b2

Summary: Text file format converters
Name: dos2unix
Version: 7.5.3
Release: 3%{?dist}
License: BSD-3-Clause
URL: https://waterlan.home.xs4all.nl/dos2unix.html
Source: https://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
Source: https://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz.asc
Source: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x38C1F572B12725BE#./38C1F572B12725BE.asc

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: make
# perl modules, required for tests
BuildRequires: perl-Test-Harness
BuildRequires: perl-Test-Simple
# for gpg signature verification
BuildRequires: gnupg2

Provides: unix2dos = %{version}-%{release}
Obsoletes: unix2dos < 5.1-1

%description
Convert text files with DOS or Mac line endings to Unix line endings and
vice versa.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%make_build LDFLAGS="%{build_ldflags}" prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

# We add doc files manually to %%doc
rm -rf %{buildroot}%{_docdir}

%find_lang %{name} --with-man --all-name

%check
make test

%files -f %{name}.lang
%license COPYING.txt
%doc man/man1/dos2unix.htm ChangeLog.txt
%doc NEWS.txt README.txt TODO.txt
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2dos
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5.3-3
- Prepare for Oreon 11 (RP1)
