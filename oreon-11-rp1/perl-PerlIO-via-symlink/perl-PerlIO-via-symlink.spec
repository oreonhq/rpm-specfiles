%global source0_hash 4107d4c34a6a3629453448c25695d92f82522aff64e29b716b56a5af586b2d52

Name:           perl-PerlIO-via-symlink
Version:        0.05
Release:        51%{?dist}
Summary:        PerlIO layers for create symlinks
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-via-symlink
Source0:        https://cpan.metacpan.org/modules/by-module/PerlIO/PerlIO-via-symlink-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Run-time:
BuildRequires:  perl(Errno)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

%description
The PerlIO layer symlink allows you to create a symbolic link by writing to
the file handle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlIO-via-symlink-%{version}
# Remove bundled modules, CPAN RT#86016
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
