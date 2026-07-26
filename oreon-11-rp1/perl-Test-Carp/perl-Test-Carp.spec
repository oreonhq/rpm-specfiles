%global source0_hash 8d0ea8edebc81b3ba4128ad8ef2238b76a1993db5d434758ceaec336b7ae743c

Name:           perl-Test-Carp
Version:        0.2
Release:        36%{?dist}
Summary:        Test your code for calls to Carp functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Carp
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Carp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::More)

%description
Call given code (with given arguments) and tests whether the given
Carp function (or their imported versions) are called (with a given
value) or not.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Carp-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

perldoc -t perlgpl > COPYING
perldoc -t perlartistic > Artistic

%check
./Build test

%files
%doc Changes README COPYING Artistic
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
