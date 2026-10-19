%global source0_hash 9a5d2520b3262bf30475272dd764a445f8e7f931bef88be0e3d3bff445da7328
%bcond_without perl_GraphViz_enables_xml
Name:           perl-GraphViz
Version:        2.26
Release:        8%{?dist}
Summary:        Interface to the GraphViz graphing tool
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GraphViz
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/GraphViz-%{version}.tar.gz
Patch0:         GraphViz-2.24-Normalize-shebangs-in-examples.patch
BuildArch:      noarch
Requires:       graphviz
Requires:       perl(Carp) >= 1.01
Requires:       perl(IPC::Run) >= 0.6
Requires:       perl(Parse::RecDescent) >= 1.965001
Requires:       perl(Time::HiRes) >= 1.51
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|IPC::Run|Parse::RecDescent|Time::HiRes|XML::Twig)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides an interface to layout and image generation of
directed and undirected graphs in a variety of formats (PostScript, PNG,
etc.) using the "dot", "neato", "twopi", "circo" and "fdp" programs from
the GraphViz project (<http://www.graphviz.org/>).

%if %{with perl_GraphViz_enables_xml}
%package XML
Summary:        Visualize XML as a tree
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Carp) >= 1.01
Requires:       perl(XML::Twig) >= 3.52
%description XML
GraphViz::XML Perl module makes it easy to visualize XML as a tree. XML
elements are represented as diamond nodes, with links to elements within them.
Character data is represented in round nodes.
%endif

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GraphViz-%{version}
%patch -P0 -p1
find -type f -exec chmod -x {} +

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mv examples/xml.pl ./
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{(as_foo.\d)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/foo.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-GraphViz-XML -f %{oreon_filedir}/perl-GraphViz-XML.list
%files -n perl-GraphViz-tests -f %{oreon_filedir}/perl-GraphViz-tests.list

%changelog

%autochangelog
