%global source0_hash d57cbd8a39368cc2122e6a4e2fea5f3ddcf4ce7a9d3031c97274dbdd080ac761

# Filter unversioned module dependency
%global __requires_exclude ^perl\\(Scalar::Util\\)$

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Net-BGP

Summary:        Perl module for object-oriented API to the BGP protocol
Name:           perl-Net-BGP
Version:        0.18
Release:        12%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/S/SS/SSCHECK/%{pkgname}-%{version}.tar.gz
Requires:       perl(Scalar::Util) >= 1.01
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 0.95 
BuildArch:      noarch

%description
An implementation of the BGP-4 inter-domain routing protocol as Perl module.
It encapsulates all of the functionality needed to establish and maintain a
BGP peering session and exchange routing update information with the peer.
It aims to provide a simple API to the BGP protocol for the purposes of
automation, logging, monitoring, testing, and similar tasks using the power
and flexibility of Perl. The module does not implement the functionality of
a RIB (Routing Information Base) nor does it modify the kernel routing table
of the host system. However, such operations could be implemented using the
API provided by the module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

# Remove signature test (#1701810)
rm -f t/00-Signature.t

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
