%global source0_hash 09f4aecf1bd8efdd3f9b39f16a240c4e9ceb61eb295b88145c96eb9d58504a2a
Name:		perl-SQL-ReservedWords
Version:	0.8
Release:        1%{?dist}
Summary:        Determine if words are reserved by ANSI/ISO SQL standard
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/SQL-ReservedWords
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/SQL-ReservedWords-%{version}.tar.gz
Patch0:		SQL-ReservedWords-0.8-build.patch
BuildArch:	noarch
Requires:	perl(Sub::Exporter)
Requires:	perl(Pod::Usage)
# oreon:deps
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl-generators
# /oreon:deps
%description
Determine if words are reserved by ANSI/ISO SQL standard.  There are also
sub modules that determine if a particular database server reserves the word.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-ReservedWords-%{version}
%patch -P0 -p1

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
