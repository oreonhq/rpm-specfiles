%global source0_hash 342d2dcfc797a20bee8179b1b96b85c0ae7a5b48827359523cd8c74c3e704502

Name:           perl-Class-ErrorHandler
Version:        0.04
Release:        31%{?dist}
Summary:        Class::ErrorHandler Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-ErrorHandler
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Class-ErrorHandler-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Test)

%description
This is Class::ErrorHandler, a base class for classes that need to do
error handling (which is, probably, most of them).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-ErrorHandler-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
