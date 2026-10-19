%global source0_hash d5852a78a1393e6a51a14a1456afb8cd75142c509468716a5acba87e4d0f7b58
Name:           perl-User-Utmp
Version:        1.8
Release:        44%{?dist}
Summary:        Perl access to utmp- and utmpx-style databases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/User-Utmp
Source0:        https://cpan.metacpan.org/authors/id/M/MP/MPIOTR/User-Utmp-%{version}.tar.gz
Patch0:         User-Utmp-1.8-strlen.patch
Patch1:         User-Utmp-1.8-Make-hints-scripts-strict-conformant.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
UNIX systems record information about current and past log-ins in a user
accounting database. This database is realized by two files: File utmpx
contains a record of all users currently logged onto the system, while file
wtmpx contains a record of all log-ins and log-outs. Some systems (such as
HP-UX and AIX) also maintain a third file containing failed log-in attempts.
The information in these files is used by commands such as who(1), last(1),
write(1), or login(1).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n User-Utmp-%{version}
%patch -P0 -p0
%patch -P1 -p1
chmod -x example.pl
sed -i -e '1 s/^#!.*//' -e '1 ause utf8;' example.pl
for F in example.pl README; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "${F}"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
