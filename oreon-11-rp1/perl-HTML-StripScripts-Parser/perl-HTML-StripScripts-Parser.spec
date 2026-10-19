%global source0_hash 478c1a4e46eb77fa7bce96ba288168f0b98c27f250e00dc6312365081aed3407
Name:           perl-HTML-StripScripts-Parser
Version:        1.03
Release:        1%{?dist}
Summary:        XSS filter using HTML::Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-StripScripts-Parser
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRTECH/HTML-StripScripts-Parser-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTML::Parser) >= 3.56
Requires:       perl(HTML::StripScripts) >= 1.04
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::StripScripts)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
%description
This class provides an easy interface to HTML::StripScripts, using
HTML::Parser to parse the HTML.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-StripScripts-Parser-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
