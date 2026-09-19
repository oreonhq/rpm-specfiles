%global source0_hash fbc812abac8aaf4a57a70668dac0bcd45fc7a0377ef1b2a8470957f7986a7490

Name:           perl-Alien-libtermkey
Version:        0.22
Release:        6%{?dist}
Summary:        Alien wrapping for libtermkey
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Alien-libtermkey
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Alien-libtermkey-%{version}.tar.gz

# This is a full-arch package because it requires an arch-specific
# libtermkey.so library but it does not install any ELF, therefore
# disable debuginfo generation.
%global debug_package %{nil}

# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(termkey)
# runtime requirements
BuildRequires:  perl(ExtUtils::CChecker)
Requires:       perl(ExtUtils::CChecker)
# This RPM package ensures libtermkey.so is installed on the system
Requires:       libtermkey-devel(%{__isa}) = %(type -p pkgconf >/dev/null && pkgconf --exists termkey && pkgconf --modversion termkey|| echo 0)

%description
This CPAN distribution wraps the C library libtermkey in a wrapper suitable
to drive CPAN and other Perl-related build infrastructure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-libtermkey-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Alien*
%{_mandir}/man3/Alien*

%changelog
%autochangelog
