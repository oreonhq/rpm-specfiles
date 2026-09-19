%global source0_hash e721cdfda183146b895e04cee712e10ab1bc73c8bad1bbc84c04b19ef1052c98

Name:           perl-Time-timegm
Version:        0.01
Release:        39%{?dist}
Summary:        UTC version of mktime()
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-timegm
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Time-timegm-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(XSLoader)

%description
The POSIX standard provides three functions for converting between integer
epoch values and 6-component "broken-down" time representations. localtime
and gmtime convert an epoch into the 6 components of seconds, minutes,
hours, day of month, month and year, in either local timezone or UTC. The
mktime function converts a local broken-down time into an epoch value.
However, POSIX does not provide a UTC version of this.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Time-timegm-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete -print
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Time*
%{_mandir}/man3/*

%changelog
%autochangelog
