%global source0_hash 886ee143ea7cd539b43bed7a287989d16736d75cbfa1f85e2ccceaf9e8959dbd
Name:           perl-Pod-Tidy
Version:        0.10
Release:        1%{?dist}
Summary:        Reformatting Pod Processor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Tidy
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/Pod-Tidy-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Text::Glob) >= 0.06
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Text::Glob\\)\s*$
Provides:       perl(Pod::Tidy)
# oreon:deps
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Newlines)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Pod::Wrap)
BuildRequires:  perl(Test::Cmd)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
