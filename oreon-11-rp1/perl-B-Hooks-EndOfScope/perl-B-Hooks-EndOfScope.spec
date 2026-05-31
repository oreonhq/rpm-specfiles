%global source0_hash edac77a17fc36620c8324cc194ce1fad2f02e9fcbe72d08ad0b2c47f0c7fd8ef

# Run extra test
%if 0%{?perl_bootstrap:1} || ( 0%{?rhel} )
%bcond_with perl_B_Hooks_EndOfScope_enables_extra_test
%else
%bcond_without perl_B_Hooks_EndOfScope_enables_extra_test
%endif
# Run optional test
%bcond_without perl_B_Hooks_EndOfScope_enables_optional_test

Name:		perl-B-Hooks-EndOfScope
Version:	0.28
Release:	5%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:	Execute code after scope compilation finishes
URL:		https://metacpan.org/release/B-Hooks-EndOfScope
Source0:        https://cpan.metacpan.org/modules/by-module/B/B-Hooks-EndOfScope-%{version}.tar.gz



Patch0:		B-Hooks-EndOfScope-0.13-shellbangs.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(lib)
BuildRequires:	perl(Text::ParseWords)
# Dependencies of bundled ExtUtils::HasCompiler
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
# Common Module Requirements
BuildRequires:	perl(Module::Implementation) >= 0.05
BuildRequires:	perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# PP Implementation Only
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Hash::Util::FieldHash)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Tie::Hash)
BuildRequires:	perl(Tie::StdHash)
# XS Implementation Only
BuildRequires:	perl(Variable::Magic) >= 0.48
# Test suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Devel::Hide) >= 0.0007
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
%if %{with perl_B_Hooks_EndOfScope_enables_optional_test}
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
%endif
# Author/Release tests
# Note:
# * Test::Pod::No404s intentionally omitted as it would fail due to
#   missing connectivity in the koji build environment
# * ExtUtils::HasCompiler is bundled, so we don't need to BuildRequire it
%if %{with perl_B_Hooks_EndOfScope_enables_extra_test}
BuildRequires:	perl(blib)
BuildRequires:	perl(Encode)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Path::Tiny) >= 0.062
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Pod::Wordlist)
BuildRequires:	perl(Test::CPAN::Changes)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::Kwalitee) >= 1.21
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::Mojibake)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
BuildRequires:	perl(Test::Spelling), hunspell-en
%endif
# Dependencies
# (none)

%description
This module allows you to execute code when Perl has finished compiling the
surrounding scope.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n B-Hooks-EndOfScope-%{version}

# Remove shellbangs from tests to placate rpmlint
%patch -P 0

# British-English spelling LICENCE upsets US spell checker
echo LICENCE >> xt/author/pod-spell.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%if %{with perl_B_Hooks_EndOfScope_enables_extra_test}
export AUTHOR_TESTING=1
%endif
make test
%if %{with perl_B_Hooks_EndOfScope_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENCE
%doc Changes CONTRIBUTING README t/
%{perl_vendorlib}/B/
%{_mandir}/man3/B::Hooks::EndOfScope.3*
%{_mandir}/man3/B::Hooks::EndOfScope::PP.3*
%{_mandir}/man3/B::Hooks::EndOfScope::XS.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-5
- Prepare for Oreon 11 (RP1)
