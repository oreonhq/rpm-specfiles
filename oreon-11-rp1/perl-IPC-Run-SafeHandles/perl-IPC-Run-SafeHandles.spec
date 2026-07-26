%global source0_hash 8ecd3f85e132ca84a32e6f1b3740d0af6f970591fd2ae69ce813aa7b46eebffc

Name:           perl-IPC-Run-SafeHandles
Version:        0.04
Release:        39%{?dist}
Summary:        Use IPC::Run and IPC::Run3 safely
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Run-SafeHandles
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLKAO/IPC-Run-SafeHandles-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter >= 1:5.8.0
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(List::MoreUtils)

BuildRequires:  perl(inc::Module::Install)

# for improved tests
BuildRequires: perl(Test::Pod::Coverage) >= 1.04
BuildRequires: perl(Test::Pod) >= 1.14

%description
IPC::Run and IPC::Run3 are both very upset when you try to use them under
environments where you have STDOUT and/or STDERR tied to something else,
such as under fastcgi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-Run-SafeHandles-%{version}
rm -r inc/

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing
# missing optional features
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
