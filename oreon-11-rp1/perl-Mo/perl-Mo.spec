%global source0_hash 91d24152391f8c2797ee35039138daea6de3ee03bdf3e1b8724fa5c75540ceb9

Name:           perl-Mo
Version:        0.40
Release:        29%{?dist}
Summary:        Perl micro-object system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mo
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/Mo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::MetaRole)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Mo provides the bare-minimum for a Perl object system, compared to other similar
systems such as Moose, Mouse and Moo.

%package Golf
Summary:        Mo minimization support module
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Golf
%{summary}.

%package Moose
Summary:        Use Moose instead of Mo
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Moose)
Requires:       perl(Moose::Role)

%description Moose
%{summary}.

%package Mouse
Summary:        Use Mouse instead of Mo
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Mouse)
Requires:       perl(Mouse::Role)
Requires:       perl(Mouse::Util::MetaRole)

%description Mouse
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mo-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Mo/Golf.pm
%exclude %{perl_vendorlib}/Mo/Moose.pm
%exclude %{perl_vendorlib}/Mo/Mouse.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Mo::Golf.3pm.*
%exclude %{_mandir}/man3/Mo::Moose.3pm.*
%exclude %{_mandir}/man3/Mo::Mouse.3pm.*
%{_bindir}/*

%files Golf
%license LICENSE
%{perl_vendorlib}/Mo/Golf.pm
%{_mandir}/man3/Mo::Golf.3pm.*

%files Moose
%license LICENSE
%{perl_vendorlib}/Mo/Moose.pm
%{_mandir}/man3/Mo::Moose.3pm.*

%files Mouse
%license LICENSE
%{perl_vendorlib}/Mo/Mouse.pm
%{_mandir}/man3/Mo::Mouse.3pm.*

%changelog
%autochangelog
