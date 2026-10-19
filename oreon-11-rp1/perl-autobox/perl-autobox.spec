%global source0_hash 70751531ba78d768d6f4f77a32b1ea2d1959e76e37b6f89e5ce6930c06c60bf6
Name:           perl-autobox
Version:        3.0.2
Release:        5%{?dist}
Summary:        Call methods on native types
License:        Artistic-2.0
URL:            https://metacpan.org/release/autobox
Source0:        https://cpan.metacpan.org/modules/by-module/autobox/autobox-v%{version}.tar.gz
Requires:       perl(Scope::Guard) >= 0.21
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Scope::Guard\\)$
Provides:       perl(autobox)
Provides:       perl(autobox)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-debugger
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
