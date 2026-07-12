%global source0_hash 70751531ba78d768d6f4f77a32b1ea2d1959e76e37b6f89e5ce6930c06c60bf6

Name:           perl-autobox
Version:        3.0.2
Release:        5%{?dist}
Summary:        Call methods on native types
License:        Artistic-2.0
URL:            https://metacpan.org/release/autobox
Source0:        https://cpan.metacpan.org/modules/by-module/autobox/autobox-v%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard) >= 0.21
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl-debugger
BuildRequires:  perl(blib)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::System::Simple) >= 1.30
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal) >= 0.017
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional Tests:
BuildRequires:  perl(Test::Pod) >= 1.00
# Dependencies:
Requires:       perl(Scope::Guard) >= 0.21

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Scope::Guard\\)$

Provides:       perl(autobox)
Provides:       perl(autobox)
%description
The autobox pragma allows methods to be called on integers, floats,
strings, arrays, hashes, and code references in exactly the same manner as
blessed references.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n autobox-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE.md
%doc Changes README
%{perl_vendorarch}/auto/autobox/
%{perl_vendorarch}/autobox/
%{perl_vendorarch}/autobox.pm
%doc %{perl_vendorarch}/autobox.pod
%{_mandir}/man3/autobox.3*

%changelog
%autochangelog
