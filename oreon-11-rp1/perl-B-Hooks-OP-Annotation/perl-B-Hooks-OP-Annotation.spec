%global source0_hash 6e26f99367f4ea944169cf6e05cf4d067832082424ca8ecefccb7b5a63217b16

Name:           perl-B-Hooks-OP-Annotation
Version:        0.44
Release:        45%{?dist}
Summary:        Annotate and delegate hooked OPs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Hooks-OP-Annotation
Source0:        https://cpan.metacpan.org/modules/by-module/B/B-Hooks-OP-Annotation-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
# Dependencies
# (none)

# Avoid provides from perl shared objects
%{?perl_default_filter}

%description
This module provides a way for XS code that hijacks OP op_ppaddr functions
to delegate to (or restore) the previous functions, whether assigned by
perl or by another module. Typically this should be used in conjunction
with B::Hooks::OP::Check.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Hooks-OP-Annotation-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/B/
%{perl_vendorarch}/B/
%{_mandir}/man3/B::Hooks::OP::Annotation.3*

%changelog
%autochangelog
