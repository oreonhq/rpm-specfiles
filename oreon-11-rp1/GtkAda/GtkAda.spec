%global source0_hash 930a72ca08f02b1b4a1ff7b8aeef1b0328547bc8f82a41fb390dbcad93b55072

Name:           GtkAda
Version:        2.24.2
Release:        56%{?dist}
Summary:        GTKada 2, an Ada binding to GTK+ 2
Summary(sv):    GTKada 2, en adabindning till GTK+ 2
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
# Adacore released this version with the GNAT exception removed from the Ada
# files, but the C files kept the LGPL. Thus only GPL-compatible code may link
# to this version of GTKada, but if somebody wanted to extract the C files and
# link only those into their program, then they wouldn't be required to apply
# the GPL to that program.

URL:            https://github.com/AdaCore/gtkada
# The release tarball is no longer available for downloading, but the source
# code should be possible to find at Github as the version history has been
# imported there.
Source:         gtkada-gpl-%{version}-src.tgz
# Patch for a more flexible build system, proposed upstream 2011-02-14:
# http://lists.adacore.com/pipermail/gtkada/2011-February/003969.html
Patch:          GtkAda-2.24.2-configuration-5.patch
# Patch to make project files use fedora-gnat-project-common:
Patch:          GtkAda-2.14.1-multilib_gpr.patch
# Fedora-specific patch to make gtkada-config use uname:
Patch:          GtkAda-2.14.1-multilib_gtkada-config.patch
# Patch to fix implicit DSO linking, proposed upstream 2010-02-16:
# http://lists.adacore.com/pipermail/gtkada/2010-February/003871.html
Patch:          GtkAda-2.18.0-lm.patch
# Hack to get libgtkada_gl in the right place:
Patch:          GtkAda-2.18.0-gl_placement.patch
# GNU-specific patch to avoid link bloat:
Patch:          GtkAda-2.18.0-link_as_needed.patch
# Patch to avoid conflicts where two project files claim the same source files,
# fixed upstream 2012-08-07:
# http://lists.adacore.com/pipermail/gtkada/2012-August/004175.html
Patch:          GtkAda-2.24.2-source_dir.patch
# "Only <glib.h> can be included directly." (said to be fixed upstream):
Patch:          GtkAda-2.18.0-no_include_gmain.patch
# Patch to remove obsolete manpage cross-references, proposed upstream 2012-07-27:
# http://lists.adacore.com/pipermail/gtkada/2012-July/004160.html
Patch:          GtkAda-2.24.2-man_xref.patch
# Fix abuse of printf-style format strings:
Patch:          GtkAda-2.24.2-format_security.patch
# "extern inline" doesn't seem to work in GCC 5:
Patch:          GtkAda-2.24.2-no_extern_inline.patch
# Build with GPRbuild:
Patch:          GtkAda-2.24.2-gprbuild.patch
# Show the link commands:
Patch:          GtkAda-2.24.2-unmask.patch
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  gtk2-devel >= 2.21
BuildRequires:  libgnome-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  libbonobo-devel
BuildRequires:  libbonoboui-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  GConf2-devel
BuildRequires:  fedora-gnat-project-common >= 3
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  recode
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
%{name} is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.

%global common_description_sv \
%{name} är en adabindning till den grafiska verktygslådan GTK+. Med %{name} \
kan du utveckla grafiska användargränssnitt i ada baserade på GTK+.

%description %{common_description_en}

This is a compatibility package of GTKada 2. See also the GtkAda3 package.

%description -l sv %{common_description_sv}

Detta är ett kompatibilitetspaket med GTKada 2. Se även paketet GtkAda3.

%package devel
Summary:        Development files for GTKada 2
Summary(sv):    Filer för programmering med GTKada 2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gnome%{?_isa} = %{version}-%{release}
Requires:       %{name}-gl%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common >= 2
# gtkada.pc requires gtk+-2.0, maybe incorrectly.
Requires:       gtk2-devel%{?_isa}
Recommends:     %{name}-doc
Conflicts:      GtkAda3-devel

# GTKada 3.x is packaged as GtkAda3, and this is now a compatibility package.
#
# Unlike GTK+, GTKada has no support for installing two versions side by side,
# other than dumping the entire directory tree under some nonstandard prefix
# and requiring users to mess with various environment variables. Despite the
# API incompatibilities, both versions use the filenames "gtkada.gpr" and
# "gtkada-config", and directories named "gtkada".
#
# Hacking the build system to change various filenames from "gtkada" to
# "gtkada3" would be more trouble than it's worth, and would make Fedora
# incompatible with everything that uses GTKada. Both developers and packagers
# would have to do special things to select the right version of the library.
#
# Therefore GtkAda-devel and GtkAda3-devel are allowed to conflict.

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use GTKada 2 to bind to GTK+ 2.x. See also
GtkAda3-devel.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder GTKada 2 för att binda till GTK+ 2.x. Se
även GtkAda3-devel.

%package gnome
Summary:        GTKada 2 binding to Gnome's GUI libraries
Summary(sv):    GTKada 2:s bindning till Gnomes GUI-bibliotek
License:        GPL-2.0-or-later
# None of the LGPL-licensed C files are in the subdirectory "gnome".
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gnome %{common_description_en}

The %{name}-gnome package contains the GTKada 2 binding to Gnome's graphical
user interface libraries.

%description gnome -l sv %{common_description_sv}

Paketet %{name}-gnome innehåller GTKada 2:s bindning till Gnomes bibliotek för
grafiska användargränssnitt.

%package gl
Summary:        GTKada 2 binding to OpenGL
Summary(sv):    GTKada 2:s bindning till OpenGL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gl %{common_description_en}

The %{name}-gl package contains the GTKada 2 binding to the OpenGL interface.

%description gl -l sv %{common_description_sv}

Paketet %{name}-gl innehåller GTKada 2:s bindning till OpenGL-gränssnittet.

%package doc
Summary:        Documentation for GTKada 2
Summary(sv):    Dokumentation till GTKada 2
BuildArch:      noarch
License:        GFDL-1.1-invariants-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later
# GFDL 1.1 applies to the User's Guide.
# The reference manual has been generated from the source code, and presumably
# inherits its license.
# The example code files are licensed like the library itself.

%description doc %{common_description_en}

The %{name}-doc package contains the documentation for GTKada 2.

%description doc -l sv %{common_description_sv}

Paketet %{name}-doc innehåller dokumentationen till GTKada 2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 0 -n gtkada-%{version}-src
find -name .cvsignore | xargs rm -fr

# Transcode the author's name in comments in two source files.
recode ISO-8859-1..UTF-8 testgtk/opengl/lw.[hc]

%build
# This package triggers a GCC failure when building with LTO.  Disable
# LTO for now.  fld_incomplete_type_of, at tree.c:5371
%define _lto_cflags %{nil}

LDFLAGS="${LDFLAGS} -Wl,--no-warn-execstack"
%{configure} --enable-build=Debuginfo --disable-subdirs --disable-static
make src "GPRbuild_optflags=%{GPRbuild_flags}"

# The documentation is not regenerated because that requires GPS and would
# cause a dependency loop.

%install
%{make_install} gprdir=%{_GNAT_project_dir}

# Also install the gtkada-config manpage.
mkdir -p %{buildroot}%{_mandir}/man1
install --mode=u=rw,go=r,a-s --preserve-timestamps docs/gtkada-config.1 %{buildroot}%{_mandir}/man1

# Put the info documentation in the right place.
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_docdir}/gtkada/gtkada_ug/gtkada_ug.info --target-directory=%{buildroot}%{_infodir}

# Put the examples in the documentation directory, excluding binaries.
mv --no-target-directory %{buildroot}%{_datadir}/examples/gtkada %{buildroot}%{_docdir}/gtkada/examples

# Include these documentation files.
install --mode=u=rw,go=r,a-s --preserve-timestamps AUTHORS README features known-problems %{buildroot}%{_docdir}/gtkada
mkdir --parents %{buildroot}%{_licensedir}/gtkada
install --mode=u=rw,go=r,a-s --preserve-timestamps COPYING %{buildroot}%{_licensedir}/gtkada
# There is a COPYING3 in the 2.24.2 tarball, but the source files' headers say
# version 2 or later, so COPYING3 is left out of the package for now.

%files
%{_libdir}/libgtkada-*.so.*
%license %{_licensedir}/gtkada
%dir %{_docdir}/gtkada
%{_docdir}/gtkada/AUTHORS
%{_docdir}/gtkada/README

%files gnome
%{_libdir}/libgnomeada-*.so.*

%files gl
%{_libdir}/libgtkada_gl-*.so.*

%files devel
%{_bindir}/*
%{_includedir}/gtkada
%{_libdir}/gtkada
%{_GNAT_project_dir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man*/*

%files doc
# features and known-problems belong with the documentation for developers.
# The license, the list of authors and the directories need to be replicated in
# the doc subpackage as it doesn't depend on the main package.
%license %{_licensedir}/gtkada
%dir %{_docdir}/gtkada
%{_docdir}/gtkada/AUTHORS
%{_docdir}/gtkada/features
%{_docdir}/gtkada/known-problems
%{_docdir}/gtkada/gtkada_ug
%{_docdir}/gtkada/gtkada_rm
%{_docdir}/gtkada/examples
%{_infodir}/*
%{_datadir}/gps

%changelog
%autochangelog
