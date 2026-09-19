%global source0_hash e63e81c52eb1e0e60ec2d983f5552d2493e117179925c96757f23c4bd9fa713a

Name:           perl-IO-Interface
Version:        1.09
Release:        37%{?dist}
Summary:        Perl extension for accessing network card configuration information
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Interface
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Interface-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorarch}/IO/
%{perl_vendorarch}/auto/IO/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
