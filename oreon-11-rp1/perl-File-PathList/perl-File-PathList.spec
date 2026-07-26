%global source0_hash e3e2799f3bceeae4992fe31ea892c34e9141f9237598cfadbc89824ede7a662c

Name:           perl-File-PathList
Version:        1.04
Release:        43%{?dist}
Summary:        Find a file within a set of paths (like @INC or Java classpaths)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-PathList
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/File-PathList-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.76
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Params::Util) >= 0.24
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Params::Util) >= 0.24

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Params::Util)\\)$

%description
Many systems that map generic relative paths to absolute paths do so with a
set of base paths. For example, perl itself when loading classes first turn
a "Class::Name" into a path like "Class/Name.pm", and then looks through each
element of @INC to find the actual file. To aid in portability, all relative
paths are provided as UNIX-style relative paths, and converted to the
localized version in the process of looking up the path.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-PathList-%{version}
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
