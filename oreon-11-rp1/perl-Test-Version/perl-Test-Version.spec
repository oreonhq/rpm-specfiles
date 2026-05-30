%global source0_hash 9ce1dd2897a5f30e1b7f8966ec66f57d8d8f280f605f28c7ca221fa79aca38e0

Name:		perl-Test-Version
Version:	2.09
Release:	28%{?dist}
Summary:	Check to see that versions in modules are sane
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-Version
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Version-%{version}.tar.gz

BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(Module::Metadata) >= 1.000020
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(version) >= 0.86
BuildRequires:	perl(warnings)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(blib) >= 1.01
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Tester)
# ===================================================================
# Author/Release test requirements
#
# Don't run these tests or include their requirements if we're
# bootstrapping, as many of these modules require each other for
# their author/release tests.
# ===================================================================
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::CPAN::Changes) >= 0.19
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
%endif
# ===================================================================
# Runtime dependencies
# ===================================================================
Requires:	perl(Test::More) >= 0.96

%description
This module's goal is to be a one stop shop for checking to see that your
versions across your dist are sane.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test-Version-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if 0%{!?perl_bootstrap:1}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Version.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.09-28
- Prepare for Oreon 11 (RP1)
