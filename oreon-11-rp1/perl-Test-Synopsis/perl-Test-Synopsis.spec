%global source0_hash d268c98b33d2fa14dbb22b20d6561bab489ee82587dfbe19ad277620c7b8b6de
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global debug_package %{nil}
%undefine _package_note_file
Name:		perl-Test-Synopsis
Version:	0.17
Release:        1%{?dist}
Summary:        Test your SYNOPSIS code
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Synopsis
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Synopsis-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Test::Builder::Module)
Provides:       perl(Test::Synopsis)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Synopsis is an (author) test module to find .pm or .pod files under your
lib directory and then make sure the example snippet code in your SYNOPSIS
section passes the perl compile check.

Note that this module only checks the perl syntax (by wrapping the code with
sub) and doesn't actually run the code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Synopsis-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
