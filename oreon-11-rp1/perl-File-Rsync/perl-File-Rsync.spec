%global source0_hash dd995df485f7334796d242efa277586d38d2544cace6ca0c3629a225df1e42d8
Name:           perl-File-Rsync
Version:        0.49
Release:        1%{?dist}
Summary:        Perl module interface to rsync
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/File-Rsync/
Source0:        http://www.cpan.org/authors/id/L/LE/LEAKIN/File-Rsync-%{version}.tar.gz
BuildArch:      noarch
Requires:       rsync
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  rsync
# /oreon:deps
%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-
2.3.2 and updated for rsync-3.1.1 but should perform properly with most
recent versions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Rsync-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
