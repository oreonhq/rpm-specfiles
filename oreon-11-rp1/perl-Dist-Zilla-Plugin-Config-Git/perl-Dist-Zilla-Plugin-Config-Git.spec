%global source0_hash 502f35869dd0841cb985e707d025ec65d14dd4f389c624870026874f9bdf82a5

Name:           perl-Dist-Zilla-Plugin-Config-Git
Version:        0.92
Release:        27%{?dist}
Summary:        Dist::Zilla configuration for a Git repository
License:        Artistic-2.0
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Config-Git
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBYRD/Dist-Zilla-Plugin-Config-Git-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla::Role::Plugin) >= 1.000
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose) >= 0.34
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types) >= 0.06
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::clean) >= 0.06
BuildRequires:  perl(String::Errf) >= 0.001
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Dist::Zilla::Role::Plugin) >= 1.000
Requires:       perl(Moose) >= 0.34
Requires:       perl(MooseX::Types) >= 0.06
Requires:       perl(namespace::clean) >= 0.06
Requires:       perl(String::Errf) >= 0.001

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Moose|MooseX::Types|namespace::clean|String::Errf)\\)$

%description
This is a Dist::Zilla configuration plugin for Git repository/branch
information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-Config-Git-%{version}

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
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
