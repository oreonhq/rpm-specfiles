%global source0_hash 20b08432ac1aebaa2cf290e92344ae19073da6d87be464952a2a73f9718890f9

Name:           perl-Algorithm-FastPermute
Version:        0.999
Release:        56%{?dist}
Summary:        Rapid generation of permutations

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-FastPermute
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBIN/Algorithm-FastPermute-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Algorithm::FastPermute generates all the permutations of an array. You pass
a block of code, which will be executed for each permutation. The array
will be changed in place, and then changed back again before "permute"
returns. During the execution of the callback, the array is read-only and
you'll get an error if you try to change its length.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-FastPermute-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} %{?_smp_mflags}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README perms.pl
%dir %{perl_vendorarch}/Algorithm
%{perl_vendorarch}/Algorithm/FastPermute.pm
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*.3*
%exclude %{perl_vendorarch}/Algorithm/perms.pl

%changelog
%autochangelog
