%global source0_hash 8b9b560131c398e5245fef3f00fe7458825889f6e4aeca48d6f3af23f4a4d8ab

Name:           perl-Syntax-Highlight-Perl6
Version:        0.88
Release:        42%{?dist}
Summary:        Perl 6 Syntax Highlighter
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND Artistic-2.0 AND ( MIT OR GPL-2.0-only )
URL:            https://metacpan.org/release/Syntax-Highlight-Perl6
Source0:        https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Syntax-Highlight-Perl6-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.03
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(open)
BuildRequires:  perl(STD) >= 32116
BuildRequires:  perl(Term::ANSIColor) >= 2.00
BuildRequires:  perl(utf8)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(Encode)
Requires:       perl(File::ShareDir)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(STD) >= 32116
Requires:       perl(Term::ANSIColor)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(STD\\)\s*$

%description
Syntax::Highlight::Perl6 parses Perl 6 source code using an embedded
STD.pm. It matches parse tree nodes to colors then returns them in
different output formats. It can be used to create web pages with colorful
source code samples in its simple and snippet HTML modes, or it can be used
as a learning tool in examining STD.pm's output using the JavaScript node
viewer in its full HTML mode. Or you can use its parse tree Perl 5 records
to build your next great idea.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Syntax-Highlight-Perl6-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=perl \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} OPTIMIZE="$RPM_OPT_FLAGS"

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_privlib}/Syntax*
%{perl_privlib}/auto/*
%{_bindir}/hilitep6
%{_mandir}/man1/hilitep6*
%{_mandir}/man3/Syntax::Highlight::Perl*

%changelog
%autochangelog
