%global source0_hash 9cf0f711007ef06bb7b18dbe45368249f6c0f67c40663877f7675815e0bf4801
Name:           perl-HTTP-Easy
Version:        0.04
Release:        1%{?dist}
Summary:        HTTP helpers for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/Mons/HTTP-Easy
Source0:        https://github.com/Mons/HTTP-Easy/archive/refs/tags/%{version}/HTTP-Easy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(lib::abs)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Set of useful helpers for HTTP work with Perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Easy-%{version}

%build

unset AUTHOR
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
