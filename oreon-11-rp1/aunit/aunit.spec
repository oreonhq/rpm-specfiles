%global source0_hash e9ef1b681c7c788023631ca13edb342d250cdbfe775f72f2907d7c1d5063ba10

# The test suite is normally run. It can be disabled with "--without=check".
%bcond check 0

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     aunit
%global upstream_version  26.0.0
%global upstream_commit   cb7458f1a7f193e72526cb6bdd1a9a82ccfdd3f7

Name:           aunit
Epoch:          2
Version:        %{upstream_version}
Release:        3%{?dist}
Summary:        A unit testing framework for Ada

License:        GPL-3.0-or-later WITH GCC-exception-3.1

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora-specific] Build a relocatable library.
Patch:          %{name}-disable-static.patch
# Correct paths from which GPRinstall is supposed to copy the documentation.
# See also: https://github.com/AdaCore/aunit/issues/50
Patch:          %{name}-fix-doc-build-path.patch
# Adjust pathnames in the manual, replacing the Adacore-specific pathnames with
# the FHS-compliant pathnames where this package installs the examples:
Patch:          %{name}-cb-examples-dir.patch

BuildRequires:  gcc-gnat gprbuild make sed findutils dos2unix
BuildRequires:  fedora-gnat-project-common
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
# TeX package `titleref` is required by `doc/share/latex_elements.py`.
BuildRequires:  tex(titleref.sty)
%if %{with check}
# Used in `test/Makefile`.
BuildRequires:  grep
BuildRequires:  diffutils
%endif

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
This is the Ada unit test framework AUnit, derived from the JUnit/CPPUnit \
frameworks for Java/C++.

%description %{common_description_en}

#################
## Subpackages ##
#################

%package devel
Summary:        Development files for AUnit
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use AUnit.

%package doc
Summary:        Documentation for AUnit
BuildArch:      noarch
License:        GFDL-1.3-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
# The documents have a GFDL 1.3 license with no invariants. Some Javascript and
# CSS files that Sphinx includes with the documentation are BSD 2-Clause and MIT
# licensed. The example code is licensed under GPLv3+ with the GCC runtime
# exception.
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# Fonts are required by the Read the Docs Sphinx theme.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

# Version information in this file is used during the build.
echo '%{version}' > ./version_information

# Convert the line-endings in some GNAT project files.
find ./examples -name '*.gpr' -print0 \
    | xargs -0 dos2unix -ic0 \
    | xargs -0 dos2unix --keepdate

# One of the tests in the test suite fails because of a runtime accessibility
# check on line 101 of file `aunit-simple_test_cases.adb`. A workaround is to
# replace all runtime checks for anonymous access types with compile-time checks
# based on the "designated type model" (-gnatd_b). See also:
#
#   - https://github.com/AdaCore/aunit/issues/55
#   - https://blog.adacore.com/going-beyond-ada-2022

# Disable dynamic accessibility checks related to anonymous access types.
cat << EOF > gnat.adc
pragma Restrictions (No_Dynamic_Accessibility_Checks);
EOF

###########
## Build ##
###########

%build

# Use configuration file and enable the `designated type` model (-gnatd_b).
%global GPRbuild_adc_flags -cargs -gnatec=gnat.adc -gnatd_b -gargs

# Build the library.
gprbuild %{GPRbuild_flags} %{GPRbuild_adc_flags} \
         -XVERSION=%{version} -P lib/gnat/aunit.gpr

# Make the documentation.
make -C doc html-all pdf-all

#############
## Install ##
#############

%install

# Install the library.
%{GPRinstall} --no-build-var -XVERSION=%{version} -P lib/gnat/aunit.gpr

# Fix up the symlink.
ln --symbolic --force lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so

# Move the examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples

rmdir %{buildroot}%{_datadir}/examples

# Clean PDF directory.
rm -r  %{buildroot}%{_pkgdocdir}/pdf/_static
find %{buildroot}%{_pkgdocdir}/pdf/ -type f -not -name 'aunit_cb.pdf' -delete

# Before making the project files architecture-independent, copy the buildroot
# into a separate directory for later testing. The testsuite fails if applied to
# the buildroot after making the project files architecture-independent because
# of the hardcoded paths in `directories.gpr`.
%if %{with check}
%global checkroot %{_builddir}/%{name}-%{version}/checkroot
mkdir %{checkroot}  # without --parents to not clobber any upstream directory
cp --recursive %{buildroot}/* %{checkroot}/
%endif

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Delete the package Linker, which contains linker parameters that a
#    shared library normally doesn't need, and can contain architecture-
#    specific pathnames.
# 4: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 5: Replace the value of Library_Dir with Directories.Libdir.
# 6: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.

###########
## Check ##
###########

%if %{with check}
%check

# Make the files of this packages visible to the test runner.
export PATH=%{checkroot}%{_bindir}:$PATH
export LD_LIBRARY_PATH=%{checkroot}%{_libdir}:$LD_LIBRARY_PATH
export GPR_PROJECT_PATH=%{checkroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH

# Run the test suite. If it fails, output its output so we can troubleshoot.
make -C test || { cat test/test.out.full >&2 ; false ; }

%endif

###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%doc README*
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_GNAT_project_dir}/%{name}.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so
# Exclude the plugin for GNAT programming studio. The IDE is
# not available in Fedora, so there's no point including it.
%exclude %{_datadir}/gps

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%dir %{_pkgdocdir}/pdf
%{_pkgdocdir}/pdf/aunit_cb.pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv

###############
## Changelog ##
###############

%changelog
%autochangelog
