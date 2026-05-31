%global source0_hash 8fd2126d3beec554df852919f4739e689202cbba6a17506e9b66ea165841a75c

Name:           perl-XML-Filter-BufferText
Version:        1.01
Release:        52%{?dist}
Summary:        Filter to put all characters() in one event
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Filter-BufferText
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-Filter-BufferText-%{version}.tar.gz



BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::SAX::Base)


%description
This is a very simple filter. One common cause of grief (and programmer
error) is that XML parsers aren't required to provide character events in
one chunk. They can, but are not forced to, and most don't. This filter
does the trivial but oft-repeated task of putting all characters into a
single event.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-Filter-BufferText-%{version}
chmod 644 Changes README BufferText.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.01-52
- Prepare for Oreon 11 (RP1)
