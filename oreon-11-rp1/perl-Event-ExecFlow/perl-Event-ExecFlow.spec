%global source0_hash c4e9f4e764216efa5e2b9efe90a6582b81cb8aed4c138b4bad747ed3bd16b7bf
%global pkgname Event-ExecFlow
Name:           perl-Event-ExecFlow
Version:        0.64
Release:        1%{?dist}
Summary:        High level API for event-based execution flow control
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND LGPL-2.1-or-later
URL:            https://metacpan.org/release/Event-ExecFlow
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRED/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Event::ExecFlow offers a high level API to declare jobs, which mainly execute
external commands, parse their output to get progress or other status
information, triggers actions when the command has been finished etc. Such jobs
can be chained together in a recursive fashion to fulfill rather complex tasks
which consist of many jobs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

# Convert encoding
for f in $(find lib/ -name *.pm) README ; do
cp -p ${f} ${f}.noutf8
iconv -f ISO-8859-1 -t UTF-8 ${f}.noutf8 > ${f}
touch -r ${f}.noutf8 ${f}
rm ${f}.noutf8
done

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod 0755 %{buildroot}%{_bindir}/execflow
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
