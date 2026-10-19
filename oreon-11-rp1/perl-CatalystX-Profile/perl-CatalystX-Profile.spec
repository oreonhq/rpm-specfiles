%global source0_hash 151a352333a6d26626d9001bb7e3b3a11cd4251a191111da60a9657eb66acd6c
Name:           perl-CatalystX-Profile
Version:        0.02
Release:        1%{?dist}
Summary:        Profile your Catalyst application with Devel::NYTProf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CatalystX-Profile
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/CatalystX-Profile-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Catalyst::Runtime) >= 5.80020
Requires:       perl(CatalystX::InjectComponent) >= 0.024
Requires:       perl(Devel::NYTProf) >= 3.01
Requires:       perl(Moose) >= 0.93
Requires:       perl(namespace::autoclean) >= 0.09
Requires:       perl(Sub::Identify) >= 0.04
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(CatalystX::InjectComponent)
BuildRequires:  perl(Devel::NYTProf)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl-generators
# /oreon:deps
%description
This (really basic for now) plugin adds support for profiling your Catalyst
application, without profiling all the crap that happens during setup. This
noise can make finding the real profiling stuff trickier, so profiling is
disabled while this happens.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-Profile-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
