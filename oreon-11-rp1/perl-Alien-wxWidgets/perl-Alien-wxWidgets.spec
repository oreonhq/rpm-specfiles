%global source0_hash 53224e4bbbefff4cf7b63ed9a62963893b9ffd4965d70d96710348f8676de249

Name:           perl-Alien-wxWidgets
Version:        0.69
Release:        31%{?dist}
Summary:        Building, finding and using wxWidgets binaries
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-wxWidgets
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Alien-wxWidgets-%{version}.tar.gz
BuildRequires:  gcc, gcc-c++
BuildRequires:  wxGTK-devel
# A lot of stuff used by inc/My/Build/Base.pm.
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 1.50
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(strict)
BuildRequires:  perl(LWP::Protocol::https)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

# No binaries in this package
%global debug_package %{nil}

%description
"Alien::wxWidgets" can be used to detect and get configuration
settings from an installed wxWidgets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-wxWidgets-%{version}

%build
export WX_CONFIG="%{_bindir}/wx-config-3.2"
%{__perl} Build.PL installdirs=vendor < /dev/null
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%{perl_vendorarch}/Alien/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
