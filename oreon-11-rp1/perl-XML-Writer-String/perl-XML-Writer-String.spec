%global source0_hash 31901cc85c6f771d34cb9814587296d99461f14eedebb4ed83b8b17b2b6d0ba6
Name:           perl-XML-Writer-String
Version:        0.1
Release:        37%{?dist}
Summary:        Capture output from XML::Writer module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Writer-String
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SOLIVER/XML-Writer-String-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(XML::Writer)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module implements a bare-bones class specifically for the purpose
of capturing data from the XML::Writer module.  XML::Writer expects an
IO::Handle object and writes XML data to the specified object (or STDOUT)
via its print() method.  This module simulates such an object for the
specific purpose of providing the required print() method.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Writer-String-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
sed -i 's/\r$//' String.pm README Changes example/*
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
