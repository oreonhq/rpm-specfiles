%global source0_hash d35cd95fef57fd4dfd8831f62c34e294d7c4b861fc909e02b76071739d52d341
Name:           perl-File-Type
Version:        0.22
Release:        1%{?dist}
Summary:        Determine file type using magic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Type
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMISON/File-Type-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(File::Type)
# oreon:deps
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::Type uses magic numbers (typically at the start of a file) to
determine the MIME type of that file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-Type-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
