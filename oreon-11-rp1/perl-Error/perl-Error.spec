%global source0_hash 34d382276c0fb0d6b38355b94c96a30b12d834d5662eb53f088ee25e3e712924
Name:           perl-Error
Epoch:          1
Version:        0.17030
Release:        3%{?dist}
Summary:        Error/exception handling in an OO-ish way
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND X11
URL:            https://metacpan.org/release/Error
Source0:        https://cpan.metacpan.org/modules/by-module/Error/Error-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
%global __provides_exclude_from ^%{_docdir}
%global __requires_exclude_from ^%{_docdir}
Provides:       perl(Error)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Error package provides two interfaces. Firstly Error provides a
procedural interface to exception handling. Secondly Error is a base class
for errors/exceptions that can either be thrown, for subsequent catch, or
can simply be recorded.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Error-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17030-3
- Prepare for Oreon 11 (RP1)
