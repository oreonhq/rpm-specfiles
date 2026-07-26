%global source0_hash 9e3bff7486193fa7e4c80774aa175188ff75a71d558ecc06501ddab24c45188d

# Run optional test
%bcond_without perl_Git_Wrapper_enables_optional_test

Name:           perl-Git-Wrapper
Version:        0.048
Release:        24%{?dist}
Summary:        Wrap git command-line interface for Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Git-Wrapper
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GENEHACK/Git-Wrapper-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Devel::CheckBin)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Symbol)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Test::Pod 1.4 not used
# Test::Pod::Coverage 1.08 not used
%if %{with perl_Git_Wrapper_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Path::Class) >= 0.26
%endif
Requires:       git-core
Requires:       perl(IPC::Cmd)

%description
Git::Wrapper provides an API for git that uses Perl data structures for
argument passing, instead of CLI-style --options as Git does.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Git-Wrapper-%{version}

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
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
