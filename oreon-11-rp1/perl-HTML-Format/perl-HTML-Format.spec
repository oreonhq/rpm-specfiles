%global source0_hash cb0a0dd8aa5e8ba9ca214ce451bf4df33aa09c13e907e8d3082ddafeb30151cc
Name:           perl-HTML-Format
Version:        2.16
Release:        1%{?dist}
Summary:        HTML formatter modules
%if "%{version}" > "2.12"
%global tarname HTML-Formatter
%else
%global tarname HTML-Format
%endif
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{tarname}
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/%{tarname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
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
# /oreon:deps
%description
A collection of modules that formats HTML as plaintext, PostScript or RTF.

%if "%{version}" > "2.12"
%package -n perl-%{tarname}
Summary:        HTML formatter modules
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
Obsoletes: perl-HTML-Format < %{version}-%{release}
Provides: perl-HTML-Format = %{version}-%{release}
%description -n perl-%{tarname}
A collection of modules that formats HTML as plaintext, PostScript or RTF.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarname}-%{version}

%build

%{__perl} Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__make} test
%if "%{version}" > "2.12"
%files -f %{oreon_filedir}/main.list
%files -n perl-HTML-Formatter -f %{oreon_filedir}/perl-HTML-Formatter.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.16-29
- Prepare for Oreon 11 (RP1)
%endif
