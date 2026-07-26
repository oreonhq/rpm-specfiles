%global source0_hash 786698225e5cb43e8f061b78cfac1e0e7d48d370034ffdc518255207741c0b2a

Name:           perl-File-Sync
Version:        0.11
Release:        39%{?dist}
Summary:        Perl access to fsync() and sync() function calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Sync
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/File-Sync-%{version}.tar.gz
Patch0:         File-Sync-UTF8.patch
# Module Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
# Module Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(POSIX)
# Runtime

%description
The fsync() function takes a Perl file handle as its only argument, and
passes its fileno() to the C function fsync(). It returns undef on failure,
or true on success.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Sync-%{version}

# re-code documentation as UTF-8
%patch -P0

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/File/
%{perl_vendorarch}/File/
%{_mandir}/man3/File::Sync.3pm*

%changelog
%autochangelog
