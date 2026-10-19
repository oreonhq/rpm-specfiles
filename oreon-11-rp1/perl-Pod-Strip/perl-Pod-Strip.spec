%global source0_hash 67506a661fa9caecefe7ba4f42f0bc15b0a6f0967c79607740f6cb6974aed4cd
Name:           perl-Pod-Strip
Version:        1.100
Release:        15%{?dist}
Summary:        Remove POD from Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Strip
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Strip-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Pod::Simple) >= 3.00
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Strip-%{version}

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
