%global source0_hash 1e4621e6fa0931231fbcb211a140b54fc30e64cc453644605d830237364d4d33
Name:           perl-Set-Tiny
Version:        0.06
Release:        5%{?dist}
Summary:        Simple sets of strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Set-Tiny
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Set-Tiny-%{version}.tar.gz
BuildArch:      noarch
%if "%{version}" == "0.06"
%endif
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
# /oreon:deps
%description
Set::Tiny is a thin wrapper around regular Perl hashes to perform often
needed set operations, such as testing two sets of strings for equality, or
checking whether one is contained within the other.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Set-Tiny-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
