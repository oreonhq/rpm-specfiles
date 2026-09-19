%global source0_hash 1e4621e6fa0931231fbcb211a140b54fc30e64cc453644605d830237364d4d33

Name:           perl-Set-Tiny
Version:        0.06
Release:        5%{?dist}
Summary:        Simple sets of strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Set-Tiny
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Set-Tiny-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)

%if "%{version}" == "0.06"
# New in 0.06
# Why doesn't Dist::Zilla check for it?
BuildRequires:  perl(blib)
%endif

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

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
