%global source0_hash 3dfaf5837ebfdc007895bfca84c3c2e76d589a7d336400e8dfb3243d818215de
Name:           perl-ExtUtils-Typemaps-Default
Version:        1.05
Release:        1%{?dist}
Summary:        Set of useful typemaps
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-Typemaps-Default
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(ExtUtils::Typemaps) >= 3.18-292
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ExtUtils::Typemaps\\)$
# oreon:deps
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps subclass that provides
a set of default mappings (in addition to what perl itself provides). These
default mappings are currently defined as the combination of the mappings
provided by the following typemap classes which are provided in this
distribution:

ExtUtils::Typemaps::ObjectMap
ExtUtils::Typemaps::STL
ExtUtils::Typemaps::Basic

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ExtUtils-Typemaps-Default-%{version}

# this is fixed in BuildRequired version of ExtUtils::Typemap 3.18-292
sed -i 's/3.18_03/3.18/' Build.PL

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
