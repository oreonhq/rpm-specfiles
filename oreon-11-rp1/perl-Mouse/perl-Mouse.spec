%global source0_hash 3ab8b0f9f96cbe43ff23498d900f91add52455dc9a7d6613a0a8186142bdeecf

Name:           perl-Mouse
Summary:        Moose minus the antlers
Version:        2.6.2
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mouse
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Mouse-v%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Devel::PPPort) >= 3.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.22
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::XSUtil) >= 0.19
BuildRequires:  perl(utf8)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(version) >= 0.9913
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader) >= 0.02
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace) >= 0.10
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
# Optional Tests
BuildRequires:  perl(Data::Dump::Streamer)
BuildRequires:  perl(Declare::Constraints::Simple)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(Locale::US)
BuildRequires:  perl(Moose)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(MouseX::Foreign)
%endif
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(Path::Class)
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Mouse → perl-Pod-Coverage-Moose
# → perl-namespace-autoclean → perl-Mouse
BuildRequires:  perl(Pod::Coverage::Moose)
%endif
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(URI)
# Dependencies
Requires:       perl(Scalar::Util) >= 1.14
Requires:       perl(Data::Dumper)
Requires:       perl(mro)
Requires:       perl(XSLoader) >= 0.02

# Virtual provides for perl-Any-Moose
Provides:       perl(Any-Moose) = %{version}

%{?perl_default_filter}
# filter unversioned Mouse::Util provide from Mouse/PurePerl.pm
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Mouse::Util\\)$

Provides:       perl(Mouse)
Provides:       perl(Mouse::Role)
Provides:       perl(Mouse::Exporter)
Provides:       perl(Mouse::Meta::TypeConstraint)
Provides:       perl(Mouse::Util)
Provides:       perl(Mouse::Util::MetaRole)
Provides:       perl(Mouse::Util::TypeConstraints)
Provides:       perl(Test::Mouse)
Provides:       perl(Mouse::Role)
%description
Moose, a powerful metaobject-fueled extension of the Perl 5 object system,
is wonderful.  (For more information on Moose, please see 'perldoc Moose'
after installing the perl-Moose package.)

Unfortunately, it's a little slow. Though significant progress has been
made over the years, the compile time penalty is a non-starter for some
applications.  Mouse aims to alleviate this by providing a subset of Moose's
functionality, faster.

%package -n perl-Test-Mouse
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Test functions for Mouse specific features
Requires:   %{name} = %{version}-%{release}

%description -n perl-Test-Mouse
This module provides some useful test functions for Mouse based classes. It is
an experimental first release, so comments and suggestions are very welcome.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mouse-v%{version}

# Fix permissions
find . -type f -exec chmod -c -x {} ';'

# Fix shellbangs
find benchmarks/ example/ t/ tool/ -type f -print0 |
  xargs -0 sed -i '1s|^#!.*perl|#!%{__perl}|'

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes benchmarks/ example/ tool/ t/
%{perl_vendorarch}/auto/Mouse/
%{perl_vendorarch}/Mouse.pm
%{perl_vendorarch}/Mouse/
%{perl_vendorarch}/ouse.pm
%{perl_vendorarch}/Squirrel.pm
%{perl_vendorarch}/Squirrel/
%{_mandir}/man3/Mouse.3*
%{_mandir}/man3/Mouse::Exporter.3*
%{_mandir}/man3/Mouse::Meta::Attribute.3*
%{_mandir}/man3/Mouse::Meta::Class.3*
%{_mandir}/man3/Mouse::Meta::Method.3*
%{_mandir}/man3/Mouse::Meta::Method::Accessor.3*
%{_mandir}/man3/Mouse::Meta::Method::Constructor.3*
%{_mandir}/man3/Mouse::Meta::Method::Delegation.3*
%{_mandir}/man3/Mouse::Meta::Method::Destructor.3*
%{_mandir}/man3/Mouse::Meta::Module.3*
%{_mandir}/man3/Mouse::Meta::Role.3*
%{_mandir}/man3/Mouse::Meta::Role::Application.3*
%{_mandir}/man3/Mouse::Meta::Role::Composite.3*
%{_mandir}/man3/Mouse::Meta::Role::Method.3*
%{_mandir}/man3/Mouse::Meta::TypeConstraint.3*
%{_mandir}/man3/Mouse::Object.3*
%{_mandir}/man3/Mouse::PurePerl.3*
%{_mandir}/man3/Mouse::Role.3*
%{_mandir}/man3/Mouse::Spec.3*
%{_mandir}/man3/Mouse::Tiny.3*
%{_mandir}/man3/Mouse::TypeRegistry.3*
%{_mandir}/man3/Mouse::Util.3*
%{_mandir}/man3/Mouse::Util::MetaRole.3*
%{_mandir}/man3/Mouse::Util::TypeConstraints.3*
%{_mandir}/man3/Mouse::XS.3*
%{_mandir}/man3/ouse.3*
%{_mandir}/man3/Squirrel.3*
%{_mandir}/man3/Squirrel::Role.3*

%files -n perl-Test-Mouse
%{perl_vendorarch}/Test/
%{_mandir}/man3/Test::Mouse.3*

%changelog
%autochangelog
