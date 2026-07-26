%global source0_hash 1b23d3d4c08b9dd3eadfc6a3f38dfd21b72669f0052e7ad18e53350ef47c9e16

Name:       perl-File-RsyncP
Version:    0.76
Release:    23%{?dist}
Summary:    A perl implementation of an Rsync client
# https://fedoraproject.org/wiki/Licensing:FAQ?rd=Licensing/FAQ#What_about_the_RSA_license_on_their_MD5_implementation.3F_Isn.27t_that_GPL-incompatible.3F
License:    GPL-2.0-only AND GPL-3.0-only AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:        https://metacpan.org/release/File-RsyncP
Source0:    https://cpan.metacpan.org/authors/id/C/CB/CBARRATT/File-RsyncP-%{version}.tar.gz
# Adapt a configure check to GCC 12, bug #2046804, CPAN RT#141822
Patch0:     File-RsyncP-0.76-Fix-configure-check-with-optimizing-and-lto-enabled-.patch
Patch1:     perl-File-RsyncP-configure-c99.patch
# Adapt to GCC 15, bug #2341029, CPAN RT#158680, proposed upstream
Patch2:     File-RsyncP-0.76-c23.patch
# Build
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires: perl(AutoLoader)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Path)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Socket)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
# Tests only
# nothing

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/File/
%{perl_vendorarch}/auto/File/
%{_mandir}/man3/File*

%changelog
%autochangelog
