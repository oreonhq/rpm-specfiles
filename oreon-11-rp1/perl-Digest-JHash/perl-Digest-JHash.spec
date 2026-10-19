%global source0_hash c746cf0a861a004090263cd54d7728d0c7595a0cf90cbbfd8409b396ee3b0063
Name:           perl-Digest-JHash
Version:        0.10
Release:        33%{?dist}
Summary:        Perl extension for 32 bit Jenkins Hashing Algorithm
License:        Artistic-2.0
URL:            https://metacpan.org/release/Digest-JHash
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Digest::JHash module allows you to use the fast JHash hashing algorithm
developed by Bob Jenkins from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 32-bit
"message digest" of the input in the form of an unsigned long integer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Digest-JHash-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test RELEASE_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
