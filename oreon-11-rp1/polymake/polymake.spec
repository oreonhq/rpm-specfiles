%global source0_hash 30e0a8f89013cf7a9a44ed90db2f69c49bf181050664c7e6bdb861c610b1bdb9
%undefine _hardened_build
%undefine _strict_symbol_defs_build
%bcond jreality 0
Name:           polymake
Version:        4.15
Release:        1%{?dist}
License:        GPL-2.0-or-later AND MIT AND MPL-2.0 AND BSD-3-Clause AND Apache-2.0
Summary:        Algorithms on convex polytopes and polyhedra
URL:            https://polymake.org/
VCS:            git:https://github.com/polymake/polymake.git
Source0:        https://polymake.org/lib/exe/fetch.php/download/%{name}-%{version}-minimal.tar.bz2
Source1:        %{name}.1
Patch:          %{name}-fedora.patch
Patch:          %{name}-no-hardening.patch
Patch:          %{name}-latte.patch
Patch:          %{name}-no-gold.patch
Patch:          %{name}-name-clash.patch
Patch:          %{name}-prefix.patch
Patch:          %{name}-soplex.patch
Patch:          %{name}-Singular-4.3.2.patch
Patch:          %{name}-sympol.patch
ExcludeArch:    %{ix86}
%if %{with jreality}
%endif
%if %{with jreality}
%endif
Requires:       boost-devel%{?_isa}
Requires:       cddlib-devel%{?_isa}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
%if %{with jreality}
Requires:       java
Requires:       javapackages-tools
%endif
Requires:       gcc-c++
Requires:       glibc-devel%{?_isa}
Requires:       libgcc%{?_isa}
Requires:       libnormaliz-devel%{?_isa}
Requires:       make
Requires:       mpfr-devel%{?_isa}
Requires:       ninja-build
Requires:       perl-interpreter = 4:%{?perl_version}%{!?perl_version:0}
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       permlib-devel
Requires:       ppl-devel%{?_isa}
Recommends:     4ti2
Recommends:     azove
Recommends:     gfan
Recommends:     latte-integrale
Recommends:     normaliz
Recommends:     plantri
Recommends:     qhull
Recommends:     Singular
Recommends:     TOPCOM
Recommends:     vinci
Suggests:       evince
Suggests:       geomview
Suggests:       graphviz
Suggests:       gv
Suggests:       okular
Suggests:       sketch
Provides:       perl(PolyDB::JsonIO)
Provides:       perl(Polymake::ConfigureStandalone)
Provides:       perl(Polymake::Namespaces)
Provides:       perl(Polymake::file_utils.pl)
Provides:       perl(Polymake::regex.pl)
Provides:       perl(Polymake::utils.pl)
Provides:       bundled(sympol) = 0.1.9
%global __provides_exclude perl\\\(Geomview.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Graphviz.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(JSON.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Metapost.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(PerlIO.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Postscript.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Povray.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Sage\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(Sketch.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(SplitsTree.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(ThreeJS.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(TikZ.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(X3d.*\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(application\\\)
%global __provides_exclude %{__provides_exclude}|perl\\\(namespaces\\\)
%global __requires_exclude perl\\\(namespaces.*\\\)
%global majver  %{gsub %version ^(%d*)r.*$ %1}
# oreon:deps
BuildRequires:  4ti2
BuildRequires:  TOPCOM
BuildRequires:  azove
BuildRequires:  boost-devel
BuildRequires:  cddlib-devel
BuildRequires:  cmake
BuildRequires:  cmake(scip)
BuildRequires:  cmake(soplex)
BuildRequires:  doxygen
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  libnormaliz-devel
BuildRequires:  lrslib-devel
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(SVG)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  permlib-devel
BuildRequires:  pkgconfig(Singular)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libmongoc-1.0)
BuildRequires:  pkgconfig(libnauty)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  ppl-devel
BuildRequires:  qhull
BuildRequires:  vinci
BuildRequires:  xhtml1-dtds
# /oreon:deps
%description
Polymake is a tool to study the combinatorics and the geometry of convex
polytopes and polyhedra.  It is also capable of dealing with simplicial
complexes, matroids, polyhedral fans, graphs, tropical objects, and so forth.

Polymake can use various computational packages if they are installed.  Those
available from Fedora are: 4ti2, azove, gfan, latte-integrale, normaliz,
qhull, Singular, TOPCOM, and vinci.

Polymake can interface with various visualization packages if they are
installed.  Install one or more of the tools from the following list: evince,
geomview, graphviz, gv, and okular.

%package        doc
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{majver}

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Help polymake find the 4ti2 tools
sed -i.orig '/global variables/i\$ENV{'PATH'} = \"\$ENV{PATH}:%{_libdir}/4ti2/bin\";\n' perl/polymake
fixtimestamp perl/polymake

# The Fedora normaliz library is not linked with libsha256
sed -i '/NMZ_HASHLIBRARY/,+2d' bundled/libnormaliz/support/configure.pl

# Fix nauty detection
sed -i 's,@@LIBDIR@@,%{_libdir},' bundled/nauty/support/configure.pl

# Build verbosely.  Avoid parallelism, which often leads to resource exhaustion.
sed -i 's,\${NINJA},& -j 1 -v,' Makefile

# Avoid obsolescence warnings
sed -i 's/fgrep/grep -F/' perllib/Polymake/ConfigureStandalone.pm

%build

export CFLAGS='%{build_cflags} -I%{_includedir}/eigen3 -I%{_includedir}/gfanlib -I%{_includedir}/nauty -Wno-unused-local-typedefs'
export CXXFLAGS='%{build_cxxflags} -I%{_includedir}/eigen3 -I%{_includedir}/gfanlib -I%{_includedir}/nauty -Wno-unused-local-typedefs'
export LDFLAGS='%{build_ldflags} -lnormaliz -ldl'
export Arch=%{_arch}
./configure --build=%{_arch} --prefix=%{_prefix} --libdir=%{_libdir} \
  --libexecdir=%{_libdir}/%{name} \
  --without-native \
  --with-cdd-include=%{_includedir}/cddlib/ \
  --with-cdd-lib=%{_libdir} \
  --with-flint=%{_prefix} \
  --with-libnormaliz=%{_prefix} \
  --with-lrs=%{_prefix} \
  --with-nauty-src=%{_prefix} \
  --with-permlib=%{_prefix} \
  --with-ppl=%{_prefix} \
  --with-scip=%{_prefix} \
  --with-singular=%{_prefix} \
  --with-soplex=%{_prefix} \
  --with-sympol=bundled \
  %{?with_jreality:--with-java=%{java_home}}%{!?with_jreality:--without-java} \
  --without-javaview
sed -e 's|-Wl,-z,now|-Wl,-z,lazy|g' \
    -e 's/-lpthread -shared/-shared/g' \
    -i build.%{_arch}/config.ninja
make all
%install
export Arch=%{_arch}
%make_install
mkdir ../xml
ln -s $PWD/xml/documentation/PTL-docs ../xml/documentation
ln -s build.%{_arch} build
mkdir doc
perl/polymake --script doxygen doc
mkdir -p %{buildroot}%{_mandir}/man1
sed "s/@VERSION@/%{version}/" %{SOURCE1} > %{buildroot}%{_mandir}/man1/%{name}.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
rm -fr %{buildroot}%{_datadir}/%{name}/apps/*/src
chmod -R u+w %{buildroot}%{_prefix}
rm -fr %{buildroot}%{_datadir}/%{name}/resources/{JuPyMake,jupyter-polymake}
sed -e '/^CFLAGS/s@%{build_cflags}@%{extension_cflags}@' \
    -e '/^CXXFLAGS/s@%{build_cxxflags}@%{extension_cxxflags}@' \
    -e '/^LDFLAGS/s@%{build_ldflags}@%{extension_ldflags}@' \
    -e '/^LDsharedFLAGS/s@-Wl,-z,relro.*@%{extension_ldflags}@' \
    -e '/^LDcallableFLAGS/s@-Wl,-z,relro.*@%{extension_ldflags}@' \
    -i %{buildroot}%{_libdir}/%{name}/config.ninja
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export COLUMNS=80
export LINES=25
make test
%files -f %{oreon_filedir}/main.list
%files -n polymake-doc -f %{oreon_filedir}/polymake-doc.list

%changelog

%autochangelog
