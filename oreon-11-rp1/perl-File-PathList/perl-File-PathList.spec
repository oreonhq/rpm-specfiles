%global source0_hash e3e2799f3bceeae4992fe31ea892c34e9141f9237598cfadbc89824ede7a662c
Name:           perl-File-PathList
Version:        1.04
Release:        1%{?dist}
Summary:        Find a file within a set of paths (like @INC or Java classpaths)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-PathList
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/File-PathList-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Params::Util) >= 0.24
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Params::Util)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
