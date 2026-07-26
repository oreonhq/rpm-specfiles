%global source0_hash efeed3ddb3a8ea18f416d485f3c2b0427145d267e63368c651d488eaa8c28d09

Name:           perl-MooseX-Has-Sugar
Version:        1.000006
Release:        27%{?dist}
Summary:        Sugar syntax for moose 'has' fields
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Has-Sugar
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/MooseX-Has-Sugar-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Moose "has" syntax is generally fine, but sometimes one gets bothered with
the constant typing of string quotes for things. The MooseX::Types module
exists and in many ways reduces the need for constant string creation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Has-Sugar-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
export RELEASE_TESTING=1
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
