%global source0_hash bafeee8fdc96eb06306a0c58bbdb7209b6de45f850e75fdc6b16db576e05e422
Name:           perl-File-Pid
Version:        1.01
Release:        47%{?dist}
Summary:        Pid File Manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Pid
Source0:        https://cpan.metacpan.org/authors/id/C/CW/CWEST/File-Pid-%{version}.tar.gz
Patch0:         File-Pid-1.01-RT-18960-Fixed-using-of-uninitialized-value.patch
BuildArch:      noarch
Requires:       perl(Class::Accessor::Fast) >= 0.19
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::Accessor::Fast\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This software manages a pid file for you. It will create a pid file,
query the process within to discover if it's still running, and remove
the pid file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Pid-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
