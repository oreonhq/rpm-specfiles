%global source0_hash f72b5f13a3e7e1bcc6850f81460504be5691fbfdf6f969bdf9f22c6b5e443f4a

Name:           perl-Acme-PlayCode
Version:        0.12
Release:        44%{?dist}
Summary:        Play code to win
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Acme-PlayCode
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/Acme-PlayCode-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose) >= 0.57
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Object::Pluggable) >= 0.0008
BuildRequires:  perl(Path::Class) >= 0.16
BuildRequires:  perl(PPI) >= 1.201
BuildRequires:  perl(PPI::Token::Comment)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.22
Requires:       perl(MooseX::Object::Pluggable) >= 0.0008

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

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
