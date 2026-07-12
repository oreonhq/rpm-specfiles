%global source0_hash 67029f20e9b734ac1f483f7175d4ce45f924581c7de8fdf44e20c79be6dc0729

# work around upstream versioning being decimal rather than v-string
%global upstream_version 4.81
%global extraversion %{nil}
%if "%{upstream_version}%{extraversion}" != "%{upstream_version}"
Provides:	perl(IO::AIO) = %{upstream_version}%{extraversion}
%endif

Name:		perl-IO-AIO
Version:	%{upstream_version}%{extraversion}
Release:	7%{?dist}
Summary:	Asynchronous Input/Output
License:	GPL-2.0-or-later
URL:		https://metacpan.org/release/IO-AIO
Source0:	https://cpan.metacpan.org/modules/by-module/IO/IO-AIO-%{upstream_version}.tar.gz
Patch0:		IO-AIO-4.4-shellbang.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Canary::Stability) >= 2001
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(common::sense)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(XSLoader)
# Script Runtime
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Time::HiRes)
# Test Suite
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test)
BuildRequires:	perl(vars)
# Dependencies
Requires:	perl(XSLoader)

# Avoid provides for private shared objects
%{?perl_default_filter}

Provides:       perl(IO::AIO)
%description
This module implements asynchronous I/O using whatever means your operating
system supports.

%package -n treescan
Summary:	Scan directory trees, list directories/files, stat, sync, grep
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	perl(Pod::Usage)

%description -n treescan
The treescan command scans directories and their contents recursively. By
default it lists all files and directories (with trailing /), but it can
optionally do various other things.

If no paths are given, treescan will use the current directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-AIO-%{upstream_version}

# Fix shellbang in treescan
%patch -P 0

%build
PERL_CANARY_STABILITY_NOPROMPT=1 perl Makefile.PL \
	INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/IO::AIO.3*

%files -n treescan
%{_bindir}/treescan
%{_mandir}/man1/treescan.1*

%changelog
%autochangelog
