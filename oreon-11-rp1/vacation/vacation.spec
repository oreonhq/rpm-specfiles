%global source0_hash 3cb72c2b728bc0c7cccdb90be90da93e0ea495f869220a4a027cfed78f7a46dd

Summary: Automatic mail answering program
Summary(de): Programm zum automatisierten Beantworten von Mails
Name: vacation
Version: 1.2.7.1
Release: 31%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source: http://downloads.sourceforge.net/vacation/%{name}-1.2.7.1.tar.gz
Source1: license-clarification
Requires: smtpdaemon perl(GDBM_File)
URL: http://sourceforge.net/projects/vacation/
BuildRequires: make
BuildRequires: gdbm-devel
BuildRequires: perl-generators
BuildRequires: gcc

%description 
Vacation is the automatic mail answering program found
on many Unix systems.

%description	-l de
Vacation beantwortet automatisch alle eingehenden EMails
mit einer Standard-Antwort und ist auf vielen Unix-Systemen
vorhanden.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vacation-1.2.7.1
cp -p %SOURCE1 .

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

install -D -p -m 755 vacation        $RPM_BUILD_ROOT%{_bindir}/vacation
install -D -p -m 755 vaclook         $RPM_BUILD_ROOT%{_bindir}/vaclook
install -D -p -m 444 vaclook.man     $RPM_BUILD_ROOT%{_mandir}/man1/vaclook.1
install -D -p -m 444 vacation-en.man $RPM_BUILD_ROOT%{_mandir}/man1/vacation.1
install -D -p -m 444 vacation-de.man $RPM_BUILD_ROOT%{_mandir}/de/man1/vacation.1

%files
%{_bindir}/vacation
%{_bindir}/vaclook
%{_mandir}/man*/*
%lang(de) %{_mandir}/de/man*/*

%doc COPYING README README.smrsh ChangeLog license-clarification

%changelog
%autochangelog
