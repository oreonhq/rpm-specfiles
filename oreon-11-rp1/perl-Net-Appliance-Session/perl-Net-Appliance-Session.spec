%global source0_hash a2073aaa56827518174c3e9b0c7fba8c39d5a4d876b67a9fc0bb18729186c2cf
Name:           perl-Net-Appliance-Session
Version:        4.300005
Release:        1%{?dist}
Summary:        Run command-line sessions to network appliances
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Appliance-Session
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Net-Appliance-Session-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::Load)
Requires:       perl(Net::CLI::Interact) >= 2.300003
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::CLI::Interact\\)$
# oreon:deps
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::CLI::Interact)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Use this module to establish an interactive command-line session with a
network appliance. There is special support for moving into "privileged"
mode and "configure" mode, along with the ability to send commands to the
connected device and retrieve returned output.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Appliance-Session-%{version}

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
