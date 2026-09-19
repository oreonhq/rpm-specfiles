%global source0_hash d0b0718e0840bd8ab0c9aac2ea8cafc98de68a67aebb7bc267a5d5b1d2b95951

Name:           perl-Parallel-Scoreboard
Version:        0.08
Release:        28%{?dist}
Summary:        Scoreboard for monitoring status of many processes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parallel-Scoreboard
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Parallel-Scoreboard-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::More)

# Run-time deps
BuildRequires: perl(Class::Accessor::Lite)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Path)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(JSON)
BuildRequires: perl(POSIX)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(Module::Install::ReadmeFromPod)

%description
Parallel::Scoreboard is a pure-perl implementation of a process scoreboard.
By using the module it is easy to create a monitor for many worker process,
like the status module of the Apache HTTP server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parallel-Scoreboard-%{version}
rm -r inc
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
