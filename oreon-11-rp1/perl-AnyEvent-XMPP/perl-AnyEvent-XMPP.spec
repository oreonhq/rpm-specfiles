%global source0_hash ec56b25e6a78630f79ee5e38b79a39957b8b89fb1ea03804f54defb9e3544256

Name:           perl-AnyEvent-XMPP
Version:        0.55
Release:        33%{?dist}
Summary:        Implementation of the XMPP Protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-XMPP
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTPLBG/AnyEvent-XMPP-%{version}.tar.gz
Patch0:         AnyEvent-XMPP-0.51-timezone.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::LibIDN)
BuildRequires:  perl(Object::Event)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser::Expat)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XML::Writer)
# Add Net::SSLeay to prevent issues like RT#80148
Requires:       perl(Net::SSLeay) >= 1.33

%{?perl_default_filter}

%description
AnyEvent::XMPP - An implementation of the XMPP Protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-XMPP-%{version}
%patch -P0 -p1 -b .timezone
for file in samples/*; do
    sed -i 's/#!.*perl/\/usr\/bin\/perl/' ${file}
    chmod a-x ${file}
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes CONTRIBUTORS README TODO samples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
