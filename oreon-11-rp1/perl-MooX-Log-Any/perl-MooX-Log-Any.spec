%global source0_hash 2a1afa0f3a411e28a9258ccabe2c5b5d647abc29f2fbf5be9ffaf2286e830534
Name:           perl-MooX-Log-Any
Version:        0.004004
Release:        1%{?dist}
Summary:        A Moose role to add support for logging via Log::Any
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Log-Any
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAZADOR/MooX-Log-Any-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A logging role building a very lightweight wrapper to Log::Any for use with
your Moo or Moose classes. Connecting a Log::Any::Adapter should be
performed prior to logging the first log message, otherwise nothing will
happen, just like with Log::Any

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Log-Any-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
