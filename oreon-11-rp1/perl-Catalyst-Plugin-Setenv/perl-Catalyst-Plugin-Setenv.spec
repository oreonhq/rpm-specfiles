%global source0_hash f8ece867a13da52d2ac6219f513249a913895cbc43d2bb4b2713aa41b5e7e005
Name:           perl-Catalyst-Plugin-Setenv
Version:        0.03
Release:        1%{?dist}
Summary:        Catalyst::Plugin::Setenv Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Setenv
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRAMBERG/Catalyst-Plugin-Setenv-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
%description
perl Build.PL ./Build ./Build test ./Build install

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Setenv-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
