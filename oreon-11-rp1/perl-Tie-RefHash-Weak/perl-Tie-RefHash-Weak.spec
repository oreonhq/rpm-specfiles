%global source0_hash bcb4fb2b7575e4caec320577e21e500b0f3ad29fede380d5b54bb84543e76988
Name:		perl-Tie-RefHash-Weak
Version:	0.09
Release:        48%{?dist}
Summary:        Tie::RefHash subclass with weakened references in the keys
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Tie-RefHash-Weak
Source0:        https://cpan.metacpan.org/modules/by-module/Tie/Tie-RefHash-Weak-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Tie::RefHash::Weak)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(Variable::Magic)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Tie::RefHash module can be used to access hashes by reference. This is
useful when you index by object, for example.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Tie-RefHash-Weak-%{version}

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
