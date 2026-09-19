%global source0_hash 51dac4a778b3cbf2e855a8a7ef0021b9d163cf8053726b27823e537349b96444

%global tarname WWW-OrangeHRM-Client
Name:           perl-%{tarname}
Version:        0.12.0
Release:        19%{?dist}
Summary:        Client for OrangeHRM
License:        GPL-1.0-or-later
URL:            http://ppisar.fedorapeople.org/%{tarname}/
Source0:        %{url}%{tarname}-v%{version}.tar.gz
Source1:        %{url}%{tarname}-v%{version}.tar.gz.asc
# Exported from owner's keyring
Source2:        gpgkey-4B528393E6A3B0DFB2EF3A6412C9C5C767C6FAA2.gpg
BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
# Run-time:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::TreeBuilder::LibXML)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl(WWW::Mechanize)
# Tests:
BuildRequires:  perl(Test::More)
Recommends:     perl(LWP::Authen::Negotiate)
Requires:       perl(LWP::Protocol::https)

%description
This module implements client for OrangeHRM information system. It has been
developed against Red Hat instance, so I cannot guarantee it works with
other instances.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{tarname}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
