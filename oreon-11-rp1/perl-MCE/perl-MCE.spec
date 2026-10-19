%global source0_hash 559af28d5310302ca63599e59f0dd76c3247b4523449c2745c5ef159968051a1
Name:           perl-MCE
Version:        1.902
Release:        1%{?dist}
Summary:        Many-core Engine for Perl providing parallel processing capabilities
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MCE
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-%{version}.tar.gz
Patch0:         MCE-1.818-Fix-sharp-bang-line.patch
BuildArch:      noarch
Requires:       perl(File::Path)
Requires:       perl(POSIX)
Requires:       perl(Sereal) >= 3.015
Requires:       perl(Storable) >= 2.04
Requires:       perl(threads::shared)
Provides:       perl(MCE::Grep)
Provides:       perl(MCE)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Many-core Engine (MCE) for Perl helps enable a new level of performance by
maximizing all available cores. MCE spawns a pool of workers and therefore
does not fork a new process per each element of data. Instead, MCE follows
a bank queuing model. Imagine the line being the data and bank-tellers the
parallel workers. MCE enhances that model by adding the ability to chunk
the next n elements from the input stream to the next available worker.

%package tools
Summary:        Many-core Engine command line tools
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       grep, gzip
%description tools
This package delivers command line tools like mce_grep(1) that utilize
the Many-core Engine (MCE) Perl library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MCE-%{version}

# Fix sharp-bang line
%patch -P 0

%build

MCE_INSTALL_TOOLS=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
ln -s mce_grep %{buildroot}%{_bindir}/mce_egrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_fgrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_zgrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_zegrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_zfgrep
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-MCE-tools -f %{oreon_filedir}/perl-MCE-tools.list

%changelog

%autochangelog
