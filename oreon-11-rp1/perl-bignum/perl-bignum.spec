# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1c9a824ab323e3e58d9808011c10ad27589dba1202806278215012ca7f522875
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: perl-bignum
Version: 0.67
Release: 1%{?dist}
Summary: Transparent big number support for Perl
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/bignum
Source0: https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/bignum-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: perl-interpreter
BuildRequires: perl(Math::BigInt)
BuildRequires: perl(Math::BigFloat)
BuildRequires: perl(Math::BigRat)
Requires: perl-interpreter
Requires: perl(Math::BigInt)
Requires: perl(Math::BigFloat)
Requires: perl(Math::BigRat)
Provides: perl(bigint) = %{version}
Provides: perl(bignum) = %{version}
Provides: perl(bigrat) = %{version}
Provides: perl(bigfloat) = %{version}

%description
Perl pragmas that turn numeric literals into big numbers.

%prep
%oreon_sha256
%autosetup -n bignum-%{version}

%build

%install
mkdir -p %{buildroot}%{perl_vendorlib}/Math/BigInt %{buildroot}%{perl_vendorlib}/Math/BigFloat %{buildroot}%{perl_vendorlib}/Math/BigRat
install -p -m 0644 lib/bigint.pm lib/bignum.pm lib/bigrat.pm lib/bigfloat.pm %{buildroot}%{perl_vendorlib}/
install -p -m 0644 lib/Math/BigInt/Trace.pm %{buildroot}%{perl_vendorlib}/Math/BigInt/
install -p -m 0644 lib/Math/BigFloat/Trace.pm %{buildroot}%{perl_vendorlib}/Math/BigFloat/
install -p -m 0644 lib/Math/BigRat/Trace.pm %{buildroot}%{perl_vendorlib}/Math/BigRat/

%check
perl -I%{buildroot}%{perl_vendorlib} -Ilib -Mbigint -e 'print 2**100, "\n"'

%files
%license LICENSE
%{perl_vendorlib}/bigint.pm
%{perl_vendorlib}/bignum.pm
%{perl_vendorlib}/bigrat.pm
%{perl_vendorlib}/bigfloat.pm
%{perl_vendorlib}/Math/BigInt/Trace.pm
%{perl_vendorlib}/Math/BigFloat/Trace.pm
%{perl_vendorlib}/Math/BigRat/Trace.pm
