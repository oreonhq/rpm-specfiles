%global source0_hash 815ab9ba156cb7d1cc6be2aaa75789f8288ba86d79f220bbe504576bcaa84aca
Name:           perl-SVK
Version:        2.2.3
Release:        46%{?dist}
Summary:        A Distributed Version Control System
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVK
Source0:        https://cpan.metacpan.org/modules/by-authors/id/C/CL/CLKAO/SVK-v%{version}.tar.gz
Patch0:         SVK-v2.2.3-Fix-building-on-Perl-without-dot-in-INC.patch
Patch1:         SVK-v2.2.3-Fix-SVN-Core-version-check.patch
BuildArch:      noarch
Requires:  perl(App::CLI)
Requires:  perl(Class::Accessor::Fast)
Requires:  perl(Class::Data::Inheritable)
Requires:  perl(Pod::Escapes)
Requires:  perl(Pod::Simple)
Requires:  perl(ExtUtils::MakeMaker)
Requires:  perl(Term::ReadKey)
Requires:  perl(Time::Progress)
Requires:  perl(URI)
Provides:  perl(SVK::Version) = %{version}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(SVK\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::Annotate)
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(App::CLI)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Autouse)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Hierarchy)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(IO::Digest)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(PerlIO::eol)
BuildRequires:  perl(PerlIO::via::dynamic)
BuildRequires:  perl(PerlIO::via::symlink)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(SVN::Simple::Edit)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Progress)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
