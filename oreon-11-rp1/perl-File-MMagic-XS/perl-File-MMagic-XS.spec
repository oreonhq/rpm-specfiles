%global source0_hash a9db0db6c5530ca63d1e248cae0b45b6dcd72d2838070fdef9443cbe056cd372
%global optflags %{optflags} -std=gnu17
Name:           perl-File-MMagic-XS
Version:        0.09008
Release:        1%{?dist}
Summary:        Guess file type with XS
License:        Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/File-MMagic-XS
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/File-MMagic-XS-%{version}.tar.gz
Patch0:         File-MMagic-XS-0.09006-qw-does-not-produce-array-context-anymore.patch
Patch1:		perl-File-MMagic-XS-format-security.patch
Patch2:         File-MMagic-XS-0.09008-Fix-building-on-Perl-without-dot-in-INC.patch
Requires:       perl(File::MMagic)
Requires:       perl(File::Spec)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a port of Apache2 mod_mime_magic.c in Perl, written in XS with the aim 
of being efficient and fast especially for applications that need to be run for
an extended amount of time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-MMagic-XS-%{version}
# Merged in 0.09008
# %%patch0 -p1
%patch -P1 -p1 -b .format-security
%patch -P2 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
