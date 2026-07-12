%global source0_hash 3cde0138a23a29bd7a46b62fa775a8a82fc6692bea2a2dc2113660dd26e4bf60

Name:           perl-MooseX-GlobRef
Version:        0.0701
Release:        42%{?dist}
Summary:        Store a Moose object in glob reference
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-GlobRef
Source0:        https://cpan.metacpan.org/authors/id/D/DE/DEXTER/MooseX-GlobRef-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exception::Assertion)
BuildRequires:  perl(Exception::Base)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Assert)
BuildRequires:  perl(Test::Unit::Lite) >= 0.11
Requires:       perl(Data::Dumper)

Obsoletes:      perl-MooseX-GlobRef-Object <= 0.0701-2.fc15

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moose\\)\s*$

Provides:       perl(MooseX::GlobRef)
%description
This meta-policy allows to store Moose object in glob reference or file
handle. The class attributes will be stored in anonymous hash associated
with glob reference. It allows to create a Moose version of IO::Handle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-GlobRef-%{version}
find eg -type f -exec chmod a-x {} +

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes eg README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
