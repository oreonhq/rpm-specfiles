%global source0_hash eb3bcc6fdf3741d43a0c05d96794b00b3534e85ee1d6466d46785ec537daa4cf

Name:           perl-B-Generate
Version:        1.56
Release:        28%{?dist}
Summary:        Create your own op trees
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Generate
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Generate-%{version}.tar.gz
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(B::Concise)
BuildRequires:  perl(B::Terse)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
The B module allows you to examine the Perl op tree at run-time, in Perl
space; it's the basis of the Perl compiler. But what it doesn't let you do
is manipulate that op tree: it won't let you create new ops, or modify old
ones. Now you can.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Generate-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license Artistic Copying
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/B*
%{_mandir}/man3/*

%changelog
%autochangelog
