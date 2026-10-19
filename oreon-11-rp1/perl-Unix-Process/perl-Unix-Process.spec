%global source0_hash 83da4cab1e4ea4ded8daddf45988bd581416431c907b0e18a3238e950a9c9107
Name:           perl-Unix-Process
Version:        1.3101
Release:        1%{?dist}
Summary:        Perl extension to get PID information from ps command
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Unix-Process
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Unix-Process-%{version}.tar.gz
Patch0:         Unix-Process-1.3101-Replace-bin-ps.patch
BuildArch:      noarch
Requires:       procps-ng
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  procps-ng
BuildRequires:  sed
# /oreon:deps
%description
This is a Perl module that can fetch ps command output fields.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Unix-Process-%{version}
# Correct ps command location
%patch -P0 -p1
sed -i -e 's|XXX|%{_bindir}/ps|g' Makefile.PL Process.pm

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
