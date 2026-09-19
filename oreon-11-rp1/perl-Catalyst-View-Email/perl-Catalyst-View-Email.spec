%global source0_hash 837211a96098cec16698ff09b135b8e30d2664db2e1b1dd205f5a07d13a8bd3c

Name:           perl-Catalyst-View-Email
Version:        0.36
Release:        30%{?dist}
Summary:        Send Email from Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-View-Email
Source0:        https://cpan.metacpan.org/authors/id/D/DH/DHOSS/Catalyst-View-Email-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst) >= 5.7
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::View)
BuildRequires:  perl(Catalyst::View::Mason) >= 0.18
BuildRequires:  perl(Catalyst::View::TT) >= 0.31
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(Email::MIME) >= 1.859
BuildRequires:  perl(Email::MIME::Creator) >= 1.455
BuildRequires:  perl(Email::Sender::Simple) => 0.100110
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(parent) >= 0.223
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# not automatically detected
Requires:       perl(Catalyst) >= 5.7
Requires:       perl(Email::MIME) >= 1.859
# could be Recommends or Suggests?
#Requires:       perl(Catalyst::View::TT) >= 0.31
#Requires:       perl(Catalyst::View::Mason) >= 0.18

%{?perl_default_filter}

%description
This module sends out emails from a stash key specified in the configuration
settings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-View-Email-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=yep make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
