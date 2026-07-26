%global source0_hash cdf4e37d8f7fc3b44d4bdbe86fd35d5cb331ca6ff44d26e00a1d97e0f46ffc60

Name:           perl-PPI-XS
Version:        0.910
Release:        29%{?dist}
Summary:        XS acceleration for PPI
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI-XS
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/PPI-XS-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(PPI) >= 1.000
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful

%{?perl_default_filter}

%description
PPI::XS provides XS-based acceleration of the core PPI packages. It
selectively replaces a (small but growing) number of methods throughout PPI
with identical but much faster C versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PPI-XS-%{version}
# Fix OELs
for F in Changes; do
    tr -d "\r" < "$F" > "${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PPI*
%{_mandir}/man3/*

%changelog
%autochangelog
