%global source0_hash b060f6eb322b75479fcfd80af6c928c806d56a79f9974a363dd5b85828121df2
Name:       perl-WWW-Mechanize-GZip 
Version:    0.14
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:        Fetch compressed web pages
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEGI/WWW-Mechanize-GZip-%{version}.tar.gz
Url:        https://metacpan.org/release/WWW-Mechanize-GZip
BuildArch:  noarch
Requires:      perl(WWW::Mechanize)
Requires:      perl(Compress::Zlib)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl-generators
# /oreon:deps
%description
The WWW::Mechanize::GZip module tries to fetch a URL by requesting 
gzip-compression from the web server.  If the response contains
a header with 'Content-Encoding: gzip', it decompresses the response in
order to get the original (uncompressed) content. This module will help
to reduce bandwidth fetching web pages, if supported by the web server.
If the web server does not support gzip-compression, no decompression
will be made.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Mechanize-GZip-%{version}
find . -type f -exec chmod -x -c {} \;

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
