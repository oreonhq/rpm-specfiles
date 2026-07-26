%global source0_hash 1e1a702b0dd390c3e629f8a9e84cca63b794d1e227957f429b6760107577fb86

Name:           perl-Net-Server-Coro
Version:        1.3
Release:        32%{?dist}

Summary:        Co-operative multithreaded server using Coro
License:        MIT
URL:            https://metacpan.org/release/Net-Server-Coro

Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Net-Server-Coro-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(inc::Module::Install)

# This one is not automatically caught by RPM
Requires:       perl(Net::SSLeay)

%description
Net::Server::Coro implements multithreaded server for the Net::Server
architecture, using Coro and Coro::Socket to make all reads and writes non-
blocking. Additionally, it supports non-blocking SSL negotiation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Server-Coro-%{version}

# Build using the system-provided module, not the bundled one
rm -fr inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%files
%doc Changes
%{_mandir}/man?/Net::Server::Coro*.gz
%{perl_vendorlib}/Net

%check
make test

%changelog
%autochangelog
