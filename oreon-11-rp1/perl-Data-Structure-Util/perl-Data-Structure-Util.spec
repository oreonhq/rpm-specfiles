%global source0_hash 9cd42a13e65cb15f3a76296eb9a134da220168ec747c568d331a50ae7a2ddbc6
Name:           perl-Data-Structure-Util
Version:        0.16
Release:        1%{?dist}
Summary:        Change nature of data within a structure
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Structure-Util
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDYA/Data-Structure-Util-%{version}.tar.gz
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Data::Structure::Util is a toolbox to manipulate the data inside a data
structure. It can process an entire tree and perform the operation
requested on each appropriate element.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Structure-Util-%{version}
chmod 644 -c CHANGES README bin/packages.pl
rm -r inc && sed -e '/^inc.*$/d' -i MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_bindir}/packages.pl \
      %{buildroot}%{_mandir}/man1/packages.pl*
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
