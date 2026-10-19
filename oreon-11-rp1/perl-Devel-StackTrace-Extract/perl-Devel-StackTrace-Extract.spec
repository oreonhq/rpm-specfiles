%global source0_hash 6366c3acd448291699a51aacba9145440e1070a0a5281ad50a9754ead1a3ddc2
Name:           perl-Devel-StackTrace-Extract
Version:        1.000000
Release:        1%{?dist}
Summary:        Extract a stack trace from an exception object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-StackTrace-Extract
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Devel-StackTrace-Extract-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::StackTrace::Frame)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Mojo::Exception)
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Throwable::Error)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
It's popular to store stack traces in objects that are thrown as
exceptions, but, this being Perl, there's more than one way to do it. This
module provides a simple interface to attempt to extract the stack trace
from various well known exception classes that are on the CPAN.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-StackTrace-Extract-%{version}

%build

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
