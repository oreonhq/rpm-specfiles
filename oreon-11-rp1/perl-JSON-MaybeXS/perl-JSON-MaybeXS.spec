%global source0_hash cd3937afa78831f80a2ad5abab6c51b9e82fca4c31e5856ea208d598db5dc867
Name:		perl-JSON-MaybeXS
Summary:        Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
Version:	1.004008
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/JSON-MaybeXS
Source0:        https://cpan.metacpan.org/modules/by-module/JSON/JSON-MaybeXS-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Cpanel::JSON::XS) >= 2.3310
Provides:       perl(JSON::MaybeXS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Mksymlists)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
