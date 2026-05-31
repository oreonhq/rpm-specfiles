%global source0_hash e8baa07b1b3f53e00af3636898bbf73aec9a0ff38f94536ede1dbe96ef086f04

Name:           perl-Text-Diff
Version:        1.45
Release:        25%{?dist}
Summary:        Perform diffs on files and record sets
# lib/Text/Diff.pm - GPL-2.0-or-later OR Artistic-1.0-Perl
# lib/Text/Diff/Config.pm - MIT
# lib/Text/Diff/Table.pm - GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:            https://metacpan.org/release/Text-Diff
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:       perl(Algorithm::Diff) >= 1.19

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Algorithm::Diff\\)$

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.45-25
- Prepare for Oreon 11 (RP1)
