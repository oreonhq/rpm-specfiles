%global source0_hash df66eb8b2d57b3cefed29b65c0a2b4bd69605da0d94f3b780e44763872fc7e6a

# Bootstrapping GPRbuild
# ======================
#
# GPRbuild needs GPRbuild to be built. When GPRbuild is not available (for
# example, because it is being introduced on a new architecture, or because a
# bug prevents GPRbuild from building a newer version of itself), then one can
# follow a bootstrapping procedure that will eventually produce a `gprbuild`
# package with which a normal (full) build can be performed.
#
# The procedure consists of the following steps:
#
#    1. Make sure the package `gprconfig-kb` is available. If the bootstrapping
#       procedure is used to introduce `gprbuild` on a new architecture, then
#       make sure that the knowledge base contains the necessary information
#       to find and identify the GNAT compiler on that architecture.
#
#    2. Build the `xmlada` package in bootstrap mode to produce a package named
#       `xmlada-sources~bootstrap` which will contain the necessary XML/Ada
#       source files needed by the bootstrap build in step 3.
#
#    3. Build this package in bootstrap mode to produce the`gprbuild~bootstrap`
#       package that can be used to run a normal build of the XML/Ada and
#       GPRbuild packages. This may require temporary changes to ExclusiveArch
#       below, for example to add an architecture that isn't yet listed in
#       GPRbuild_arches.
#
# Historical Note
#
# Before upstream included the `bootstrap.sh` script, one had to bootstrap
# GPRbuild by including a pre-built GPRbuild binary as a "Source" and use that
# binary to build GPRbuild again from sources. This method requires a special
# exception according to the packaging guidelines. While no longer required, the
# so-called bootstrap exception for GPRbuild is still available here:
#
#    https://pagure.io/packaging-committee/issue/605
#
# Enabling Bootstrap Mode
#
# Either pass `--with=bootstrap` to mock(1) or change `bcond_with` to
# `bcond_without`, then commit, build, revert to `bcond_with` and commit again.
#
%bcond_with bootstrap

# The test suite is normally run. It can be disabled with "--without=check".
%bcond check 0

# Stripping out debugging information isn't important when bootstrapping.
%if %{with bootstrap}
%global debug_package %{nil}
%endif

# Don't build libgpr when bootstrapping.
%if %{with bootstrap}
%define with_libgpr 0
%else
%define with_libgpr 1
%endif

# Upstream source information.
%global upstream_owner         AdaCore
%global upstream_name          gprbuild
%global upstream_version       26.0.0
%global upstream_release_date  20250915
%global upstream_commit        bdfb879cf03643ec8e48a09ce07b08c4a6ff0263

Name:           gprbuild
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        A multi-language extensible build tool

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND Unicode-DFS-2016
# GPRbuild itself is licensed under GPL v3 or later with a runtime
# exception, but is statically linked to both the GNAT runtime library
# and the XML/Ada library to prevent the package from breaking when
# GCC or XML/Ada is updated.
#
# - The GNAT runtime library is licensed under the the same license
#   and exception: GPL v3 or later with a runtime exception.
#
# - XML/Ada is also licensed under the same GPL v3 or later and
#   runtime exception, but also mentions the Unicode license as
#   Unicode data files are used as an input for generating some of
#   XML/Ada's source code.

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz
# For testing.
Source1:        gprbuild-sanity.tar.gz

# [unbundling] The GPRconfig KB is already available when bootstrapping.
Patch:          %{name}-dont-reinstall-the-gprconfig-kb.patch
# Set the library so version; rejected upstream as "finicky":
# https://github.com/AdaCore/gprbuild/issues/108
Patch:          %{name}-set-library-so-version.patch

# Resolve naming conflict with libraries for Google gRPC.
#    GPRbuild and Google's gRPC both want the filename "libgpr.so". This patch
#    renames the library to "libgnatprj.so" to resolve the conflict. The name is
#    chosen for consistency with Debian.
#    As of this writing the conflict is unresolved in both upstreams:
#    https://github.com/grpc/grpc/issues/27850
#    https://github.com/AdaCore/gprbuild/issues/120
Patch:          %{name}-resolve-libgpr-conflict.patch

# [Fedora-specific] Follow soft links when resolving the compiler driver.
#    This usrmove patch works for this package. Upstream a different solution
#    would be needed to handle other possible setups.
Patch:          %{name}-usrmove.patch

# [Fedora-specific] Hard code the default KB dir to `/usr/share/gprconfig`.
#    In the upstream code, the default location of the knowledge base is
#    defined to be relative to the installation folder. This is a problem
#    when testing GPRbuild and utilities in a staging directory. For Fedora,
#    installation paths are fixed so the location of the KB can be hard coded.
Patch:          %{name}-hard-code-default-kb-dir.patch

# backport of upstream commit 6421e350274b3018a26bd058b1c90d033b053f71:
Patch:          gprbuild-operator_not_declared.patch

BuildRequires:  gcc-gnat make sed dos2unix findutils
BuildRequires:  libgnat-static
# A fedora-gnat-project-common that contains the macro GPRinstall is needed.
BuildRequires:  fedora-gnat-project-common >= 3.21

%if %{with bootstrap}
BuildRequires:  gprconfig-kb >= 24.0.0
BuildRequires:  xmlada-sources
%else
BuildRequires:  gprbuild
# xmlada-devel must be explicitly specified for first build after bootstrap.
BuildRequires:  xmlada-devel
# An XMLada build that accepts LIBRARY_TYPE=static-pic is needed.
BuildRequires:  xmlada-static >= 2:23
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  texinfo
# TeX package `titleref` is required by `doc/share/latex_elements.py`.
BuildRequires:  tex(titleref.sty)
%endif

%if %{with check}
# To verify if G++ and GFortran are detected by gprconfig.
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
# Language packs used for testing.
# -- list derived from: https://gcc.gnu.org/git/?p=gcc.git;a=tree;f=gcc/po;hb=HEAD
BuildRequires:  glibc-langpack-be
BuildRequires:  glibc-langpack-da
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-el
BuildRequires:  glibc-langpack-es
BuildRequires:  glibc-langpack-fi
BuildRequires:  glibc-langpack-fr
BuildRequires:  glibc-langpack-hr
BuildRequires:  glibc-langpack-id
BuildRequires:  glibc-langpack-ja
BuildRequires:  glibc-langpack-nl
BuildRequires:  glibc-langpack-ru
BuildRequires:  glibc-langpack-sr
BuildRequires:  glibc-langpack-sv
BuildRequires:  glibc-langpack-tr
BuildRequires:  glibc-langpack-uk
BuildRequires:  glibc-langpack-vi
BuildRequires:  glibc-langpack-zh
# Moreutils parallel and chronic parallelize the compiler detection test:
BuildRequires:  moreutils-parallel moreutils
BuildRequires:  tar
%endif

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

Requires:       gprconfig-kb >= 24.0.0
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc

%global common_description_en \
GPRbuild is an advanced software tool designed to help automate the \
construction of multi-language systems. It removes complexity from \
multi-language development by allowing developers to quickly and easily \
compile and link software written in a combination of languages including \
Ada, Assembler, C, C++, and Fortran. Easily extendable by users to cover \
new toolchains and languages it is primarily aimed at projects of all \
sizes organized into subsystems and libraries and is particularly \
well-suited for compiled languages.

%description %{common_description_en}

#################
## Subpackages ##
#################

%if %{without bootstrap}

%package doc
Summary:        Documentation for GPRbuild
BuildArch:      noarch
License:        GFDL-1.3-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later WITH GNAT-exception
# The license of the documentation itself is GFDL 1.3. Some Javascript and CSS
# files that Sphinx includes with the documentation are BSD 2-Clause and
# MIT-licensed. Some examples are licensed under GPL 3.0 or later with GCC
# runtime exception. Some other examples are licensed under GPL 3.0 or later
# with GNAT exception.

%description doc %{common_description_en}

This package contains the documentation in HTML, plain text, PDF, and Info
format, and some examples.

%if %{with_libgpr}

%package -n libgpr
Summary:        The GNAT project manager library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       libgnatprj

%description -n libgpr
An Ada library for handling GNAT project files.

This is not the libgpr that is part of gRPC from Google.

%package -n libgpr-devel
Summary:        Development files for the GNAT project manager library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       libgpr%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
# gpr.gpr imports XMLada project files, so require xmlada-devel.
Requires:       xmlada-devel
Provides:       libgnatprj-devel

%description -n libgpr-devel
An Ada library for handling GNAT project files.

This package contains source code and linking information for developing
applications that use the GNAT project manager library.

This is not the libgpr that is part of gRPC from Google.
%endif
%endif

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

# Convert the line-endings of some files.
find ./examples -type f -a \( -name '*.gpr' -o -name '*.ada' \) -print0 \
    | xargs -0 dos2unix -ic0 \
    | xargs -0 dos2unix --keepdate

# Update some release specific information in the source code. The substitutions
# are scoped to specific lines to increase the chance of detecting code changes
# at this point. Sed should exit with exit code 0 if the substitution succeeded
# (using `t`, jump to end of script) or exit with a non-zero exit code if the
# substitution failed (using `q1`, quit with exit code 1).
sed --in-place \
    --expression='33 { s,18.0w,%{upstream_version},         ; t; q1 }' \
    --expression='36 { s,19940713,%{upstream_release_date}, ; t; q1 }' \
    --expression='38 { s,"2016",Date (1 .. 4),              ; t; q1 }' \
    --expression='43 { s,Gnatpro,GPL,                       ; t; q1 }' \
    gpr/src/gpr-version.ads

###########
## Build ##
###########

%build
%if %{with bootstrap}

# Emit some useful output.
gcc -v
gcc -dumpmachine
gcc -dumpversion
gnatls -v --version

# Additional flags to make executables position-independent.
%global Gnatmake_flags_pie -cargs -fPIC -largs -pie -lgnarl_pic -lgnat_pic

export GNATMAKEFLAGS='%{Gnatmake_flags} %{Gnatmake_flags_pie}'

# This will build the bootstrapped binaries.
./bootstrap.sh \
    --with-xmlada=%{_includedir}/xmlada/sources/ \
    --prefix=%{buildroot}%{_prefix}/ \
    build

%else

# Additional flags to make executables position-independent. Note that the tools
# are still statically linked to prevent them from breaking when updating to a
# new GCC release.
%global GPRbuild_flags_pie -cargs -fPIC -largs -pie -lgnarl_pic -lgnat_pic -gargs

gprbuild -v -p %{GPRbuild_flags} %{GPRbuild_flags_pie} \
         -XBUILD=production -XLIBRARY_TYPE=static-pic -XVERSION=%{version} \
         -P gprbuild.gpr

%if %{with_libgpr}
gprbuild -v -p %{GPRbuild_flags} \
         -XBUILD=production -XLIBRARY_TYPE=relocatable -XVERSION=%{version} \
         -P gpr/gpr.gpr
%endif

# Make the documentation.
make -C doc html txt pdf info

%endif

#############
## Install ##
#############

%install
%if %{with bootstrap}

# This will install the bootstrapped binaries.
bash -x ./bootstrap.sh \
     --with-xmlada=%{_includedir}/xmlada/sources/ \
     --prefix=%{buildroot}%{_prefix}/ \
     install

%else

# Install the external tools.
%{GPRinstall} \
           --install-name=gprbuild --mode=usage \
           -XBUILD=production -XINSTALL_MODE=nointernal -XVERSION=%{version} \
           -P gprbuild.gpr

# Install the internal tools.
gprinstall --create-missing-dirs --no-manifest \
           --prefix=%{buildroot}%{_prefix} \
           --install-name=gprbuild --mode=usage \
           -XBUILD=production -XINSTALL_MODE=internal -XVERSION=%{version} \
           -P gprbuild.gpr

%if %{with_libgpr}

# Install the library.
%{GPRinstall -s libgpr -a libgpr} --no-build-var \
           -XBUILD=production -XLIBRARY_TYPE=relocatable -XVERSION=%{version} \
           -P gpr/gpr.gpr

# Fix up the symbolic links for the shared libraries.
ln --symbolic --force libgnatprj.so.%{version} %{buildroot}%{_libdir}/libgnatprj.so

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/libgpr");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/libgpr";|i' \
    %{buildroot}%{_GNAT_project_dir}/gpr.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.

%endif

# Install the Info version of the manual where Info files belong.
mv --no-target-directory %{buildroot}%{_pkgdocdir}/info %{buildroot}%{_infodir}

# Move the examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples
rmdir %{buildroot}%{_datadir}/examples

%endif

###########
## Check ##
###########

%if %{with check}
%check

# Make the files installed in the buildroot visible to the testsuite.
export PATH=%{buildroot}%{_bindir}:%{buildroot}%{_libexecdir}:$PATH
export GPR_PROJECT_PATH=%{buildroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH

# TEST 1: Validate knowledge base.

gprconfig --batch -o /dev/null --validate

# TEST 2: Verify detection of compilers and linkers under different locales.

# Tests 1 and 2 mostly test the knowledge base. These tests are done here
# instead of in gprconfig-kb.spec to avoid a dependency loop that would make
# bootstrapping GPRbuild even more complicated.

# In each locale, ask GPRconfig to find GCC compilers for Ada, Assembly, C, C++
# and Fortran, and LD for linking object files ("Bin_Img"). Prevent mixing of
# error messages from parallel processes by collecting each one's error stream
# with chronic.
parallel -i \
         chronic env 'LANG={}' \
                     gprconfig --batch -o /dev/null \
                               --config=Ada,,default,%{_bindir},GNAT \
                               --config=Asm,,,%{_bindir},GCC-ASM \
                               --config=Asm2,,,%{_bindir},GCC-ASM \
                               --config=Asm_Cpp,,,%{_bindir},GCC-ASM \
                               --config=C,,,%{_bindir},GCC \
                               --config=C++,,,%{_bindir},G++ \
                               --config=Fortran,,,%{_bindir},GFORTRAN \
                               --config=Bin_Img,,,%{_bindir},LD \
         -- $(locale -a)

# TEST 3: Perform a test build.

# Unpack the test project.
tar --verbose --extract --gzip --file %{SOURCE1}

# Try to build the test project; use the pre-installed GPRconfig KB.
gprbuild -v -P gprbuild-tests/tests_shared.gpr

# TEST 4: Build and run the examples.

make -C examples run

%endif

###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%doc README*
%{_bindir}/gpr*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gpr*
%attr(444,-,-) %{_GNAT_project_dir}/_default.gpr
%if %{without bootstrap}
# Exclude the installation script; it serves no purpose in this context.
%exclude %{_prefix}/doinstall
%endif

%if %{without bootstrap}

%files doc
%{_infodir}/*
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/pdf
%{_pkgdocdir}/txt
%{_pkgdocdir}/examples
# Remove Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv

%if %{with_libgpr}

%files -n libgpr
%{_libdir}/libgnatprj.so.%{version}

%files -n libgpr-devel
%{_GNAT_project_dir}/gpr.gpr
%dir %{_includedir}/libgpr
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/libgpr/gpr_imports.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/libgpr/*.ad[sb]
%dir %{_libdir}/libgpr
%attr(444,-,-) %{_libdir}/libgpr/*.ali
%{_libdir}/libgnatprj.so

%endif
%endif

###############
## Changelog ##
###############

%changelog
%autochangelog
