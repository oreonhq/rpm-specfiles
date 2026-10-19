%global source0_hash 68f49de6a41c153ddc735da81c6b4dd5dd26e15c2b3f7968286d6c1429b152fa
Name:           perl-CSS-Tiny
Version:        1.20
Release:        1%{?dist}
Summary:        Read/Write .css files with as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CSS-Tiny
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/CSS-Tiny-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Clone)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Clone)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
%description
CSS::Tiny is a perl class to read and write .css style-sheets with as
little code as possible, reducing load time and memory overhead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CSS-Tiny-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
