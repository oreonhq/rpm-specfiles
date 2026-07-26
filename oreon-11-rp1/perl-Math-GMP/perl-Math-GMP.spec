%global source0_hash 382b71e54762f639e9a42a9b06934151987ba57d11bb70d35e3bec88d50450ce

Summary:	High speed arbitrary size integer math
Name:		perl-Math-GMP
Version:	2.25
Release:	15%{?dist}
License:	LGPL-2.0-or-later
URL:		https://metacpan.org/release/Math-GMP
Source0:	https://www.cpan.org/modules/by-module/Math/Math-GMP-%{version}.tar.gz
Patch0:		Math-GMP-2.18-no-Alien::GMP.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gmp-devel
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.10.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(Config)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
Math::GMP was designed to be a drop-in replacement both for Math::BigInt and
for regular integer arithmetic. Unlike BigInt, though, Math::GMP uses the GNU
gmp library for all of its calculations, as opposed to straight Perl functions.
This can result in speed improvements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-GMP-%{version}

# Avoid need for Alien::GMP; our build environment doesn't need it
%patch -P 0

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING.LIB LICENSE
%doc Changes README.md
%{perl_vendorarch}/Math/
%{perl_vendorarch}/auto/Math/
%{_mandir}/man3/Math::GMP.3*

%changelog
%autochangelog
