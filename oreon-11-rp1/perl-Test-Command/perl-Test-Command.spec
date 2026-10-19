%global source0_hash 28a3fc6fea73a19f563f11bd0f28186756d4c74207be6deacaad26d2081b9533
Name:           perl-Test-Command
Version:        0.11
Release:        1%{?dist}
Summary:        Test routines for external commands
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Command
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Command-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
