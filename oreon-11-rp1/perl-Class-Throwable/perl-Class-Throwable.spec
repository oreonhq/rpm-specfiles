%global source0_hash dc9a11e0dab56dc220dea8c94fe3c47db5e7dd7c1ed04dc8178aa5bb7bfbbcce

%global pkgname Class-Throwable

Name:           perl-Class-Throwable
Version:        0.13
Release:        30%{?dist}
Summary:        A minimal lightweight exception class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Throwable
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMX/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.1
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Scalar::Util) >= 1.1

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Scalar::Util\\)$

%description
This module implements a minimal lightweight exception object. It is
meant to be a compromise between more basic solutions like Carp which
can only print information and cannot handle exception objects, and more
complex solutions like Exception::Class which can be used to define
complex inline exceptions and has a number of module dependencies. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}
# Correct permissons
find -type f -exec chmod 0644 {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README t/
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Throwable.3pm*

%changelog
%autochangelog
