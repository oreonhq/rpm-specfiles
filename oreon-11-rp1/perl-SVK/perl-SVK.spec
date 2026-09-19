%global source0_hash 815ab9ba156cb7d1cc6be2aaa75789f8288ba86d79f220bbe504576bcaa84aca

Name:           perl-SVK
Version:        2.2.3
Release:        46%{?dist}
Summary:        A Distributed Version Control System
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVK
Source0:        https://cpan.metacpan.org/modules/by-authors/id/C/CL/CLKAO/SVK-v%{version}.tar.gz
Patch0:         SVK-v2.2.3-Fix-building-on-Perl-without-dot-in-INC.patch
# Fix subversion version check, CPAN RT#125150
Patch1:         SVK-v2.2.3-Fix-SVN-Core-version-check.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Algorithm::Annotate)
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(App::CLI)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Autouse) >= 1.15
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Data::Hierarchy) >= 0.30
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(IO::Digest)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Path::Class) >= 0.16
BuildRequires:  perl(PerlIO::eol) >= 0.13
BuildRequires:  perl(PerlIO::via::dynamic) >= 0.11
BuildRequires:  perl(PerlIO::via::symlink) >= 0.02
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::Simple)
#BuildRequires:  perl(SVN::Mirror) >= 0.71
BuildRequires:  perl(SVN::Simple::Edit) >= 0.27
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI)
BuildRequires:  perl(version) >= 0.68
BuildRequires:  perl(YAML::Syck) >= 0.60
BuildRequires:  perl(Time::Progress)
Requires:  perl(App::CLI)
Requires:  perl(Class::Accessor::Fast)
Requires:  perl(Class::Data::Inheritable)
Requires:  perl(Pod::Escapes)
Requires:  perl(Pod::Simple)
Requires:  perl(ExtUtils::MakeMaker)
#Requires:  perl(SVN::Mirror) >= 0.71
Requires:  perl(Term::ReadKey)
Requires:  perl(Time::Progress)
Requires:  perl(URI)
Provides:  perl(SVK::Version) = %{version}

# Remove under-specified provides
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(SVK\\)$

%description
SVK is a decentralized version control system written in Perl. It uses
the Subversion file system but provides additional features:

    * Offline operations like check-in, log, merge.
    * Distributed branches.
    * Lightweight checkout copy management (no .svn directories).
    * Advanced merge algorithms, like star-merge and cherry picking.

For more information about the SVK project, visit http://svk.elixus.org/.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVK-v%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL --skipdeps NO_PACKLIST=1 INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# The tests are a bit hosed. Revisit at some point.
#make test
# Some tests fail: <https://rt.cpan.org/Public/Bug/Display.html?id=58633>
#chmod -R u+w t

%files
%license ARTISTIC COPYING
%doc CHANGES CHANGES-1.0 COMMITTERS README
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/svk

%changelog
%autochangelog
