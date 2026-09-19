%global source0_hash af9f0e8fb4b8aa75466e4b70be6c0405dffe8d0c0e616dbccdcb7d51fdfcb841

Name:           perl-Hardware-Verilog-Parser
Version:        0.13
Release:        48%{?dist}
Summary:        Complete grammar for parsing Verilog code using perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hardware-Verilog-Parser
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSLONDON/Hardware-Verilog-Parser-%{version}.tar.gz
Patch0:         Hardware-Verilog-Parser-0.13-grammar.patch
Patch1:         Hardware-Verilog-Parser-0.13-rt51080.patch
Patch2:         Hardware-Verilog-Parser-0.13-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Filter bogus requires/provides of PrecompiledParser
%global __provides_exclude ^perl\\((Parse::RecDescent::)?PrecompiledParser\\)
%global __requires_exclude ^perl\\(PrecompiledParser\\)

%description
This module defines the complete grammar needed to parse any Verilog code.
By overloading this grammar, it is possible to easily create perl scripts
which run through Verilog code and perform specific functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hardware-Verilog-Parser-%{version}

# Fix shellbangs
find . -type f | xargs perl -pi -e 's|#! /bin/perl|#! /usr/bin/perl|'

# Fix FTBFS due to typos in grammar (#839599)
%patch -P0

# Fix "Use of uninitialized value in array dereference" (CPAN RT#51080)
%patch -P1

#Fix building on Perl without '.' in @INC
%patch -P2 -p1

%build
./generate_precompiled_parser.pl
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT

%check
# CPAN RT#51080
perl -Iblib/lib ./parser.pl ./test1.v

make test

%files
%doc Changes readme.txt test1.v
%{perl_vendorlib}/Hardware/Verilog/
%{_mandir}/man3/Hardware::Verilog::Parser.3pm*

%changelog
%autochangelog
