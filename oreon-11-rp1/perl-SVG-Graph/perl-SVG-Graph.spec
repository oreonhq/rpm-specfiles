%global source0_hash 02aa78f5f4912837d56ad885730377c17f3154823296e99fbc0d529a0d483dac
Name:           perl-SVG-Graph
Version:        0.04
Release:        1%{?dist}
Summary:        Visualize your data in Scalable Vector Graphics (SVG) format
License:        Artistic-2.0
URL:            https://metacpan.org/release/SVG-Graph
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJFIELDS/SVG-Graph-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Statistics::Descriptive) >= 2.6
Requires:       perl(SVG) >= 2.27
Requires:       perl(Tree::DAG_Node) >= 1.04
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Statistics::Descriptive|SVG|Tree::DAG_Node)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Math::Spline)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(SVG)
BuildRequires:  perl(Statistics::Descriptive)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tree::DAG_Node)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
SVG::Graph is a suite of perl modules for plotting data. SVG::Graph
currently supports plots of one-, two- and three-dimensional data, as well
as N-ary rooted trees.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVG-Graph-%{version}

# remove all execute bits from eg subdirectory
find eg -type f -exec chmod -x {} 2>/dev/null ';'

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
