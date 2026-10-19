%global source0_hash 4717d700caa7bfdef9d7b4ec2f48a0df06ece758afeaa9e8b3f04961b9c368a6
Name:           perl-Role-Basic
Version:        0.16
Release:        1%{?dist}
Summary:        Just roles. Nothing else
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Role-Basic
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/Role-Basic-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Simplified Moose-like roles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Role-Basic-%{version}
# Convert to utf-8
iconv -f ISO-8859-1 -t utf-8 Changes > Changes~
mv Changes~ Changes

%build

%{__perl} Build.PL installdirs=vendor
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
