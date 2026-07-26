%global source0_hash 16a78ddcf36a79623b91be75507b760867ddf2ab6a108b44d39a01614422211f

Name:           perl-MooseX-Configuration
Version:        0.02
Release:        29%{?dist}
Summary:        Define attributes which come from configuration files
License:        Artistic-2.0
URL:            https://metacpan.org/release/MooseX-Configuration
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-Configuration-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(autodie)
BuildRequires:  perl(B)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(warnings)

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
