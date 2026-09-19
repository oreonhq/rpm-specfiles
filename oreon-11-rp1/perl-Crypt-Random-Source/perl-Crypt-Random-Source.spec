%global source0_hash ec4ece269f9ad1958c6e298ecee2e5a4345e357f3a4ffb2c748116af876eede6

Name:           perl-Crypt-Random-Source
Version:        0.14
Release:        24%{?dist}
Summary:        Get weak or strong random data from pluggable sources
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Crypt-Random-Source
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Crypt-Random-Source-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
# runtime requirements
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module provides implementations for a number of byte oriented sources
of random data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Random-Source-%{version}

%build
/usr/bin/perl Build.PL --installdirs vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENCE 
%doc Changes README
%{perl_vendorlib}/Crypt*
%{_mandir}/man3/Crypt*

%changelog
%autochangelog
