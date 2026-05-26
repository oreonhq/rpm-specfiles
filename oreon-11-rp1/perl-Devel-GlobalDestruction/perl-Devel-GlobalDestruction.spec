Name:		perl-Devel-GlobalDestruction
Version:	0.14
Release:	28%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:	Expose PL_dirty, the flag that marks global destruction
URL:		https://metacpan.org/release/Devel-GlobalDestruction
Source:		https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-GlobalDestruction-0.14.tar.gz
# oreon url source checksums begin
%global source0_sha256 34b8a5f29991311468fe6913cadaba75fd5d2b0b3ee3bb41fe5b53efab9154ab
%global source0_file Devel-GlobalDestruction-0.14.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Text::ParseWords)
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Exporter::Progressive) >= 0.001011
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(threads)
BuildRequires:	perl(threads::shared)
# Dependencies
# (none)

%description
Perl's global destruction is a little tricky to deal with with respect to
finalizers because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happening you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Devel-GlobalDestruction-0.14.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "34b8a5f29991311468fe6913cadaba75fd5d2b0b3ee3bb41fe5b53efab9154ab" || { echo "oreon: Source0 SHA256 mismatch for Devel-GlobalDestruction-0.14.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Devel-GlobalDestruction-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README t/
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::GlobalDestruction.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-28
- Prepare for Oreon 11 (RP1)
