Name:           perl-Class-Singleton
Version:        1.6
Release:        15%{?dist}
Summary:        Implementation of a "Singleton" class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Singleton
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/Class-Singleton-1.6.tar.gz
# oreon url source checksums begin
%global source0_sha256 27ba13f0d9512929166bbd8c9ef95d90d630fc80f0c9a1b7458891055e9282a4
%global source0_file Class-Singleton-1.6.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
# Module Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)

%description
This is the Class::Singleton module. A Singleton describes an object class
that can have only one instance in any system. An example of a Singleton
might be a print spooler or system registry. This module implements a
Singleton class from which other classes can be derived. By itself, the
Class::Singleton module does very little other than manage the
instantiation of a single object. In deriving a class from
Class::Singleton, your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Class-Singleton-1.6.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "27ba13f0d9512929166bbd8c9ef95d90d630fc80f0c9a1b7458891055e9282a4" || { echo "oreon: Source0 SHA256 mismatch for Class-Singleton-1.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Class-Singleton-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license Artistic Copying LICENCE
%doc Changes README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Singleton.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6-15
- Prepare for Oreon 11 (RP1)
