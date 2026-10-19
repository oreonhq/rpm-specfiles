%global source0_hash 51da6ff71519470a173ad0f81db2db8e508c3e0322c5f24f691efeb5e42104d5
Name:           perl-FileHandle-Fmode
Version:        0.15
Release:        1%{?dist}
Summary:        Determine whether a filehandle is opened for reading, writing, or both
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/FileHandle-Fmode
Source0:        https://cpan.metacpan.org/modules/by-module/FileHandle/FileHandle-Fmode-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(FileHandle::Fmode)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Determine whether a filehandle is opened for reading, writing, or both.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n FileHandle-Fmode-%{version}

# Tarball probably made on Windows
chmod -c -x CHANGES Fmode.pm Fmode.xs Makefile.PL MANIFEST README

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
