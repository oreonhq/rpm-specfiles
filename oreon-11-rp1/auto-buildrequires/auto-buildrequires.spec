%global source0_hash 44d5b3199c6d4615c2cdb0014f63d5b9db728318ac084c7c53ffce8cbe27e929

Summary:       Work out BuildRequires for rpmbuild automatically
Name:          auto-buildrequires
Version:       1.3
Release:       14%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later

URL:           http://people.redhat.com/~rjones/auto-buildrequires/
Source0:       http://people.redhat.com/~rjones/auto-buildrequires/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl-podlators
BuildRequires: make

Requires:      rpm-build
Requires:      perl-String-ShellQuote

%description
Auto-BuildRequires is a simple set of scripts for automatically suggesting 
BuildRequires lines for programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc COPYING README
%{_bindir}/auto-br
%{_bindir}/auto-br-rpmbuild
%{_libexecdir}/auto-br-analyze.pl
%{_libexecdir}/%{name}-preload.so
%{_mandir}/man1/autobuildrequires.1*
%{_mandir}/man1/auto-br.1*
%{_mandir}/man1/auto-br-rpmbuild.1*

%changelog
%autochangelog
