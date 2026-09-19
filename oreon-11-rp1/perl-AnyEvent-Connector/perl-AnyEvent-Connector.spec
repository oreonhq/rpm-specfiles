%global source0_hash a8c4a96ca72f400b5c241b0e61cae02b4a7490eded8ef737f16f1cb7ac931d44

Name:           perl-AnyEvent-Connector
Version:        0.04
Release:        8%{?dist}
Summary:        AnyEvent TCP connect with transparent proxy handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-Connector
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/AnyEvent-Connector-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.006
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Module::Build::Prereqs::FromCPANfile) >= 0.02
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
AnyEvent::Connector object has tcp_connect method compatible with that from
AnyEvent::Socket, and it handles proxy settings transparently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-Connector-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/AnyEvent
%{_mandir}/man3/AnyEvent::Connector*

%changelog
%autochangelog
