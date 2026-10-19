%global source0_hash ff20713d1a14d257af9c78209001f40dc177e4b9d1496115cbd8726d577946c7
%bcond_with perl_Path_Tiny_enables_optional_test
Name:		perl-Path-Tiny
Version:	0.150
Release:        1%{?dist}
Summary:        File path utility
License:	Apache-2.0
URL:		https://metacpan.org/release/Path-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Path_Tiny_enables_optional_test}
%endif
Requires:	perl(Cwd)
Requires:	perl(Digest) >= 1.03
Requires:	perl(Digest::SHA) >= 5.45
Requires:	perl(Encode)
Requires:	perl(Fcntl)
Requires:	perl(File::Compare)
Requires:	perl(File::Copy)
Requires:	perl(File::Glob)
Requires:	perl(File::Path) >= 2.07
Requires:	perl(File::stat)
Requires:	perl(File::Temp) >= 0.18
Requires:	perl(threads)
Requires:	perl(warnings::register)
Requires:	perl(Unicode::UTF8) >= 0.58
Provides:       perl(Path::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::UTF8)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module attempts to provide a small, fast utility for working with file
paths. It is friendlier to use than File::Spec and provides easy access to
functions from several other core file handling modules.

It doesn't attempt to be as full-featured as IO::All or Path::Class, nor does
it try to work for anything except Unix-like and Win32 platforms. Even then, it
might break if you try something particularly obscure or tortuous.

All paths are forced to have Unix-style forward slashes. Stringifying the
object gives you back the path (after some clean up).

File input/output methods flock handles before reading or writing, as
appropriate.

The *_utf8 methods (slurp_utf8, lines_utf8, etc.) operate in raw mode without
CRLF translation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Path-Tiny-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.150-3
- Prepare for Oreon 11 (RP1)
