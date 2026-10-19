%global source0_hash a274c56ea73ffe2a06a6448f052c54c3fd1e07b51f8c31cd2af2829644c995a4
Name:           perl-AnyEvent-DBus
Version:        0.31
Release:        1%{?dist}
Summary:        Adapt Net::DBus to AnyEvent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-DBus
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-DBus-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::DBus)
BuildRequires:  perl(Net::DBus::Binding::Watch)
BuildRequires:  perl(common::sense)
BuildRequires:  perl-generators
# /oreon:deps
%description
Loading this module will install the necessary magic to seamlessly integrate
Net::DBus into AnyEvent.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-DBus-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
