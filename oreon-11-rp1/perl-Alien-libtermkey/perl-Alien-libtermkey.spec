%global source0_hash fbc812abac8aaf4a57a70668dac0bcd45fc7a0377ef1b2a8470957f7986a7490
Name:           perl-Alien-libtermkey
Version:        0.22
Release:        1%{?dist}
Summary:        Alien wrapping for libtermkey
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-libtermkey
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Alien-libtermkey-%{version}.tar.gz
%global debug_package %{nil}
Requires:       perl(ExtUtils::CChecker)
Requires:       libtermkey-devel(%{__isa}) = %(type -p pkgconf >/dev/null && pkgconf --exists termkey && pkgconf --modversion termkey|| echo 0)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(termkey)
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
