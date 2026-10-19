%global source0_hash bcd6d82f6c8af0fe069fced7dd165a4795b0b6e92351c7d4e5a1ab9a14fc35c6
Name:           perl-Class-Std
Version:        0.013
Release:        1%{?dist}
Summary:        Support for creating standard "inside-out" classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Std
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Std-%{version}.tar.gz
Patch0:         Class-Std-0.013-POD-encoding.patch
BuildArch:      noarch
Requires:       perl(Data::Dumper)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides tools that help to implement the "inside out object"
class structure in a convenient and standard way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Std-%{version}
%patch -P0 -p1

%build

perl Build.PL installdirs=vendor
./Build
%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
