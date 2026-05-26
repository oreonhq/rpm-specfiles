Name:           perl-Class-Accessor
Version:        0.51
Release:        24%{?dist}
Summary:        Automated accessor generation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 bf12a3e5de5a2c6e8a447b364f4f5a050bf74624c56e315022ae7992ff2f411c
%global source0_file Class-Accessor-0.51.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
# Test Suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
# Dependencies
# (none)

%description
This module automagically generates accessors/mutators for your class.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Class-Accessor-0.51.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bf12a3e5de5a2c6e8a447b364f4f5a050bf74624c56e315022ae7992ff2f411c" || { echo "oreon: Source0 SHA256 mismatch for Class-Accessor-0.51.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Class-Accessor-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make  %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes examples/ README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Accessor.3*
%{_mandir}/man3/Class::Accessor::Fast.3*
%{_mandir}/man3/Class::Accessor::Faster.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.51-24
- Prepare for Oreon 11 (RP1)
