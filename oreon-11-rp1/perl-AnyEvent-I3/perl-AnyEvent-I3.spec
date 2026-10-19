%global source0_hash 1bcd3b60db3d5560148de791353e8af1172264f5a85e77197b9ffc041dac483a
Name:           perl-AnyEvent-I3
Version:        0.19
Release:        1%{?dist}
Summary:        Communicate with the i3 window manager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-I3
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTPLBG/AnyEvent-I3-%{version}.tar.gz
BuildArch:      noarch
Recommends:     i3 >= 4.14
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  i3
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module connects to the i3 window manager using the UNIX socket based
IPC interface it provides (if enabled in the configuration file). You can
then subscribe to events or send messages and receive their replies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn AnyEvent-I3-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
