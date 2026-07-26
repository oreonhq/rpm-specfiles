%global source0_hash 809ee2f11705706b33c54312b5c7bee674838f2beaaedaf8cb945e702aae39b6

Name:           perl-HTML-FormatText-WithLinks-AndTables
Version:        0.07
Release:        29%{?dist}
Summary:        Converts HTML to Text with tables in tact
License:        Artistic-2.0
URL:            https://metacpan.org/release/HTML-FormatText-WithLinks-AndTables
BuildArch:      noarch

Source0:        https://cpan.metacpan.org/authors/id/D/DA/DALEEVANS/HTML-FormatText-WithLinks-AndTables-%{version}.tar.gz

# build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module was inspired by HTML::FormatText::WithLinks which has proven to
be a useful "lynx -dump" work-alike. However one frustration was that no
other HTML converters I came across had the ability to deal effectively
with HTML <TABLE>s. This module can in a rudimentary sense do so. The aim
was to provide facility to take a simple HTML based email template, and to
also convert it to text with the <TABLE> structure intact for inclusion as
"multi-part/alternative" content. Further, it will preserve both the
formatting specified by the <TD> tag's "align" attribute, and will also
preserve multi-line text inside of a <TD> element provided it is broken
using <BR/> tags.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormatText-WithLinks-AndTables-%{version}
/usr/bin/chmod -x Changes

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
