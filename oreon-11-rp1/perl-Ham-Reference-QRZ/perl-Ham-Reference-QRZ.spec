%global source0_hash 23a13e6ffb31daaa90047bb4ab8d6062c05464dfffc39319ad17f024ab921116
Name:               perl-Ham-Reference-QRZ
Version:            0.04
Release:        28%{?dist}
Summary:        An object oriented front end for the QRZ.COM Amateur Radio call-sign database
License:            Artistic-2.0
URL:                https://metacpan.org/release/Ham-Reference-QRZ
Source0:        https://cpan.metacpan.org/modules/by-module/Ham/BRADMC/Ham-Reference-QRZ-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
An object oriented front end for the QRZ.COM Amateur Radio call-sign database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Ham-Reference-QRZ-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
