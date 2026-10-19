%global source0_hash 34b8a5f29991311468fe6913cadaba75fd5d2b0b3ee3bb41fe5b53efab9154ab
Name:		perl-Devel-GlobalDestruction
Version:	0.14
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Expose PL_dirty, the flag that marks global destruction
URL:		https://metacpan.org/release/Devel-GlobalDestruction
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-GlobalDestruction-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Devel::GlobalDestruction)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perl's global destruction is a little tricky to deal with with respect to
finalizers because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happening you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-GlobalDestruction-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-28
- Prepare for Oreon 11 (RP1)
