%global source0_hash 8db966a913dac4e464230702aa222bf38afe212193e636bc0f3cc651badeccee
Name:           perl-IO-Handle-Util
Summary:        Utilities for working with IO::Handle-like objects
Version:        0.02
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/IO-Handle-Util-%{version}.tar.gz
URL:            https://metacpan.org/release/IO-Handle-Util
BuildArch:      noarch
Requires:       perl(IO::String)
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(asa)
BuildRequires:  perl(autodie)
BuildRequires:  perl(ok)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides a number of helpful routines to manipulate or
create IO::Handle like objects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Handle-Util-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir="%{buildroot}" --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
