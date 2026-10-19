%global source0_hash cb0a0dd8aa5e8ba9ca214ce451bf4df33aa09c13e907e8d3082ddafeb30151cc
Name:           perl-HTML-Formatter
Version:        2.16
Release:        1%{?dist}
Summary:        HTML formatter modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Formatter
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-Formatter-%{version}.tar.gz
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
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
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
