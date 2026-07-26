%global source0_hash 28a3fc6fea73a19f563f11bd0f28186756d4c74207be6deacaad26d2081b9533

Name:           perl-Test-Command
Version:        0.11
Release:        30%{?dist}
Summary:        Test routines for external commands
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Command
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Command-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.62
# Dependencies:
# (none)

%description
Test::Command intends to bridge the gap between the well tested functions
and objects you choose and their usage in your programs. By examining the
exit status, terminating signal, STDOUT and STDERR of your program you can
determine if it is behaving as expected.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Command-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Command.3*

%changelog
%autochangelog
