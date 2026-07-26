%global source0_hash 8704bfe505f66b340f62e85c9ff319c19e9670b26d4b012c91f4e103b1daace0

Name:           perl-MooseX-Storage
Summary:        A serialization framework for Moose classes
Version:        0.53
Release:        18%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Storage-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-Storage
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.7501
BuildRequires:  perl(IO::AtomicFile)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.99
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::Any)
BuildRequires:  sed
# test BR
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::JSON)
BuildRequires:  perl(Test::Deep::Type)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires) >= 0.05
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(utf8)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::XS)
#BuildRequires:  perl(MooseX::Storage::Format::JSONpm)

%{?perl_default_filter}

%description
MooseX::Storage is a serialization framework for Moose, it provides a
very flexible and highly pluggable way to serialize Moose classes to a
number of different formats and styles. This is still an early release
of this module, so use with caution. It's outward facing serialization
API should be considered stable, but I still reserve the right to make
tweaks if I need too. Anything beyond the basic pack/unpack, freeze/thaw
and load/store should not be relied on. There are 3 levels to the
serialization, each of which builds upon the other and each of which
can be customized to the specific needs of your class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Storage-%{version}

# silence rpmlint warnings
sed -i '1s,#!.*perl,#!/usr/bin/perl,' t/*.t
chmod 0644 t/*.t

%build
/usr/bin/perl Makefile.PL --skipdeps INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README t/
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
