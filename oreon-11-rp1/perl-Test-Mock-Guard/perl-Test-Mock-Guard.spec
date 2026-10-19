%global source0_hash 7f228a63f8d6ceb92aa784080a13e85073121b2835eca06d794f9709950dbd3d
Name:           perl-Test-Mock-Guard
Version:        0.10
Release:        1%{?dist}
Summary:        Simple mock test library using RAII
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Mock-Guard
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAICRON/Test-Mock-Guard-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Exporter) >= 5.63
# oreon:deps
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Mock::Guard is mock test library using RAII. This module is able to
change method behavior by each scope. See SYNOPSIS's sample code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Mock-Guard-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
