%global source0_hash 5e05770a09a52c7d3d9139e10a93757133f099b863d0823c8e4a021df7ffa502

Name:           perl-Exception-Class-TryCatch
Version:        1.13
Release:        34%{?dist}
Summary:        Syntactic try/catch sugar for use with Exception::Class
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Exception-Class-TryCatch
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Exception-Class-TryCatch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Exception::Class) >= 1.2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.47

%{?perl_default_filter}

%description
Exception::Class::TryCatch provides syntactic sugar for use with
Exception::Class using the familiar keywords try and catch. Its primary
objective is to allow users to avoid dealing directly with $@ by ensuring
that any exceptions caught in an eval are captured as Exception::Class
objects, whether they were thrown objects to begin with or whether the
error resulted from die. This means that users may immediately use isa and
various Exception::Class methods to process the exception.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Exception-Class-TryCatch-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
