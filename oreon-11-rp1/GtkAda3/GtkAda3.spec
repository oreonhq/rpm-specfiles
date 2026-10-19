%global source0_hash 4650af277b55aff0092ccc89891eb0be72b617b801fe5a24b1b65ccc2c9aaa1c
%global upstream_owner    AdaCore
%global upstream_name     gtkada
%global upstream_version  26.0.0
%global upstream_commit   6106d463e45d259e5bc44d9514e44664b7d7eac9
Name:           GtkAda3
Epoch:          2
Version:        %{upstream_version}
Release:        3%{?dist}
Summary:        GTKada, an Ada binding to GTK+ 3
Summary(sv):    GTKada, en adabindning till GTK+ 3
%bcond_with gps
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Source2:        testgtk_Makefile
Source3:        testgtk.gpr
Source4:        gtkada.gpr.in
Patch:          %{name}-enable-a-staged-build.patch
Patch:          %{name}-gps-plugin-remove-gtkada-rm.patch
Patch:          gtkada-dialog-constraint_error.patch
Patch:          gtkada-canvas_view-implicit_conversion.patch
ExclusiveArch:  %{GPRbuild_arches}
Obsoletes:      GtkAda3-gl < 2:23
%global common_description_en \
GTKada is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.
%global common_description_sv \
GTKada är en adabindning till den grafiska verktygslådan GTK+. Med GTKada \
kan du utveckla grafiska användargränssnitt i ada baserade på GTK+.
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  fedora-gnat-project-common
BuildRequires:  findutils
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  gtk3-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
# /oreon:deps
%description %{common_description_en}

This version of GTKada binds to GTK+ 3.x.

%description -l sv %{common_description_sv}

Denna versionen av GTKada binder till GTK+ 3.x.

#################
## Subpackages ##
#################

%package devel
Summary:        Development files for GTKada for GTK+ 3
Summary(sv):    Filer för programmering med GTKada för GTK+ 3
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(glib-2.0)
Recommends:     %{name}-doc
Conflicts:      GtkAda-devel < 3
%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use GTKada to bind to GTK+ 3.x.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder GTKada för att binda till GTK+ 3.x.

%package doc
Summary:        Documentation for GTKada for GTK+ 3
Summary(sv):    Dokumentation till GTKada för GTK+ 3
BuildArch:      noarch
License:        GFDL-1.1-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
%description doc %{common_description_en}

The %{name}-doc package contains the documentation for GTKada for GTK+ 3.x.

%description doc -l sv %{common_description_sv}

Paketet %{name}-doc innehåller dokumentationen till GTKada för GTK+ 3.x.

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

# The substitutions below are scoped to specific lines to increase the chance of
# detecting code changes at this point. Sed should exit with exit code 0 if the
# substitution succeeded (using `t`, jump to end of script) or exit with a non-
# zero exit code if the substitution failed (using `q1`, quit with exit code 1).

# Change the name of the target directory of the documentation to avoid a
# conflict between GtkAda3-doc and GtkAda-doc.
sed --in-place \
    --expression='83 { s,share/doc/gtkada,share/doc/GtkAda3, ; t; q1 }' \
    --expression='86 { s,share/doc/gtkada,share/doc/GtkAda3, ; t; q1 }' \
    src/gtkada.gpr

# Adjust the documentation directory in the GPS plug-in as-well.
sed --in-place \
    --expression='4 { s,share/doc/gtkada,share/doc/GtkAda3, ; t; q1 }' \
    xml/gtkada.xml

# Set the target directory of the artifacts of the `testgtk` application to be
# relative to the prefix argument of GPRinstall, and don't treat the Ada source
# code as artifacts.
sed --in-place \
    --expression='45 { s,share/examples/gtkada/testgtk,\./, ; t; q1 }' \
    --expression='46 { s|"\*\.ad\*", ||                     ; t; q1 }' \
    testgtk/testgtk.gpr

# Update the package version (also in configure.ac, as this is the source for
# the version shown in the documentation; see also `docs/gtkada_ug/conf.py`).
sed --in-place \
    --expression='1   { s,18.0w,%{version}, ; t; q1 }' \
    ./configure.ac
sed --in-place \
    --expression='582 { s,18.0w,%{version}, ; t; q1 }' \
    --expression='583 { s,18.0w,%{version}, ; t; q1 }' \
    ./configure

# Remove VCS files. Some interfere with the code generation check at the
# beginning of the build section.
find -name ".cvsignore" -type f -delete
find -name ".gitignore" -type f -delete

# Remove bogus executable bits.
chmod a-x testgtk/*.ad[sb]

###########
## Build ##
###########

%build

%define _lto_cflags %{nil}
%{configure} --disable-static --disable-static-pic
mkdir stage  # without --parents to avoid clobbering any existing directory
%{make_build} relocatable GPRBUILD_OPTIONS='%{GPRbuild_flags} -largs -lm -gargs'
make -C docs/gtkada_ug html latexpdf
%{GPRinstall -d stage -s gtkada -a gtkada} \
    --no-build-var --no-lib-link -P src/gtkada.gpr
ln --symbolic --force libgtkada.so.%{version} stage%{_libdir}/libgtkada.so
%global GPRbuild_flags_pie -cargs -fPIC -largs -pie -bargs -shared -gargs
%{make_build} tools GPRBUILD_OPTIONS='%{GPRbuild_flags} %{GPRbuild_flags_pie} -largs -lm -gargs -aP stage%{_GNAT_project_dir}'
%{GPRinstall -d stage} --no-build-var --mode=usage \
    -aP stage%{_GNAT_project_dir} -P src/tools/tools.gpr
%install
%global demodir %{_pkgdocdir}/examples/testgtk
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps
cp --archive stage/* --target-directory=%{buildroot}
gprinstall --create-missing-dirs --no-manifest --no-build-var \
           --prefix=%{buildroot}%{demodir} \
           --sources-subdir=%{buildroot}%{demodir} \
           --project-subdir=%{buildroot}%{demodir} \
           --sources-only \
           -P testgtk/testgtk.gpr
gprinstall --create-missing-dirs --no-manifest --no-build-var \
           --prefix=%{buildroot}%{demodir}/task_project \
           --sources-subdir=%{buildroot}%{demodir}/task_project/src \
           --project-subdir=%{buildroot}%{demodir}/task_project/ \
           --sources-only \
           -P testgtk/task_project/task_project.gpr
sed --expression='22 { s,@VERSION@,%{version}, ; t; q1 }' \
    %{SOURCE4} \
    >%{buildroot}%{_GNAT_project_dir}/gtkada.gpr
%{inst} --no-target-directory %{SOURCE2} %{buildroot}%{demodir}/Makefile
%{inst} %{SOURCE3} --target-directory=%{buildroot}%{demodir}
mv %{buildroot}%{_datadir}/gps/plug-ins/gtkada.xml \
   %{buildroot}%{_datadir}/gps/plug-ins/gtkada3.xml
mkdir --parents %{buildroot}%{_licensedir}/%{name}
%{inst} COPYING* --target-directory=%{buildroot}%{_licensedir}/%{name}
%{inst} AUTHORS README.md features* known-problems* --target-directory=%{buildroot}%{_pkgdocdir}
%oreon_autofiles GtkAda3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles GtkAda3-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n GtkAda3-devel -f %{oreon_filedir}/GtkAda3-devel.list
%files -n GtkAda3-doc -f %{oreon_filedir}/GtkAda3-doc.list

%changelog

%autochangelog
