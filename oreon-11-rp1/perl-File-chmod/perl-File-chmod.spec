%global source0_hash 6cafafff68bc84215168b55ede0d191dcb57f9a3201b51d61edb2858a2407795

Name:           perl-File-chmod
Version:        0.42
Release:        34%{?dist}
Summary:        Implements symbolic and ls chmod modes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-chmod
Source0:        https://cpan.metacpan.org/authors/id/X/XE/XENO/File-chmod-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# tests
BuildRequires:  perl(blib)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-chmod-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w %{buildroot}/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
