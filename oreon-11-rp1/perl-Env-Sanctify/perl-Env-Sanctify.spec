%global source0_hash 20e3b5661c265474a69f2899478eb27b9464925586bb6b6fb666129e5828325f
Name:		perl-Env-Sanctify
Summary:        Lexically scoped sanctification of %ENV
Version:	1.12
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Env-Sanctify
Source0:        https://cpan.metacpan.org/modules/by-module/Env/Env-Sanctify-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Env::Sanctify)
Provides:       perl(Env::Sanctify)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Env::Sanctify is a module that provides lexically-scoped manipulation and
sanctification of %%ENV. You can specify that it alter or add additional
environment variables or remove existing ones according to a list of matching
regexen. You can then either restore the environment back manually or let the
object fall out of scope, which automagically restores. It's useful for
manipulating the environment that forked processes and sub-processes will
inherit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Env-Sanctify-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test AUTHOR_TESTING=1 RELEASE_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
