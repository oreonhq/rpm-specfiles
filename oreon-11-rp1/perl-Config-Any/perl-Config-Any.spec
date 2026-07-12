%global source0_hash c0668eb5f2cd355bf20557f04dc18a25474b7a0bcfa79562e3165d9a3c789333

Name:           perl-Config-Any
Summary:        Load configuration from different file formats, transparently
Version:        0.33
Release:        8%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Any
Source0:        https://cpan.metacpan.org/modules/by-module/Config/Config-Any-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Pluggable::Object) >= 3.6
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Optional Functionality
BuildRequires:  perl(Config::General) >= 2.48
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(YAML)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(XML::LibXML) >= 1.59
# Dependencies
Requires:       perl(Config::General) >= 2.48
Requires:       perl(Config::Tiny)
Requires:       perl(Cpanel::JSON::XS)
Requires:       perl(XML::NamespaceSupport)
Requires:       perl(XML::Simple)
Requires:       perl(YAML::XS)
Requires:       perl(YAML)

Provides:       perl(Config::Any)
%description
Config::Any provides a facility for Perl applications and libraries to
load configuration data from multiple different file formats. It supports
XML, YAML, JSON, Apache-style configuration, Windows INI files, and even
Perl code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Config-Any-%{version}

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
# conf/ for examples of different config types
%doc Changes README t/conf/
%{perl_vendorlib}/Config/
%{_mandir}/man3/Config::Any.3*
%{_mandir}/man3/Config::Any::Base.3*
%{_mandir}/man3/Config::Any::General.3*
%{_mandir}/man3/Config::Any::INI.3*
%{_mandir}/man3/Config::Any::JSON.3*
%{_mandir}/man3/Config::Any::Perl.3*
%{_mandir}/man3/Config::Any::XML.3*
%{_mandir}/man3/Config::Any::YAML.3*

%changelog
%autochangelog
