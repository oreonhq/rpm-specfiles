%global source0_hash 76cca0e8936f7054b85889536ecfc8c59ea8b8404f0bd0625d718d978567533e

Name:           perl-MooseX-Workers
Version:        0.24
Release:        34%{?dist}
Summary:        Provides a simple sub-process management for asynchronous tasks
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Workers
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/MooseX-Workers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
BuildRequires:  perl(warnings)
Requires:       perl(POE::Wheel::Run)

%{?perl_default_filter}

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
