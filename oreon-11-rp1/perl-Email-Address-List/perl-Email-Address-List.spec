%global source0_hash 305b94c778011cee70d9f21514d92e985fa9dccbb84c64798f0c1f0b24eb870e

Name:           perl-Email-Address-List
Version:        0.06
Release:        22%{?dist}
Summary:        RFC close address list parsing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Address-List
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/Email-Address-List-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(autodie)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)

%description
Parser for From, To, Cc, Bcc, Reply-To, Sender and previous prefixed with
Resent- (e.g. Resent-From) headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Address-List-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
