%global source0_hash f72b5f13a3e7e1bcc6850f81460504be5691fbfdf6f969bdf9f22c6b5e443f4a
Name:           perl-Acme-PlayCode
Version:        0.12
Release:        44%{?dist}
Summary:        Play code to win
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Acme-PlayCode
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/Acme-PlayCode-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooseX::Object::Pluggable) >= 0.0008
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Object::Pluggable)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Token::Comment)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
It aims to change the code to be better (to be worse if you want).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Acme-PlayCode-%{version}
dos2unix README
dos2unix Changes

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
