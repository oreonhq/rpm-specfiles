%global source0_hash 4650af277b55aff0092ccc89891eb0be72b617b801fe5a24b1b65ccc2c9aaa1c

# Upstream source information.
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

# The GNAT Studio plug-in is excluded because GNAT Studio isn't packaged.
# Pass "--with gps" to RPMbuild to include it.
%bcond_with gps

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
# The license is GPLv3+ with the GCC runtime exception, except for:
# - src/misc.c          : GPLv2+ with GNAT runtime exception
# - src/misc_osx.h      : GPLv2+ with GNAT runtime exception
# - src/misc_osx.m      : GPLv2+ with GNAT runtime exception
# - src/gtkada-intl.gpb : GPLv2+ with GNAT runtime exception

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

Source2:        testgtk_Makefile
Source3:        testgtk.gpr
Source4:        gtkada.gpr.in

# [Fedora-specific] Don't rebuild the library when building gtkada-dialog.
Patch:          %{name}-enable-a-staged-build.patch
# [Fedora-specific] GNAT Studio plugin: remove shortcut to the GtkAda RM.
Patch:          %{name}-gps-plugin-remove-gtkada-rm.patch
# Don't raise Constraint_Error instead of displaying an iconless custom dialog:
# https://github.com/AdaCore/gtkada/issues/56
Patch:          gtkada-dialog-constraint_error.patch
# Backport of upstream commit 26be71ad32cb5edd4c2bf5b45e92e2ae664eb957:
Patch:          gtkada-canvas_view-implicit_conversion.patch

BuildRequires:  gcc-gnat gprbuild make
BuildRequires:  fedora-gnat-project-common

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme

BuildRequires:  python3
BuildRequires:  gtk3-devel
BuildRequires:  diffutils
BuildRequires:  sed
BuildRequires:  findutils

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

# GTK.GLarea is now included in the main library so GtkAda3-gl is gone. Let
# upgrades remove the subpackage:
Obsoletes:      GtkAda3-gl < 2:23

%global common_description_en \
GTKada is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.

%global common_description_sv \
GTKada är en adabindning till den grafiska verktygslådan GTK+. Med GTKada \
kan du utveckla grafiska användargränssnitt i ada baserade på GTK+.

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

# Unlike GTK+, GTKada has no support for installing two versions side by side,
# other than dumping the entire directory tree under some nonstandard prefix
# and requiring users to mess with various environment variables. Despite the
# API incompatibilities, both versions use the filename "gtkada.gpr" and
# directories named "gtkada".
#
# Hacking the build system to change various filenames from "gtkada" to
# "gtkada3" would be more trouble than it's worth, and would make Fedora
# incompatible with everything that uses GTKada. Both developers and packagers
# would have to do special things to select the right version of the library.
#
# Therefore GtkAda-devel and GtkAda3-devel are allowed to conflict.

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
# The documents have a GFDL 1.1 license with no invariants. Some Javascript and
# CSS files that Sphinx includes with the documentation are BSD 2-Clause and MIT
# licensed. The example code is licensed under GPLv3+ with the GCC runtime
# exception.
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# Fonts are required by the Read the Docs Sphinx theme.

%description doc %{common_description_en}

The %{name}-doc package contains the documentation for GTKada for GTK+ 3.x.

%description doc -l sv %{common_description_sv}

Paketet %{name}-doc innehåller dokumentationen till GTKada för GTK+ 3.x.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

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
# This package triggers a GCC failure when building with LTO.  Disable
# LTO for now.  fld_incomplete_type_of, at ipa-free-lang-data.cc:257
%define _lto_cflags %{nil}

%{configure} --disable-static --disable-static-pic

# NOTE FOR v23.0.0: The re-generated code does not match the pre-generated code
# in the tarball: upstream made manual changes to the pre-generated code:
#
#    gtk-list_store.adb : upstream commit 99dafa9, near line 536
#    gtk-list_store.adb : upstream commit e9c0e98, near line 536
#    gtk-tree_model.adb : upstream commit 6ae5622, near line 1110
#
# We'll disable the regeneration for now and continue to use the pre-generated
# code with the manual changes.

%if 0

# Regenerate the generated Ada packages to verify that they can be regenerated.
# Use the included GIR files, because binding.py is only expected to work with
# those specific files.
mv src/generated src/pre-generated
mkdir src/generated
make generate PYTHON='%{python3}'

# Compare the generated packages to the pre-generated ones to verify that the
# code being compiled is the same as what the developers upstream have reviewed
# and tested. Ignore differences in comment lines.
rm src/generated/tmp.ada
diff --recursive --ignore-matching-lines='^-- ' src/pre-generated src/generated >&2

%endif

# In order to build gtkada-dialog with hardening switches and dynamically link
# it with the GTKada library, we need to build the library first and then stage
# it.
mkdir stage  # without --parents to avoid clobbering any existing directory

# Build the library.
%{make_build} relocatable GPRBUILD_OPTIONS='%{GPRbuild_flags} -largs -lm -gargs'

# Build the documentation (user's guide only as the reference guide requires
# Gnatdoc; a tool that has not been packaged yet). We build the documentation
# now as it's installed with gtkada.gpr (see `Artifacts` package in gtkada.gpr).
make -C docs/gtkada_ug html latexpdf

# Stage the library and documentation. Use GPRinstall directly instead of the
# Makefile rule to have full control over what is installed where.
%{GPRinstall -d stage -s gtkada -a gtkada} \
    --no-build-var --no-lib-link -P src/gtkada.gpr

# Create the library link.
ln --symbolic --force libgtkada.so.%{version} stage%{_libdir}/libgtkada.so

# Additional flags to link the executable (gtkada-dialog) dynamically with the
# GNAT runtime and make it position-independent.
%global GPRbuild_flags_pie -cargs -fPIC -largs -pie -bargs -shared -gargs

# Build gtkada-dialog.
%{make_build} tools GPRBUILD_OPTIONS='%{GPRbuild_flags} %{GPRbuild_flags_pie} -largs -lm -gargs -aP stage%{_GNAT_project_dir}'

# Stage gtkada-dialog.
%{GPRinstall -d stage} --no-build-var --mode=usage \
    -aP stage%{_GNAT_project_dir} -P src/tools/tools.gpr

#############
## Install ##
#############

%install
%global demodir %{_pkgdocdir}/examples/testgtk
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps

# The library, gtkada-dialog and the documention have already been staged, so
# just copy them to the "buildroot" staging directory. Do not move (mv) because
# find-debuginfo will want to collect some files under stage.
cp --archive stage/* --target-directory=%{buildroot}

# Install the examples (testgtk plus related).
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

# It's much easier to install our own multilib-compatible usage project file
# than to patch the one that GPRinstall generated.
# It needs the version string inserted though.
sed --expression='22 { s,@VERSION@,%{version}, ; t; q1 }' \
    %{SOURCE4} \
    >%{buildroot}%{_GNAT_project_dir}/gtkada.gpr

# Add a standalone build system for the demo programs so that users can build
# them and link them to the packaged libraries.
%{inst} --no-target-directory %{SOURCE2} %{buildroot}%{demodir}/Makefile
%{inst} %{SOURCE3} --target-directory=%{buildroot}%{demodir}

# Rename the GNAT Studio plugin.
mv %{buildroot}%{_datadir}/gps/plug-ins/gtkada.xml \
   %{buildroot}%{_datadir}/gps/plug-ins/gtkada3.xml

# Include these license and documentation files.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
%{inst} COPYING* --target-directory=%{buildroot}%{_licensedir}/%{name}
%{inst} AUTHORS README.md features* known-problems* --target-directory=%{buildroot}%{_pkgdocdir}

###########
## Files ##
###########

%files
%{_libdir}/libgtkada.so.*
%license %{_licensedir}/%{name}
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README.md

%files devel
%dir %{_includedir}/gtkada
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/gtkada/*.[ch]
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gtkada/*.ad[sb]
%dir %{_libdir}/gtkada
%attr(444,-,-) %{_libdir}/gtkada/*.ali
%{_GNAT_project_dir}/*
%{_libdir}/lib*.so
# There's little reason to make a separate subpackage for gtkada-dialog, so
# it's included in the -devel package:
%{_bindir}/*

%files doc
# features and known-problems belong with the documentation for developers.
# The license, the list of authors and the directories need to be replicated in
# the doc subpackage as it doesn't depend on the main package.
%license %{_licensedir}/%{name}
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/features*
%{_pkgdocdir}/known-problems*
%{_pkgdocdir}/gtkada_ug
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package:
%exclude %{_pkgdocdir}/gtkada_ug/.buildinfo
%exclude %{_pkgdocdir}/gtkada_ug/objects.inv

%if %{with gps}
%{_datadir}/gps
%else
%exclude %{_datadir}/gps
%endif

###############
## Changelog ##
###############

%changelog
%autochangelog
