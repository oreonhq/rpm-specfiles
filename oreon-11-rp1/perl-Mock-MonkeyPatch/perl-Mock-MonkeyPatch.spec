%global source0_hash acc586530cb62e814166cacfb792b8977b6c3d56c77b169e6ab1c30d48e1d585

Name:           perl-Mock-MonkeyPatch
Version:        1.03
Release:        4%{?dist}
Summary:        Monkey patching with test mocking in mind
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Mock-MonkeyPatch
Source0:        https://cpan.metacpan.org/authors/id/J/JB/JBERGER/Mock-MonkeyPatch-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(:VERSION) >= 5.6
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More) >= 0.96

%description
Mock::MonkeyPatch injects a subroutine in the place of an existing one.
It returns an object by which you can revisit the manner in which the
mocked subroutine was called. Further when the object goes out of
scope (or when the "restore" method is called) the original subroutine
is replaced.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mock-MonkeyPatch-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Mock*
%{_mandir}/man3/Mock*

%changelog
%autochangelog
