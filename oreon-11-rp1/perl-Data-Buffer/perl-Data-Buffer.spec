%global source0_hash 815956260f846095f12e1682da6f6d6857a2512dcf394dbc569293102b8fe4ad

Summary:	Read/write buffer class for perl
Name:		perl-Data-Buffer
Version:	0.06
Release:	4%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Data-Buffer
Source0:	https://cpan.metacpan.org/modules/by-module/Data/Data-Buffer-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test2::V0)
# Dependencies
# (none)

%description
Data::Buffer implements a low-level binary buffer in which you can get and put
integers, strings, and other data. Internally the implementation is based on
pack and unpack, such that Data::Buffer is really a layer on top of those
built-in functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Buffer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Buffer.3*

%changelog
%autochangelog
