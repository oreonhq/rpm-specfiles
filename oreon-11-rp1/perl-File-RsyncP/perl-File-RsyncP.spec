%global source0_hash 1b23d3d4c08b9dd3eadfc6a3f38dfd21b72669f0052e7ad18e53350ef47c9e16
Name:       perl-File-RsyncP
Version:    0.76
Release:        23%{?dist}
Summary:        A perl implementation of an Rsync client
License:    GPL-2.0-only AND GPL-3.0-only AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:        https://metacpan.org/release/File-RsyncP
Source0:        https://cpan.metacpan.org/authors/id/C/CB/CBARRATT/File-RsyncP-%{version}.tar.gz
Patch0:     File-RsyncP-0.76-Fix-configure-check-with-optimizing-and-lto-enabled-.patch
Patch1:     perl-File-RsyncP-configure-c99.patch
Patch2:     File-RsyncP-0.76-c23.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Socket)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::RsyncP is a perl implementation of an Rsync client. It is compatible with
Rsync 2.5.5 - 2.6.3 (protocol versions 26-28). It can send or receive files,
either by running rsync on the remote machine, or connecting to an rsyncd
daemon on the remote machine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n File-RsyncP-%{version}
# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/redhat/config.* FileList/

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_flags}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
