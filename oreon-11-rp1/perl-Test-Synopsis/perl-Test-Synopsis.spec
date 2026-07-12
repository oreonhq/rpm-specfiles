%global source0_hash d268c98b33d2fa14dbb22b20d6561bab489ee82587dfbe19ad277620c7b8b6de

# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

# Similarly, for package note feature
%undefine _package_note_file

Name:		perl-Test-Synopsis
Version:	0.17
Release:	14%{?dist}
Summary:	Test your SYNOPSIS code
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Synopsis
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Synopsis-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(parent)
BuildRequires:	perl(Pod::Simple) >= 3.09
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::Builder) >= 0.34
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
# Extra Tests; can't run these when bootstrapping or in EL since many
# of these packages won't be available
%if 0%{!?perl_bootstrap:1} && 0%{!?rhel:1}
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Pod::Wordlist) >= 1.06
BuildRequires:	perl(Test::CPAN::Changes)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::DistManifest)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::Kwalitee) >= 1.21
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::Mojibake)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
BuildRequires:	perl(Test::Spelling) >= 0.12, hunspell-en
BuildRequires:	perl(Test::Version)
%endif
# Dependencies
Requires:	perl(Test::Builder::Module)

Provides:       perl(Test::Synopsis)
%description
Test::Synopsis is an (author) test module to find .pm or .pod files under your
lib directory and then make sure the example snippet code in your SYNOPSIS
section passes the perl compile check.

Note that this module only checks the perl syntax (by wrapping the code with
sub) and doesn't actually run the code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Synopsis-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if 0%{!?perl_bootstrap:1} && 0%{!?rhel:1}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README README.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Synopsis.3*

%changelog
%autochangelog
