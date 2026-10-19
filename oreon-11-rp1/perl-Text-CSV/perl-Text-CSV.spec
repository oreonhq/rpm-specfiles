%global source0_hash dfcaec925a788b0ba41e51bc6d16e21b0e98b4c7af9b79395090add75f5e506f
Name:       perl-Text-CSV
Version:    2.06
Release:        2%{?dist}
Summary:        Comma-separated values manipulator
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Text-CSV
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Text-CSV-%{version}.tar.gz
BuildArch:  noarch
Requires:       perl(IO::Handle)
Suggests:       perl(Text::CSV_XS) >= 1.59
%{?perl_default_filter}
Provides:       perl(Text::CSV)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(charnames)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

The module accepts either strings or files as input and can utilize any
user-specified characters as delimiters, separators, and escapes so it is
perhaps better called ASV (anything separated values) rather than just CSV.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-CSV-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%check

make test TEST_VERBOSE=1
%install
%{make_install}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
