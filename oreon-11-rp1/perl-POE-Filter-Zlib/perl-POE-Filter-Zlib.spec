%global source0_hash 96973c90465842905825da6448ccb2697906e40d4d3d0f80ebf4e29864cbb37f

Name:           perl-POE-Filter-Zlib
Version:        2.04
Release:        27%{?dist}
Summary:        POE filter wrapped around Compress::Zlib
# note license definition in Makefile.PL
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Filter-Zlib
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Filter-Zlib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib) >= 2
# POE::Filter version from POE in META data
BuildRequires:  perl(POE::Filter) >= 0.38
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Compress::Zlib) >= 1.34
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stackable)
BuildRequires:  perl(Test::More) >= 0.47
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       perl(Compress::Raw::Zlib) >= 2
# POE::Filter version from POE in META data
Requires:       perl(POE::Filter) >= 0.38

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Compress::Raw::Zlib|POE::Filter)\\)$

%description
POE::Filter::Zlib provides a POE filter for performing compression and
uncompression using Compress::Zlib. It is suitable for use with
POE::Filter::Stackable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Filter-Zlib-%{version}
for F in Changes.old; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes* README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
