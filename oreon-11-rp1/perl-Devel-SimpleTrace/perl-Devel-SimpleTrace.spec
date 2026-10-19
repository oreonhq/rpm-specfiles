%global source0_hash d318a85bb29ee3c770e6b888585692a6f1a0173faf001be995e97481212536bf
Name:           perl-Devel-SimpleTrace
Version:        0.08
Release:        1%{?dist}
Summary:        See where you code warns and dies using stack traces
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-SimpleTrace
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/Devel-SimpleTrace-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module can be used to more easily spot the place where a program or a
module generates errors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-SimpleTrace-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
