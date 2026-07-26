%global source0_hash 09cec07d9f436a205e31ff21a4b8b9e9c5847810b38b833d3c96d0cbb1d57249

Name:           perl-Scalar-Util-LooksLikeNumber
Version:        1.39.2
Release:        34%{?dist}
Summary:        Access to looks_like_number() perl API function
# Defined in Makefile.PL, also mentioned in LooksLikeNumber.xs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scalar-Util-LooksLikeNumber
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Scalar-Util-LooksLikeNumber-%{version}.tar.gz
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Exporter)
# Tests only
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)

%description
Scalar::Util::LooksLikeNumber contains looks_like_number() like
Scalar::Util's looks_like_number(), except it returns the raw value from
the C function. Scalar::Util used to do this also, but it returns a
booleanized value since 1.39.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Scalar-Util-LooksLikeNumber-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Scalar*
%{_mandir}/man3/*

%changelog
%autochangelog
