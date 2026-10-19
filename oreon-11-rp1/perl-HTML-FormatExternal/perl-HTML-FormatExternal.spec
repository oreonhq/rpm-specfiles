%global source0_hash 3c59f233d0b10686a85aed0c994011cec68626da0128dea90b5c4fdc1746cfc3
%bcond_without perl_HTML_FormatExternal_enables_optional_test
%bcond_without perl_HTML_FormatExternal_enables_elinks
%bcond_without perl_HTML_FormatExternal_enables_html2text
%bcond_without perl_HTML_FormatExternal_enables_links
%bcond_without perl_HTML_FormatExternal_enables_lynx
%bcond_with perl_HTML_FormatExternal_enables_netrik
%bcond_with perl_HTML_FormatExternal_enables_vilistextum
%bcond_without perl_HTML_FormatExternal_enables_w3m
%bcond_with perl_HTML_FormatExternal_enables_zen
Name:           perl-HTML-FormatExternal
Version:        26
Release:        21%{?dist}
Summary:        HTML to text formatting using external programs
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/HTML-FormatExternal
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/HTML-FormatExternal-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_HTML_FormatExternal_enables_optional_test}
%endif
Requires:       perl(Encode)
Requires:       perl(File::Copy)
Requires:       perl(File::Temp) >= 0.18
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(URI::file\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Taint::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(constant)
BuildRequires:  perl(constant::defer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a common base for formatter modules which turn HTML into plain text
by dumping it through the respective external programs. Available modules are:

%{?with_perl_HTML_FormatExternal_enables_elinks:HTML::FormatText::Elinks}
%{?with_perl_HTML_FormatExternal_enables_html2text:HTML::FormatText::Html2text}
%{?with_perl_HTML_FormatExternal_enables_links:HTML::FormatText::Links}
%{?with_perl_HTML_FormatExternal_enables_lynx:HTML::FormatText::Lynx}
%{?with_perl_HTML_FormatExternal_enables_netrik:HTML::FormatText::Netrik}
%{?with_perl_HTML_FormatExternal_enables_vilistextum:HTML::FormatText::Vilistextum}
%{?with_perl_HTML_FormatExternal_enables_w3m:HTML::FormatText::W3m}
%{?with_perl_HTML_FormatExternal_enables_zen:HTML::FormatText::Zen}

%if %{with perl_HTML_FormatExternal_enables_elinks}
%package Elinks
Summary:        Format HTML as plain text using ELinks
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       elinks
Requires:       perl(URI::file) >= 0.08
%description Elinks
This Perl module turns HTML into plain text using the ELinks program.
%endif

%if %{with perl_HTML_FormatExternal_enables_html2text}
%package Html2text
Summary:        Format HTML as plain text using html2text
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       python3-html2text
%description Html2text
This Perl module turns HTML into plain text using the html2text program.
%endif

%if %{with perl_HTML_FormatExternal_enables_links}
%package Links
Summary:        Format HTML as plain text using Links
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       links
Requires:       perl(URI::file) >= 0.08
%description Links
This Perl module turns HTML into plain text using the Links program.
%endif

%if %{with perl_HTML_FormatExternal_enables_lynx}
%package Lynx
Summary:        Format HTML as plain text using Lynx
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       lynx
Requires:       perl(URI::file) >= 0.08
%description Lynx
This Perl module turns HTML into plain text using the Lynx program.
%endif

%if %{with perl_HTML_FormatExternal_enables_netrik}
%package Netrik
Summary:        Format HTML as plain text using Netrik
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       netrik
Requires:       perl(URI::file) >= 0.08
%description Netrik
This Perl module turns HTML into plain text using the Netrik program.
%endif

%if %{with perl_HTML_FormatExternal_enables_vilistextum}
%package Vilistextum
Summary:        Format HTML as plain text using Vilistextum
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       vilistextum
%description Vilistextum
This Perl module turns HTML into plain text using the Vilistextum program.
%endif

%if %{with perl_HTML_FormatExternal_enables_w3m}
%package W3m
Summary:        Format HTML as plain text using w3m
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       perl(URI::file) >= 0.08
Requires:       w3m
%description W3m
This Perl module turns HTML into plain text using the w3m program.
%endif

%if %{with perl_HTML_FormatExternal_enables_zen}
%package Zen
Summary:        Format HTML as plain text using Zen
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       zen
%description Zen
This Perl module turns HTML into plain text using the Zen program.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormatExternal-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_PERL_SWITCHES=-T
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-HTML-FormatExternal-Elinks -f %{oreon_filedir}/perl-HTML-FormatExternal-Elinks.list
%files -n perl-HTML-FormatExternal-Html2text -f %{oreon_filedir}/perl-HTML-FormatExternal-Html2text.list
%files -n perl-HTML-FormatExternal-Links -f %{oreon_filedir}/perl-HTML-FormatExternal-Links.list
%files -n perl-HTML-FormatExternal-Lynx -f %{oreon_filedir}/perl-HTML-FormatExternal-Lynx.list
%files -n perl-HTML-FormatExternal-W3m -f %{oreon_filedir}/perl-HTML-FormatExternal-W3m.list

%changelog

%autochangelog
