%global source0_hash dae1195a2ccb52beb3b89962dd03425f7d188f2481eeacf85f3f7a99404eb7a0

Name:           perl-WWW-GoodData
Version:        1.11
Release:        34%{?dist}
Summary:        Client library for GoodData REST-ful API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-GoodData
Source0:        https://cpan.metacpan.org/authors/id/L/LK/LKUNDRAK/WWW-GoodData-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Pod)
Requires:       perl(IO::Socket::SSL)

%description
WWW::GoodData is the client for GoodData JSON-based API built atop
WWW::GoodData::Agent client agent, with focus on usefulness and
correctness of implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-GoodData-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc ISSUES
%{perl_vendorlib}/*
%{_bindir}/gdc
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
%autochangelog
