%global source0_hash a9ca38682f3ebeb8f104a176bda7d424d0cc51d7f5bdfc255a4d600f01174363
Name:           perl-MooseX-LogDispatch
Version:        1.2002
Release:        1%{?dist}
Summary:        Logging Role for Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooseX-LogDispatch
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGOULAH/MooseX-LogDispatch-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(MooseX::LogDispatch::ConfigMaker) = %{version}
Provides:       perl(MooseX::LogDispatch::Interface) = %{version}
Provides:       perl(MooseX::LogDispatch::Logger) = %{version}
%{?perl_default_filter}
%global __requires_exclude ^perl\\(MooseX::LogDispatch::(ConfigMaker|Interface|Logger)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Log::Dispatch::Config)
BuildRequires:  perl(Log::Dispatch::Configurator)
BuildRequires:  perl(Log::Dispatch::Configurator::AppConfig)
BuildRequires:  perl(Log::Dispatch::Null)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Log::Dispatch role for use with your Moose classes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-LogDispatch-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
