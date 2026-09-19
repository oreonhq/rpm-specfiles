%global source0_hash 5547750f239db63b23d3027a07dbb16fd01a220d681e4f61624e6851401463c3

Name:           perl-MooseX-Role-WarnOnConflict
Version:        0.01
Release:        12%{?dist}
Summary:        Warn if classes override role methods without excluding them
License:        Artistic-2.0
URL:            http://cpan.metacpan.org/dist/MooseX-Role-WarnOnConflict/
Source0:        http://cpan.metacpan.org/authors/id/O/OV/OVID/MooseX-Role-WarnOnConflict-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__chmod}
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators

BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Meta::Role::Application::ToClass)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(warnings)

%description
When using Moose::Role, a class which provides a method a role provides
will silently override that method. This can cause strange, hard-to-debug
errors when the role's methods are not called. Simply use
MooseX::Role::WarnOnConflict instead of Moose::Role and overriding a role's
method becomes a composition-time warning. See the synopsis for a
resolution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Role-WarnOnConflict-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
