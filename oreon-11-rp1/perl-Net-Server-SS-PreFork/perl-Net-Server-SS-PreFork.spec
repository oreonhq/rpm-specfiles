%global source0_hash 6d22b3a84eb3e01fb238f566bdb3014847d30e0d51ec1e86a0b6e043e367968b

Name:           perl-Net-Server-SS-PreFork
Version:        0.05
Release:        44%{?dist}
Summary:        Hot-deployable variant of Net::Server::PreFork
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Net-Server-SS-PreFork
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Net-Server-SS-PreFork-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Net::Server::PreFork)
BuildRequires:  perl(Net::Server::Proto::TCP)
BuildRequires:  perl(Server::Starter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP) >= 0.06

%{?perl_default_filter}

%description
Net::Server::SS::PreFork is a Net::Server personality, extending
Net::Server::PreFork. It can be run by the start_server script of
Server::Starter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Server-SS-PreFork-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/man3/Net*

%changelog
%autochangelog
