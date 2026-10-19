%global source0_hash 583545c9e5312bb4193ab16de9f55ff8f4b4a7ded128cee8dd2cb021d4678b5b
Name:           perl-CHI
Version:        0.61
Release:        1%{?dist}
Summary:        Unified cache handling interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CHI
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/CHI-%{version}.tar.gz
Patch1:         perl-CHI-0.60-Adapt-to-changes-in-Cache-FastMmap-1.45.patch
BuildArch:      noarch
%bcond_with author_tests
%bcond_without smoke_tests
%if %{with author_tests}
%endif
%if %{with smoke_tests}
%endif
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Bar\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Baz\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DummySerializer\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Foo\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp::Assert\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::MoreUtils\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Log::Any\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::Duration\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::Duration::Parse\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::HiRes\\)$
Requires: perl(Carp::Assert) >= 0.20
Requires: perl(List::MoreUtils) >= 0.13
Requires: perl(Log::Any) >= 0.06
Requires: perl(Time::Duration) >= 1.06
Requires: perl(Time::Duration::Parse) >= 0.03
Requires: perl(Time::HiRes) >= 1.30
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Cache::FastMmap)
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::JHash)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::MoreUtils)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(MooX::Types::MooseLike::Numeric)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Log::Dispatch)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::Duration)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl-generators
# /oreon:deps
%description
CHI provides a unified caching API, designed to assist a developer in
persisting data for a specified period of time.

%package Test
Summary:        CHI::Test module
Requires:       perl-CHI = %{version}-%{release}
Requires: perl(Test::Deep)
Requires: perl(Test::Exception)
Requires: perl(List::MoreUtils) >= 0.13
Requires: perl(Time::HiRes) >= 1.30
%description Test
CHI::Test and CHI::t perl modules

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CHI-%{version}
%patch -P1 -p1

# Fix bogus permissions
find lib \( -type f -a -executable \) -exec chmod -x {} \;

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__make} test %{?with_author_tests:AUTHOR_TESTING=1} %{?with_smoke_tests:AUTOMATED_TESTING=1}
%files -f %{oreon_filedir}/main.list
%files -n perl-CHI-Test -f %{oreon_filedir}/perl-CHI-Test.list

%changelog

%autochangelog
