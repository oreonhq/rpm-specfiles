%global source0_hash 930a72ca08f02b1b4a1ff7b8aeef1b0328547bc8f82a41fb390dbcad93b55072
Name:           GtkAda
Version:        2.24.2
Release:        56%{?dist}
Summary:        GTKada 2, an Ada binding to GTK+ 2
Summary(sv):    GTKada 2, en adabindning till GTK+ 2
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/AdaCore/gtkada
Source0:        gtkada-gpl-%{version}-src.tgz
Patch:          GtkAda-2.24.2-configuration-5.patch
Patch:          GtkAda-2.14.1-multilib_gpr.patch
Patch:          GtkAda-2.14.1-multilib_gtkada-config.patch
Patch:          GtkAda-2.18.0-lm.patch
Patch:          GtkAda-2.18.0-gl_placement.patch
Patch:          GtkAda-2.18.0-link_as_needed.patch
Patch:          GtkAda-2.24.2-source_dir.patch
Patch:          GtkAda-2.18.0-no_include_gmain.patch
Patch:          GtkAda-2.24.2-man_xref.patch
Patch:          GtkAda-2.24.2-format_security.patch
Patch:          GtkAda-2.24.2-no_extern_inline.patch
Patch:          GtkAda-2.24.2-gprbuild.patch
Patch:          GtkAda-2.24.2-unmask.patch
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
%{name} is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.
%global common_description_sv \
%{name} är en adabindning till den grafiska verktygslådan GTK+. Med %{name} \
kan du utveckla grafiska användargränssnitt i ada baserade på GTK+.
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  fedora-gnat-project-common
BuildRequires:  findutils
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  gtk2-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libbonobo-devel
BuildRequires:  libbonoboui-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  make
BuildRequires:  recode
# /oreon:deps
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
Requires:       gtk2-devel%{?_isa}
Recommends:     %{name}-doc
Conflicts:      GtkAda3-devel
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

%define _lto_cflags %{nil}
LDFLAGS="${LDFLAGS} -Wl,--no-warn-execstack"
%{configure} --enable-build=Debuginfo --disable-subdirs --disable-static
make src "GPRbuild_optflags=%{GPRbuild_flags}"
%install
%{make_install} gprdir=%{_GNAT_project_dir}
mkdir -p %{buildroot}%{_mandir}/man1
install --mode=u=rw,go=r,a-s --preserve-timestamps docs/gtkada-config.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_docdir}/gtkada/gtkada_ug/gtkada_ug.info --target-directory=%{buildroot}%{_infodir}
mv --no-target-directory %{buildroot}%{_datadir}/examples/gtkada %{buildroot}%{_docdir}/gtkada/examples
install --mode=u=rw,go=r,a-s --preserve-timestamps AUTHORS README features known-problems %{buildroot}%{_docdir}/gtkada
mkdir --parents %{buildroot}%{_licensedir}/gtkada
install --mode=u=rw,go=r,a-s --preserve-timestamps COPYING %{buildroot}%{_licensedir}/gtkada
%oreon_autofiles GtkAda-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles GtkAda-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles GtkAda-gl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles GtkAda-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n GtkAda-devel -f %{oreon_filedir}/GtkAda-devel.list
%files -n GtkAda-gnome -f %{oreon_filedir}/GtkAda-gnome.list
%files -n GtkAda-gl -f %{oreon_filedir}/GtkAda-gl.list
%files -n GtkAda-doc -f %{oreon_filedir}/GtkAda-doc.list

%changelog

%autochangelog
