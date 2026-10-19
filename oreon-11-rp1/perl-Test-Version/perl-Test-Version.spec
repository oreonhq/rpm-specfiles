%global source0_hash 9ce1dd2897a5f30e1b7f8966ec66f57d8d8f280f605f28c7ca221fa79aca38e0
Name:		perl-Test-Version
Version:	2.09
Release:        28%{?dist}
Summary:        Check to see that versions in modules are sane
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-Version
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Version-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1}
%endif
Requires:	perl(Test::More) >= 0.96
Provides:       perl(Test::Version)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module's goal is to be a one stop shop for checking to see that your
versions across your dist are sane.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Version-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%if 0%{!?perl_bootstrap:1}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.09-28
- Prepare for Oreon 11 (RP1)
