%global source0_hash c466468854bbf5f35222aecb987d596267de1f25c73aef8149cde11c58456858

Name:           perl-Test2-Tools-Command
Version:        0.20
Release:        8%{?dist}
Summary:        Test simple unix commands
License:        BSD-3-Clause

URL:            https://metacpan.org/pod/Test2::Tools::Command
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMATES/Test2-Tools-Command-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(warnings)

%description
This module tests that commands given particular arguments result in particular
outputs by way of the exit status word, standard output, and standard error.
Various parameters to the command function alter exactly how this is done, in
addition to variables that can be set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Test2-Tools-Command-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Test2::Tools::Command*.*

%changelog
%autochangelog
