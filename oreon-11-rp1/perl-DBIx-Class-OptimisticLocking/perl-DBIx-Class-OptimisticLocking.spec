%global source0_hash 3c0243153189f4db1ccc4af4fd0531ffa9bf8df378addb28da9a55c83d2f41d4

Name:           perl-DBIx-Class-OptimisticLocking
Version:        0.02
Release:        31%{?dist}
Summary:        Optimistic locking support for DBIx::Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Class-OptimisticLocking
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPHILLIPS/DBIx-Class-OptimisticLocking-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Optimistic locking is an alternative to using exclusive locks when you have
the possibility of concurrent, conflicting updates in your database.
 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-OptimisticLocking-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes README
# incorrect fsf address reported upstream
# https://rt.cpan.org/Ticket/Display.html?id=106640
%license LICENSE
%{perl_vendorlib}/DBIx*
%{_mandir}/man3/DBIx*

%changelog
%autochangelog
