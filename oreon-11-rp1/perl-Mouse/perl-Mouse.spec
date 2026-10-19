%global source0_hash 3ab8b0f9f96cbe43ff23498d900f91add52455dc9a7d6613a0a8186142bdeecf
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Mouse
Summary:        Moose minus the antlers
Version:        2.6.2
Release:        2%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mouse
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYOHEX/Mouse-v%{version}.tar.gz
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(Scalar::Util) >= 1.14
Requires:       perl(Data::Dumper)
Requires:       perl(mro)
Requires:       perl(XSLoader) >= 0.02
Provides:       perl(Any-Moose) = %{version}
%{?perl_default_filter}
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump::Streamer)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Declare::Constraints::Simple)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::US)
BuildRequires:  perl(Module::Build::XSUtil)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MouseX::Foreign)
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Pod::Coverage::Moose)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(URI)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles perl-Test-Mouse usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Mouse -f %{oreon_filedir}/perl-Test-Mouse.list

%changelog

%autochangelog
