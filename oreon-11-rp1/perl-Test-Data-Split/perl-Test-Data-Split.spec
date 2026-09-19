%global source0_hash e5083890adad30d7de50703569d5f5cef174a198593522ea7b46ce387b828022

%define upstream_name    Test-Data-Split

Name:       perl-%{upstream_name}
Version:    0.2.2
Release:    15%{?dist}

Summary:    Split data-driven tests into several test scripts
License:    MIT
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{version}.tar.gz

Requires:  perl(List::MoreUtils)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::All)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Build) >= 0.280.0
BuildRequires: perl(MooX)
BuildRequires: perl(MooX::late)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(autodie)
BuildRequires: perl(blib)
BuildRequires: perl(lib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
This module splits a set of data with IDs and arbitrary values into one test
file per (key+value) for easy parallelization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%license LICENSE
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
%autochangelog
