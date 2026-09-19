%global source0_hash 4a2dbe1cd1c82c31f2bb9f3e417f0b04fadc171590df15330109c33d4d208175

Name:           perl-Proc-InvokeEditor
Version:        1.13
Release:        25%{?dist}
Summary:        Perl extension for starting a text editor
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-InvokeEditor
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTEVENS/Proc-InvokeEditor-%{version}.tar.gz
# Remove hard-coded shell bangs from documentation
Patch0:         Proc-InvokeEditor-1.07-Remove-shell-bangs.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp::Assert) >= 0.11
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Temp) >= 0.12
BuildRequires:  perl(IPC::Cmd)
# Text::ParseWords not used on Linux
BuildRequires:  perl(vars)
# Tests:
# ed || vi must be installed to pass tests
BuildRequires:  ed
# Test::CPAN::Meta not used
BuildRequires:  perl(Test::More) >= 0.08
# Test::Perl::Critic not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       perl(Carp::Assert) >= 0.11
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(File::Temp) >= 0.12
# List default editors enumarated by this Perl module
Suggests:       ed
Suggests:       vim-core

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp::Assert|File::Spec|File::Temp)\\)$

%description
This Perl module provides the ability to supply some text to an external text
editor, have it edited by the user, and retrieve the results.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-InvokeEditor-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
