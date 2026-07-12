%global source0_hash cd3937afa78831f80a2ad5abab6c51b9e82fca4c31e5856ea208d598db5dc867

# Note: this package takes the approach of adding a hard dependency on
# upstream's preferred back-end, Cpanel::JSON::XS, rather than using
# a virtual provides/requires arrangement so that any of the supported
# back-ends could be used. This is not only much simpler and does not
# involve modifications to the back-end packages, but it also makes for
# consistent results as we're always using the same, most-tested
# back-end.

Name:		perl-JSON-MaybeXS
Summary:	Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
Version:	1.004008
Release:	5%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/JSON-MaybeXS
Source0:	https://cpan.metacpan.org/modules/by-module/JSON/JSON-MaybeXS-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(lib)
BuildRequires:	perl(Text::ParseWords)
# Dependencies of bundled ExtUtils::HasCompiler
BuildRequires:	perl(Config)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(ExtUtils::Mksymlists)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
%if 0%{?fedora} > 36 || 0%{?rhel} > 9
BuildRequires:	perl(Cpanel::JSON::XS) >= 4.38
BuildRequires:	perl(experimental)
%else
BuildRequires:	perl(Cpanel::JSON::XS) >= 2.3310
%endif
BuildRequires:	perl(Exporter)
BuildRequires:	perl(if)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(JSON::PP) >= 2.27300
BuildRequires:	perl(JSON::XS) >= 3.0
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs) >= 0.002006
# Dependencies
%if 0%{?fedora} > 36 || 0%{?rhel} > 9
Requires:	perl(Cpanel::JSON::XS) >= 4.38
Requires:	perl(experimental)
%else
Requires:	perl(Cpanel::JSON::XS) >= 2.3310
%endif

Provides:       perl(JSON::MaybeXS)
%description
This module first checks to see if either Cpanel::JSON::XS or JSON::XS
is already loaded, in which case it uses that module. Otherwise it tries
to load Cpanel::JSON::XS, then JSON::XS, then JSON::PP in order, and
either uses the first module it finds or throws an error.

It then exports the "encode_json" and "decode_json" functions from the
loaded module, along with a "JSON" constant that returns the class name
for calling "new" on.

If you're writing fresh code rather than replacing JSON.pm usage, you
might want to pass options as constructor args rather than calling
mutators, so we provide our own "new" method that supports that.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n JSON-MaybeXS-%{version}

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
%doc Changes README
%{perl_vendorlib}/JSON/
%{_mandir}/man3/JSON::MaybeXS.3*

%changelog
%autochangelog
