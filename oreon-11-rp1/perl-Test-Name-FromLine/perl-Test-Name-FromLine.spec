%global source0_hash cee6cc18f6f46f37fe4437130bad4e740df79818683f13f922763c0e9c5c6378

Name:           perl-Test-Name-FromLine
Summary:        Automatically name tests from their source code
Version:        0.13
Release:        33%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Name-FromLine

Source0:        https://cpan.metacpan.org/authors/id/S/SA/SATOH/Test-Name-FromLine-%{version}.tar.gz

BuildArch:      noarch

# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder)
# test requirements
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)

%{?perl_default_filter}

%description
Test::Name::FromLine is a testing helper that automatically names each unit
test from its source code declaration, unless it was explicitly named.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Name-FromLine-%{version}

# Remove bundled build requirements
/usr/bin/rm -fr inc
/usr/bin/sed -i '/^inc\//d' MANIFEST

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::Name::FromLine*

%changelog
%autochangelog
