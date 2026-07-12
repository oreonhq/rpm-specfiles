%global source0_hash cb0a0dd8aa5e8ba9ca214ce451bf4df33aa09c13e907e8d3082ddafeb30151cc

Name:           perl-HTML-Formatter
Version:        2.16
Release:        31%{?dist}
Summary:        HTML formatter modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Formatter
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-Formatter-%{version}.tar.gz

BuildArch:      noarch

# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Element) >= 3.15
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(base)
BuildRequires:  perl(integer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# testing requirements
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)

BuildRequires:  perl(Font::Metrics::Courier)
BuildRequires:  perl(Font::Metrics::CourierBold)
BuildRequires:  perl(Font::Metrics::CourierBoldOblique)
BuildRequires:  perl(Font::Metrics::CourierOblique)
BuildRequires:  perl(Font::Metrics::Helvetica)
BuildRequires:  perl(Font::Metrics::HelveticaBold)
BuildRequires:  perl(Font::Metrics::HelveticaBoldOblique)
BuildRequires:  perl(Font::Metrics::HelveticaOblique)
BuildRequires:  perl(Font::Metrics::TimesBold)
BuildRequires:  perl(Font::Metrics::TimesBoldItalic)
BuildRequires:  perl(Font::Metrics::TimesItalic)
BuildRequires:  perl(Font::Metrics::TimesRoman)

Requires:       perl(Font::Metrics::Courier)
Requires:       perl(Font::Metrics::CourierBold)
Requires:       perl(Font::Metrics::CourierBoldOblique)
Requires:       perl(Font::Metrics::CourierOblique)
Requires:       perl(Font::Metrics::Helvetica)
Requires:       perl(Font::Metrics::HelveticaBold)
Requires:       perl(Font::Metrics::HelveticaBoldOblique)
Requires:       perl(Font::Metrics::HelveticaOblique)
Requires:       perl(Font::Metrics::TimesBold)
Requires:       perl(Font::Metrics::TimesBoldItalic)
Requires:       perl(Font::Metrics::TimesItalic)
Requires:       perl(Font::Metrics::TimesRoman)

Obsoletes:      perl-HTML-Format < %{version}-%{release}
Provides:       perl-HTML-Format = %{version}-%{release}

%{?perl_default_filter}

Provides:       perl(HTML::FormatText)
Provides:       perl(HTML::Formatter)
%description
A collection of modules that formats HTML as plaintext, PostScript or RTF.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTML-Formatter-%{version}

%build
/usr/bin/perl Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/HTML
%{_mandir}/man3/HTML*

%changelog
%autochangelog
