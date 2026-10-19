%global source0_hash 9b2d4390b5de6b0cf4558e4ad04317a73c5e13dd19af29149c4e47c37fb2423b
Name:           perl-Stream-Buffered
Version:        0.03
Release:        1%{?dist}
Summary:        Temporary buffer to save bytes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Stream-Buffered
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Stream-Buffered-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Stream::Buffered is a buffer class to store arbitrary length of byte
strings and then get a seekable filehandle once everything is buffered. It
uses PerlIO and/or temporary file to save the buffer depending on the
length of the size.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Stream-Buffered-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=-1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
