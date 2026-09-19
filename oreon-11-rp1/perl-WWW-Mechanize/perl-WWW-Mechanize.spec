%global source0_hash 5adce695f3968565d3c8e597b988525ee4c89f40ecb1a21ecee7a16532dbb668

Name:           perl-WWW-Mechanize
Version:        2.20
Release:        2%{?dist}
Summary:        Automates web page form & link interaction
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/WWW-Mechanize
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(HTML::Form) >= 6.08
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Request) >= 1.3
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(bytes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Message) >= 7.01
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings) >= 1.04
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
# $mech->content( format => 'text' ) requires HTML::TreeBuilder to be installed
# https://metacpan.org/pod/WWW::Mechanize#$mech-%3Econtent(...)
Requires:       perl(HTML::TreeBuilder)

%description
"WWW::Mechanize", or Mech for short, helps you automate interaction
with a website.  It supports performing a sequence of page fetches
including following links and submitting forms. Each fetched page is
parsed and its links and forms are extracted. A link or a form can be
selected, form fields can be filled and the next page can be fetched.
Mech also stores a history of the URLs you've visited, which can be
queried and revisited.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Mechanize-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test TEST_VERBOSE=1

%files
%doc Changes etc/www-mechanize-logo.png
%{_bindir}/mech-dump
%dir %{perl_vendorlib}/WWW
%{perl_vendorlib}/WWW/Mechanize
%{perl_vendorlib}/WWW/Mechanize.pm
%{_mandir}/man1/mech-dump.1*
%{_mandir}/man3/WWW::Mechanize.3pm*
%{_mandir}/man3/WWW::Mechanize::*.3pm*

%changelog
%autochangelog
