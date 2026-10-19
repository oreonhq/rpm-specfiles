%global source0_hash d809676471c7ebea65cf5b6f0309223697f71fe60fa97e6d1bcb0d837880f167
Name:           perl-Commandable
Version:        0.14
Release:        1%{?dist}
Summary:        utilities for commandline-based programs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Commandable
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Commandable-0.14.tar.gz
%{?perl_default_filter}
Provides:       perl(Commandable)
Provides:       perl(Commandable::Command)
Provides:       perl(Commandable::Finder)
Provides:       perl(Commandable::Finder::MethodAttributes)
Provides:       perl(Commandable::Finder::Packages)
Provides:       perl(Commandable::Finder::SubAttributes)
Provides:       perl(Commandable::Finder::SubAttributes::Attrs)
Provides:       perl(Commandable::Invocation)
Provides:       perl(Commandable::Output)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(experimental)
BuildRequires:  perl(meta)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
utilities for commandline-based programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Commandable-%{version}

%build

/usr/bin/perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
