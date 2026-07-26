%global source0_hash 1e3db191853d235c42c7d2a5dc2ea055158ff29c7d54c5c673d271cdbd43bc6a

Name:           perl-XML-SAX-ExpatXS
Version:        1.33
Release:        46%{?dist}
Summary:        Perl SAX 2 XS extension to Expat parser
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-SAX-ExpatXS
Source0:        https://cpan.metacpan.org/authors/id/P/PC/PCIMPRICH/XML-SAX-ExpatXS-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.4.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::SAX) >= 0.96
BuildRequires:  perl(XML::SAX::Base)
# Tests:
BuildRequires:  perl(Test)
Requires:       perl(XML::SAX) >= 0.96

%description
XML::SAX::ExpatXS is a direct XS extension to Expat XML parser. It implements
Perl SAX 2.1 interface <http://perl-xml.sourceforge.net/perl-sax/>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-SAX-ExpatXS-%{version}
chmod -x ExpatXS.xs

%build
echo n | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%triggerin -- perl-XML-SAX
%{_bindir}/perl -MXML::SAX -e \
  'XML::SAX->add_parser(q(XML::SAX::ExpatXS))->save_parsers()' 2>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
    %{_bindir}/perl -MXML::SAX -e \
        'XML::SAX->remove_parser(q(XML::SAX::ExpatXS))->save_parsers()' \
        2>/dev/null || :
fi

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/XML*
%{_mandir}/man3/*

%changelog
%autochangelog
