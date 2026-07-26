%global source0_hash c4a21dc1ca8a35a612415eb8027d9407142f2b27b5fa9e67917a88f388947726

Name:           perl-Net-IDN-Nameprep
Summary:        Stringprep Profile for Internationalized Domain Names (RFC 3491)
Version:        1.102
Release:        32%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IDN-Nameprep
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Nameprep-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Unicode::Stringprep) >= 1.1
BuildRequires:  perl(Unicode::Stringprep::Mapping)
BuildRequires:  perl(Unicode::Stringprep::Prohibited)

%{?perl_default_filter}

%description
This module implements the nameprep specification, which describes how to
prepare internationalized domain name (IDN) labels in order to increase the
likelihood that name input and name comparison work in ways that make sense
for typical users throughout the world. Nameprep is a profile of the
stringprep protocol and is used as part of a suite of on-the-wire protocols
for internationalizing the Domain Name System (DNS).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IDN-Nameprep-%{version}

# Remove incorrect executable bits
chmod -x Changes \
         lib/Net/IDN/Nameprep.pm

# Convert files to UTF-8
for FILE in LICENSE README; do
  iconv -f ISO_8859-1 -t UTF8 $FILE > $FILE.utf8
  mv $FILE.utf8 $FILE
done

# Drop non-free file
# See comments 7 and 9 of the review request:
#     https://bugzilla.redhat.com/show_bug.cgi?id=891873
rm -f t/nameprep_vec.t

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Net
%{_mandir}/man3/Net::IDN::Nameprep.3pm*

%changelog
%autochangelog
