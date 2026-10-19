%global source0_hash 3fc983e3140fa2580250bbcf2b52e2acbdbc5abda4374c3be78235905d8ca8eb
Name:           perl-Text-Diff
Version:        1.46
Release:        1%{?dist}
Summary:        Perform diffs on files and record sets
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:            https://metacpan.org/release/Text-Diff
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Algorithm::Diff) >= 1.19
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Algorithm::Diff\\)$
Provides:       perl(Text::Diff)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Text::Diff provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is better
integrated with Perl and available on all platforms. It is often faster
than shelling out to a system's diff executable for small files, and
generally slower on larger files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-Diff-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
