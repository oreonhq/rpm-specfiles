%global source0_hash f3d1fcf95b361157693198bb452c08f2dc27f61ab65b5a2d4f226abf7f1b2347

Name:           perl-Date-JD
Version:        0.006
Release:        24%{?dist}
Summary:        Conversion between flavors of Julian Date
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-JD
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-JD-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.006
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)
Requires:       perl(POSIX)

%{?perl_default_filter}

%description
For date and time calculations it is convenient to represent dates by a
simple linear count of days, rather than in a particular calendar. This is
such a good idea that it has been invented several times. If there were a
single such linear count then it would be the obvious data interchange
format between calendar modules. With several versions, calendar modules
can use such sensible data formats and still have interoperability
problems. This module tackles that problem, by performing conversions
between different flavors of day count. These day count systems are
generically known as "Julian Dates", after the most venerable of them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-JD-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
