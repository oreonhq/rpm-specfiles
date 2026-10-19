%global source0_hash 160970c29a72afbe412fa4ce1d14ce662ee271ea6fd1754ee62f00f89f62aac2
Name:           perl-Perl-Critic-Deprecated
Version:        1.119
Release:        1%{?dist}
Summary:        Perl::Critic policies that have been superseded by others
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Deprecated
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-Critic-Deprecated-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Critic::Policy) >= 1.094
Requires:       perl(Perl::Critic::Utils) >= 1.094
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Perl::Critic::Policy|Perl::Critic::Utils)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PPI::Node)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The included policies are:
  - Write "$my_variable = 42" instead of "$MyVariable = 42".
  - Write "sub my_function{}" instead of "sub MyFunction{}".
  - Put source-control keywords in every file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Deprecated-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
