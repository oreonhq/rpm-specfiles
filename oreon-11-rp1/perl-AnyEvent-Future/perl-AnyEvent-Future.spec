%global source0_hash b028bbcdd9abfe956dc719918aaa0c5f837fc5693b62a9cd885478f13e24b746
Name:           perl-AnyEvent-Future
Version:        0.05
Release:        1%{?dist}
Summary:        Use Future with AnyEvent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-Future/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/AnyEvent-Future-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Future)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Timer)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This subclass of Future integrates with AnyEvent, allowing the await method
to block until the future is ready. It allows AnyEvent-using code to be
written that returns Future instances, so that it can make full use of
Future's abilities, including Future::Utils, and also that modules using it
can provide a Future-based asynchronous interface of their own.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-Future-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
