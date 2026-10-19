%global source0_hash 76cca0e8936f7054b85889536ecfc8c59ea8b8404f0bd0625d718d978567533e
Name:           perl-MooseX-Workers
Version:        0.24
Release:        1%{?dist}
Summary:        Provides a simple sub-process management for asynchronous tasks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Workers
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/MooseX-Workers-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(POE::Wheel::Run)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MooseX::Workers is a Role that provides easy delegation of long-running
tasks into a managed child process. Process management is taken care of via
POE and it's POE::Wheel::Run module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Workers-%{version}

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
