%global source0_hash 236cc65941406b964e616be093a3e74d74287dc843fdd70bc562d55a8ade3b09

Name:           perl-Text-ExtractWords
Summary:        Perl extension to extract words from strings
Version:        0.08
Release:        43%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-ExtractWords
Source0:        https://cpan.metacpan.org/authors/id/H/HD/HDIAS/Text-ExtractWords-%{version}.tar.gz

BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(AutoLoader)  
BuildRequires:  perl(DynaLoader)  
BuildRequires:  perl(Exporter)  
BuildRequires:  perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

%description
Extract words from texts or emails, for example to identify spam.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-ExtractWords-%{version}

# Remove executable bit on examples
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorarch}/auto/Text
%{perl_vendorarch}/Text
%{_mandir}/man3/Text::ExtractWords.3pm*

%changelog
%autochangelog
