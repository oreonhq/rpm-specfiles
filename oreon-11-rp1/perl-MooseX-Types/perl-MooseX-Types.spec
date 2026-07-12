%global source0_hash a5374c7b0273220239b19dda88b824dd73b95398c913c5c9e305edbdb5e0270f

Name:           perl-MooseX-Types
Version:        0.51
Release:        3%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Organize your Moose types in libraries
URL:            https://metacpan.org/dist/MooseX-Types
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan) >= 6.00
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 1.06
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Union)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::autoclean) >= 0.16
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods) >= 0.100052
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Moose)
# Dependencies
# (none)

Provides:       perl(MooseX::Types)
Provides:       perl(MooseX::Types::Moose)
%description
The types provided with the Moose man page are by design global. This
package helps you to organize and selectively import your own and the
built-in types in libraries. As a nice side effect, it catches typos at
compile-time too.

However, the main reason for this module is to provide an easy way to not
have conflicts with your type names, since the internal fully qualified
names of the types will be prefixed with the library's name.

This module will also provide you with some helper functions to make it
easier to use Moose types in your code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-Types-%{version}

# fix shebang
/usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/00-report-prereqs.t

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENCE
%doc Changes CONTRIBUTING README t/
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::Types.3*
%{_mandir}/man3/MooseX::Types::Base.3*
%{_mandir}/man3/MooseX::Types::CheckedUtilExports.3*
%{_mandir}/man3/MooseX::Types::Combine.3*
%{_mandir}/man3/MooseX::Types::Moose.3*
%{_mandir}/man3/MooseX::Types::TypeDecorator.3*
%{_mandir}/man3/MooseX::Types::UndefinedType.3*
%{_mandir}/man3/MooseX::Types::Util.3*
%{_mandir}/man3/MooseX::Types::Wrapper.3*

%changelog
%autochangelog
