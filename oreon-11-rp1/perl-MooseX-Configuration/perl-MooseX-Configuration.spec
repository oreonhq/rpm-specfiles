%global source0_hash 16a78ddcf36a79623b91be75507b760867ddf2ab6a108b44d39a01614422211f
Name:           perl-MooseX-Configuration
Version:        0.02
Release:        1%{?dist}
Summary:        Define attributes which come from configuration files
License:        Artistic-2.0
URL:            https://metacpan.org/release/MooseX-Configuration
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-Configuration-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(autodie)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module lets you define attributes which can come from a configuration
file. It also adds a role to your class which allows you to write a
configuration file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Configuration-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
