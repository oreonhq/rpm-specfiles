%global source0_hash 0022da5982645d9ef0207f3eb9ef63e70e9713ed2340ed7b3850779b0d842a7d
%global upstream_version 1.201
%global extra_version 0
Name:           perl-Algorithm-Diff
Version:        %{upstream_version}%{?extra_version}
Release:        15%{?dist}
Summary:        Compute 'intelligent' differences between two files/lists
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-Diff
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Algorithm-Diff-1.201.tar.gz
Patch0:         Algorithm-Diff-1.1903-provides.patch
BuildArch:      noarch
Requires:       perl(Carp)
Provides:       perl(Algorithm::Diff)
Provides:       perl(Algorithm::DiffOld)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a module for computing the difference between two files, two strings,
or any other two lists of things. It uses an intelligent algorithm similar to
(or identical to) the one used by the Unix "diff" program. It is guaranteed to
find the *smallest possible* set of differences.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Algorithm-Diff-%{upstream_version}

# Generate provide for perl(Algorithm::DiffOld)
%patch -P0

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{upstream_version}%{?extra_version}-15
- Prepare for Oreon 11 (RP1)
