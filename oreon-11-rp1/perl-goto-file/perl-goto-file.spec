%global source0_hash c6cdd5ee4a6cdcbdbf314d92a4f9985dbcdf9e4258048cae76125c052aa31f77
Name:           perl-goto-file
Version:        0.005
Release:        19%{?dist}
Summary:        Stop parsing the current file and move on to a different one
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/goto-file
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/goto-file-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::Require::RealFork)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
It is rare, but there are times where you want to swap out the currently
compiling file for a different one. This Perl module does that. From the point
you use the module perl will be parsing the new file instead of the original.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n goto-file-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
