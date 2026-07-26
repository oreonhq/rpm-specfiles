%global source0_hash bf88873248ef88cc5e68ed074493496be684ec334e11273d4654306dd9dae485

Name:           perl-POSIX-strftime-Compiler
Version:        0.46
Release:        7%{?dist}
Summary:        GNU C library compatible strftime for loggers and servers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POSIX-strftime-Compiler
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.008004
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
POSIX::strftime::Compiler provides GNU C library compatible strftime(3).
But this module will not affected by the system locale. This feature is
useful when you want to write loggers, servers and portable applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POSIX-strftime-Compiler-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
