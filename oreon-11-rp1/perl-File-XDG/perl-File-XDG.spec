%global source0_hash 88bd7c1458cb763beced6e7bd0c11972a156b1e39232984f8a7a8be4206bf7ce

Name:           perl-File-XDG
Version:        1.03
Release:        %autorelease
Summary:        Basic implementation of the XDG base directory specification

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-XDG
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-XDG-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Class) > 0.26
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test::More) >= 0.98

%{?perl_default_filter}

%description
This Perl module provides a basic implementation of the XDG base
directory specification as exists by the Free Desktop Organization. It
supports all XDG directories except for the runtime directories, which
require session management support in order to function.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n File-XDG-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
