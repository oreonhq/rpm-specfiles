%global source0_hash 1fda712d4ba5e1868159ed35f6f8efbfae9d435d6376f5606d533bcb080555a4

Name:           perl-Filesys-Notify-Simple
Summary:        Simple and dumb file system watcher
Version:        0.14
Release:        19%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-%{version}.tar.gz 
URL:            https://metacpan.org/release/Filesys-Notify-Simple
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Linux::Inotify2)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)

Requires:       perl(File::Find)
Requires:       perl(Linux::Inotify2)

%{?perl_default_filter}

%description
Filesys::Notify::Simple is a simple but unified interface to get
notifications of changes to a given filesystem path.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Filesys-Notify-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
