%global source0_hash 416695e5bdcffd74eab79aedb17877abefd068a6a549389baccbebb919bdfb7e

Name:           perl-Parse-CPAN-Distributions
Version:        0.14
Release:        32%{?dist}
Summary:        Provides an index for current CPAN distributions
License:        Artistic-2.0
URL:            https://metacpan.org/release/Parse-CPAN-Distributions
Source0:        https://cpan.metacpan.org/authors/id/B/BA/BARBIE/Parse-CPAN-Distributions-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  glibc-common
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests:
# Test::CPAN::Meta not used
# Test::CPAN::Meta::JSON not used
BuildRequires:  perl(Test::More) >= 0.70
# Test::Pod 1.0 not used
# Test::Pod::Coverage 0.08 not used

%description
This Perl module provides the ability to index the distributions that are
currently listed on CPAN. This is done by parsing the index file find-ls.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-CPAN-Distributions-%{version}
# Normalize encoding
iconv -f ISO-8859-1 -t UTF-8 <LICENSE >LICENSE.utf8
touch -r LICENSE LICENSE.utf8
mv LICENSE.utf8 LICENSE

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
