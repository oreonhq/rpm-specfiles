%global source0_hash 0b2ba7de2cd7ddd5fe102a2e2ae7aeba21eaab1078bf3bfd3c5a722937256380

Name:           perl-Net-AMQP
Version:        0.06
Release:        20%{?dist}
Summary:        Advanced Message Queue Protocol (de)serialization and representation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Net-AMQP
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHIPS/Net-AMQP-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88

%{?perl_default_filter}

%description
This module implements the frame (de)serialization and representation of
the Advanced Message Queue Protocol (http://www.amqp.org/). It is to be
used in conjunction with client or server software that does the actual
TCP/IP communication.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-AMQP-%{version}

%build
%{__perl} Build.PL installdirs=vendor
%{__perl} -pi -e 's/\r//' spec/amqp0-9*.xml
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc CHANGES eg README spec
%license LICENSE
%{perl_vendorlib}/Net*
%{_mandir}/man3/Net*

%changelog
%autochangelog
