%global source0_hash 886ee143ea7cd539b43bed7a287989d16736d75cbfa1f85e2ccceaf9e8959dbd

Name:           perl-Pod-Tidy
Version:        0.10
Release:        30%{?dist}
Summary:        Reformatting Pod Processor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Tidy
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/Pod-Tidy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Wrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Newlines) >= 0.03
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Cmd) >= 1.05
BuildRequires:  perl(Test::Distribution) >= 1.22
BuildRequires:  perl(Test::More)
Requires:       perl(Text::Glob) >= 0.06

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Text::Glob\\)\s*$

Provides:       perl(Pod::Tidy)
%description
This module provides the heavy lifting needed by the podtidy utility
although the API should be general enough that it can be used directly.

podtidy processes a Pod document and attempts to tidy it's formatting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Tidy-%{version}

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
%doc Changes Todo
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
