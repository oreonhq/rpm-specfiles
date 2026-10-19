%global source0_hash 9e3bff7486193fa7e4c80774aa175188ff75a71d558ecc06501ddab24c45188d
%bcond_without perl_Git_Wrapper_enables_optional_test
Name:           perl-Git-Wrapper
Version:        0.048
Release:        24%{?dist}
Summary:        Wrap git command-line interface for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Git-Wrapper
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GENEHACK/Git-Wrapper-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Git_Wrapper_enables_optional_test}
%endif
Requires:       git-core
Requires:       perl(IPC::Cmd)
# oreon:deps
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::CheckBin)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
