%global source0_hash 008981f868a151be41cdfded28daa37f7029b51e57c75c976b24ead91f401a68

Name:           perl-HTML-Encoding
Version:        0.61
Release:        43%{?dist}
Summary:        Determine the encoding of HTML/XML/XHTML documents

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Encoding
Source0:        https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/HTML-Encoding-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
HTML::Encoding helps to determine the encoding of HTML and XML/XHTML
documents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Encoding-%{version}
find . -type f | xargs chmod -c -x
find . -type f | xargs %{__perl} -pi -e 's/\r//g'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/HTML/
%{_mandir}/man3/HTML::Encoding.3*

%changelog
%autochangelog
