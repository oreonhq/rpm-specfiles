%global source0_hash 0ab827a513b6e14403184fb065a8ea1d2ebda122d2178cbf45c781f311240eaf

Name:           perl-Curses-UI
Version:        0.9609
Release:        31%{?dist}
Summary:        Curses based OO user interface framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Curses-UI
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDXI/Curses-UI-%{version}.tar.gz
# Support Unicode, bug #2043798, CPAN RT#56695, proposed to the upstream
Patch0:         Curses-UI-0.9609-Use-wide-character-aware-functions.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Curses) >= 1.29
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
Curses::UI is an object-oriented user interface framework for Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Curses-UI-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CREDITS README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
