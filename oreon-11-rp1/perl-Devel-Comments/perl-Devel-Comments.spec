%global source0_hash 57a8676b1a484835b6062b855a606f78a36cc60b470cac4f9984940651a83b60

Name:           perl-Devel-Comments
Version:        1.1.4
Release:        40%{?dist}
Summary:        Debug with executable smart comments to logs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Comments
Source0:        https://cpan.metacpan.org/authors/id/X/XI/XIONG/developer-tools/Devel-Comments-v%{version}.tar.gz
BuildArch:      noarch
# Compile-time:
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Filter::Simple) >= 0.8
BuildRequires:  perl(IO::Capture::Tie_STDx)
BuildRequires:  perl(IO::Capture::Stdout)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Text::Balanced) >= 2
BuildRequires:  perl(version) >= 0.77
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(IO::Capture::Stderr::Extended)
BuildRequires:  perl(IO::Capture::Stdout::Extended)
Requires:       perl(Filter::Simple) >= 0.8
Requires:       perl(Test::More) >= 0.94
Requires:       perl(Text::Balanced) >= 2

# Remove under-specifed dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Filter::Simple|Text::Balanced\\)\\s*$

%description
Devel::Comments is a source filter for your Perl code, intended to be used
only during development. Specially-formatted 'smart' comments are replaced by
executable code to dump variables to screen or to file, display loop progress
bars, or enforce conditions. These smart comments can all be disabled at once
by commenting out the "use Devel::Comments" line, whereupon they return to
being simple, dumb comments. Your debugging code can remain in place,
guaranteed harmless, ready for the next development cycle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Comments-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
