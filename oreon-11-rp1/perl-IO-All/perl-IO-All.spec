%global source0_hash 54e21d250c0229127e30b77a3461e10077854ec244f26fb670f1b445ed4c4d5b
%bcond_without perl_IO_All_enables_mldbm
%bcond_without perl_IO_All_enables_optional_test
%bcond_without perl_IO_All_enables_extra_test
Name:           perl-IO-All
Version:        0.87
Release:        1%{?dist}
Summary:        IO::All Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-All
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/IO-All-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_IO_All_enables_mldbm}
%endif
%if %{with perl_IO_All_enables_optional_test}
%endif
%if %{with perl_IO_All_enables_extra_test}
%endif
Requires:       perl(File::Copy)
Requires:       perl(File::MimeInfo)
Requires:       perl(File::Path)
Requires:       perl(File::ReadBackwards)
Requires:       perl(IO::Handle)
%if %{with perl_IO_All_enables_mldbm}
Recommends:     perl(MLDBM)
%endif
Requires:       perl(Tie::File)
Requires:       perl(warnings)
Provides:       perl(IO::All)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::MimeInfo)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ReadBackwards)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(MLDBM)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::File)
BuildRequires:  perl(base)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The IO::All object is a proxy for IO::File, IO::Dir, IO::Socket,
IO::String, Tie::File, File::Spec, File::Path and File::ReadBackwards; as
well as all the DBM and MLDBM modules. You can use most of the methods
found in these classes and in IO::Handle (which they inherit from). IO::All
adds dozens of other helpful idiomatic methods including file stat and
manipulation functions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-All-%{version}
find -type f -perm /0100 -name '*.pm' -exec chmod -c a-x {} \;

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%if %{with perl_IO_All_enables_extra_test}
RELEASE_TESTING=1
%else
unset RELEASE_TESTING
%endif
make %{?_smp_mflags} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.87-26
- Prepare for Oreon 11 (RP1)
