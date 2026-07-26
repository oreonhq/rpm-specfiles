%global source0_hash e4d39537db35d75eb88032d2d26a707733fe33b6baeb212f9c733fc4bff07e43

Name:           perl-Text-ASCIITable
Version:        0.22
Release:        29%{?dist}
Summary:        Create a nice formatted table using ASCII characters
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-ASCIITable
Source0:        https://cpan.metacpan.org/authors/id/L/LU/LUNATIC/Text-ASCIITable-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build) >= 0.27

%description
Pretty nifty if you want to output dynamic text to your console or other
fixed-size-font displays, and at the same time it will display it in a nice
human-readable, or "cool" way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-ASCIITable-%{version}
for i in ansi-example.pl lib/Text/ASCIITable/Wrap.pm t/*; do
    iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i
done

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README ansi-example.pl
%{perl_vendorlib}/Text*
%{_mandir}/man3/Text*

%changelog
%autochangelog
