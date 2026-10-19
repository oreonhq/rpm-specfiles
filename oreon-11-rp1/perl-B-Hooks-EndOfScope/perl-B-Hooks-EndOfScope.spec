%global source0_hash edac77a17fc36620c8324cc194ce1fad2f02e9fcbe72d08ad0b2c47f0c7fd8ef
%bcond_without perl_B_Hooks_EndOfScope_enables_extra_test
%bcond_without perl_B_Hooks_EndOfScope_enables_optional_test
Name:		perl-B-Hooks-EndOfScope
Version:	0.28
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Execute code after scope compilation finishes
URL:		https://metacpan.org/release/B-Hooks-EndOfScope
Source0:        https://cpan.metacpan.org/modules/by-module/B/B-Hooks-EndOfScope-%{version}.tar.gz
Patch0:		B-Hooks-EndOfScope-0.13-shellbangs.patch
BuildArch:	noarch
%if %{with perl_B_Hooks_EndOfScope_enables_optional_test}
%endif
%if %{with perl_B_Hooks_EndOfScope_enables_extra_test}
%endif
Provides:       perl(B::Hooks::EndOfScope)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  hunspell-en
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Pod::Wordlist)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::Mojibake)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Spelling)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Variable::Magic)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%if %{with perl_B_Hooks_EndOfScope_enables_extra_test}
export AUTHOR_TESTING=1
%endif
make test
%if %{with perl_B_Hooks_EndOfScope_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-5
- Prepare for Oreon 11 (RP1)
