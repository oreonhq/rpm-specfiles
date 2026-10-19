%global source0_hash 084fa3ad14a06b979c19d13d4644e2cd99370aaa920a44499ba356af23793659
Name:           perl-Class-Can
Version:        0.01
Release:        46%{?dist}
Summary:        Inspect a class/method and say what it can do (and why)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Can
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Can-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Class::Can interrogates the object heirarchy of a package to return a hash
detailling what methods the class could dispatch (as the key), and the
package it found it in (as the value).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Can-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
