%global source0_hash e5375b2924f3120b68a88c4282bdc0a2dd282dfafbf27229c61c2fa5284121ae

Name:           perl-MooseX-Role-Tempdir
Version:        0.101
Release:        21%{?dist}
Summary:        Moose role to provide temporary directories
License:        ISC
URL:            https://metacpan.org/release/MooseX-Role-Tempdir
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAMB/MooseX-Role-Tempdir-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(MooseX::Role::Parameterized)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

%description
This is a very simple Moose role that provides an attribute 'tmpdir' and
creates a temporary directory (via File::Temp) to go along with it. One
temporary directory will be created for every object with this role, so
keep that in mind if you're going crazy with lots of objects or
creation/destruction.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Role-Tempdir-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
# Changes file is empty
%doc README
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
