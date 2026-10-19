%global source0_hash 8d0ea8edebc81b3ba4128ad8ef2238b76a1993db5d434758ceaec336b7ae743c
Name:           perl-Test-Carp
Version:        0.2
Release:        1%{?dist}
Summary:        Test your code for calls to Carp functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Carp
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Carp-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::More)
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
