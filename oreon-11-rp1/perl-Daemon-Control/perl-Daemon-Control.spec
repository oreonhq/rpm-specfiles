%global source0_hash 8440389a83166f5b993f806d9f60460677ee2af1c613600968989333d70d4707

Name:           perl-Daemon-Control
Version:        0.001010
Release:        20%{?dist}
Summary:        Create init scripts in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Daemon-Control
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYMKAT/Daemon-Control-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::Path) >= 2.08

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Path\\)$

%description
Daemon::Control provides a library for creating init scripts in perl. Your
perl script just needs to set the accessors for what and how you want
something to run and the library takes care of the rest.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Daemon-Control-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
