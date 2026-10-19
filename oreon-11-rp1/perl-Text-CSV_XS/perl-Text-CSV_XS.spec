%global source0_hash 65c5662d4fe8ef3039a1b32f641634d0aae6ab10eabbb24f740c75332f2caf30
Name:           perl-Text-CSV_XS
Version:        1.64
Release:        1%{?dist}
Summary:        Comma-separated values manipulation routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-CSV_XS
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-%{version}.tgz
Requires:       perl(Encode)
Requires:       perl(IO::Handle)
Requires:       perl(UNIVERSAL::isa)
%{?perl_default_filter}
Provides:       perl(Text::CSV_XS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(UNIVERSAL::isa)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-CSV_XS-%{version}

chmod -c a-x examples/*

# Upstream does this on purpose (2011-03-23):
# "As Text::CSV_XS is so low-level, most of these files are actually *examples*
# and not ready-to-run out-of-the-box scripts that work as expected, though
# I must admit that some have evolved into being like that."
#find . -type f -exec sed -i '1s/pro/usr/' {} \;

%build

perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}" \
  NO_PACKLIST=true \
  NO_PERLLOCAL=true
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
