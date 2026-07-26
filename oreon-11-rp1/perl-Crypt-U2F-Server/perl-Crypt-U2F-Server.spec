%global source0_hash 41a46e302ed41867e3be4830bf843a438d005606dd55ac703db331bd98965ce9

Name:           perl-Crypt-U2F-Server
Version:        0.47
Release:        5%{?dist}
Summary:        Low level wrapper around the U2F C library (server side)
License:        BSD-2-Clause AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/Crypt-U2F-Server
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIMARD/Crypt-U2F-Server-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libu2f-server-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.18.1
BuildRequires:  perl(Authen::U2F::Tester) >= 0.02
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

%description
This is a very low level wrapper around the original C library. You
probably shouldn't use it, but use Crypt::U2F::Server::Simple instead!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-U2F-Server-%{version}

%build
perl Makefile.PL \
  INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::U2F::Server*3pm*

%changelog
%autochangelog
