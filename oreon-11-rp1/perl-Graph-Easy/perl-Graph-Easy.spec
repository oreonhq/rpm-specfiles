%global source0_hash d4a2c10aebef663b598ea37f3aa3e3b752acf1fbbb961232c3dbe1155008d1fa

Name:           perl-Graph-Easy
Version:        0.76
Release:        28%{?dist}
Summary:        Convert or render graphs as ASCII, HTML, SVG or via Graphviz
License:        GPL-2.0-or-later AND Apache-1.1
URL:            https://metacpan.org/release/Graph-Easy
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Graph-Easy-%{version}.tar.gz
Patch0:         graph-easy-undefined-lc.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Getopt::Long)
Requires:       perl(Pod::Usage)

# avoid circular dependencies
%bcond_without bootstrap
%if %{without bootstrap}
BuildRequires:  perl(Graph::Easy::As_svg) >= 0.23
Requires:       perl(Graph::Easy::As_svg) >= 0.23
%endif

# filter unversioned provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Graph::Easy\\)$
%global __provides_exclude %__provides_exclude|perl\\(Graph::Easy::(Edge|Edge::Cell|Group|Node)\\)$

%description
Graph::Easy lets you generate graphs consisting of various shaped nodes
connected by edges (with optional labels). It can read and write graphs in a
variety of formats, as well as render them via its own grid-based layouter.
Since the layouter works on a grid (manhattan layout), the output is most
useful for flow charts, network diagrams, or hierarchy trees.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Graph-Easy-%{version}
%patch -P0 -p 1

chmod 0644 examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc CHANGES README TODO examples
%{_bindir}/graph-easy
%{_mandir}/man1/graph-easy*
%{perl_vendorlib}/Graph*
%{_mandir}/man3/Graph::Easy*

%changelog
%autochangelog
