%global source0_hash a202f1c9955d26973d30e6d0357ba83f4031bc218006d620fa916420316a4f24

# This package has a bootstrap build mode that can be used to create a source
# code package for bootstrapping GPRbuild. See the 'gprbuild' spec file for more
# information.
%bcond_with bootstrap

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     xmlada
%global upstream_version  26.0.0
%global upstream_commit   5e5b761eb827f458efd2043a5e9ab03e1a614720

Name:           xmlada
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        XML library for Ada

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND Unicode-DFS-2016
# XML/Ada itself is licensed under GPL v3 or later with a runtime exception. The
# Unicode license is mentioned as Unicode data files were used as an input for
# generating some of XML/Ada's source code.

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

# XML/Ada's aggregate project file. This project file is normally generated and
# installed by GPRinstall, but as we'll install each XML/Ada component
# separately, we need to maintain and install it manually.
Source1:        xmlada.gpr

BuildRequires:  make
%if %{without bootstrap}
BuildRequires:  gcc-gnat gprbuild sed
BuildRequires:  fedora-gnat-project-common
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
%else
BuildRequires:  findutils
%endif

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
XML/Ada includes support for parsing XML files, including DTDs, full support for \
SAX, and an almost complete support for the core part of the DOM. It includes \
support for validating XML files with XML schemas.

%description %{common_description_en}

#################
## Subpackages ##
#################

%if %{without bootstrap}

%package devel
Summary:        Development files for the XML/Ada library
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the XML/Ada library.

%package static
Summary:        Static libraries of XML/Ada
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description static %{common_description_en}

This package contains the XML/Ada libraries for static linking. It is needed
for linking GPRbuild statically so that GPRbuild will remain functional when
libraries are upgraded.

Other Fedora packages shall require xmlada-devel rather than xmlada-static if
possible.

%package doc
Summary:        Documentation for the XML/Ada library
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and MIT-licensed.
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# Fonts are required by the Read the Docs Sphinx theme.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.

%else

# When bootstrapping gprbuild, only a package that contains source code is
# produced, so a debug package is not needed.
%global debug_package %{nil}

%package sources
Summary:        Sources of the XML/Ada library (for bootstrapping GPRbuild)
BuildArch:      noarch

%description sources %{common_description_en}

This package contains source code for bootstrapping GPRbuild on architectures
on which GPRbuild is not yet available.

%endif

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

# Set version number.
sed --in-place --expression 's/18.0w/%{version}/' configure configure.in

###########
## Build ##
###########

%build
%if %{without bootstrap}
%configure --enable-build=distrib --enable-shared

# Build the libraries.
%{make_build} shared static-pic GPROPTS='%{GPRbuild_flags}'

# Make the documentation.
make -C docs html latexpdf

%else
%{configure} --enable-build=distrib

%endif

#############
## Install ##
#############

%install
%if %{without bootstrap}

# Verify that the ALI files of both builds (relocatable and static-pic) match.
# The verfication is necessary as GPRinstall will overwrite the ALI files during
# the installation of the static-pic build (which is installed after the
# relocatable build).
for component_dir in dom schema unicode sax input_sources ; do
    diff --exclude "*.a" --exclude "*.so*" --exclude ".cvsignore" \
         %{_builddir}/%{name}-%{version}/${component_dir}/lib/relocatable \
         %{_builddir}/%{name}-%{version}/${component_dir}/lib/static-pic
done

# Install each component.
function run_gprinstall {
    local libtype=$1
    local component=$2
    local directory=$3  # directory name in the source tree
    %{GPRinstall -s xmlada/${component}} \
               --build-var=LIBRARY_TYPE --build-var=XMLADA_BUILD \
               --build-name=${libtype} -XLIBRARY_TYPE=${libtype} \
               -P ${directory}/%{name}_${component}.gpr
}

for libtype in relocatable static-pic ; do
    for component in dom schema unicode sax ; do
        run_gprinstall ${libtype} ${component} ${component}
    done

    # The "input" component needs special treatment as its dirname in the source
    # tree ("input_sources") is not reflected in its GNAT project file
    # ("xmlada_input.gpr").
    run_gprinstall ${libtype} input input_sources
done

# Install the aggregate project file ("xmlada.gpr").
install --mode=u=rw,go=r,a-s --preserve-timestamps \
        %{SOURCE1} --target-directory=%{buildroot}%{_GNAT_project_dir}

# Fix up the symbolic links for the shared libraries.
for component in dom input_sources schema unicode sax ; do
    ln --symbolic --force lib%{name}_${component}.so.%{version} \
       %{buildroot}%{_libdir}/lib%{name}_${component}.so
done

# Move examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples

rmdir %{buildroot}%{_datadir}/examples

# Make the generated project files architecture-independent.
for component in dom input schema unicode sax ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}/${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/%{name}_${component}.gpr
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 4: Replace the value of Library_Dir with Directories.Libdir.
    # 5: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done

%else

# Copy the source files.
mkdir --parents %{buildroot}%{_includedir}/%{name}/sources
cp -r . %{buildroot}%{_includedir}/%{name}/sources
find %{buildroot}%{_includedir}/%{name}/sources -type f ! -name "*ad[sb]" ! -name "*gpr" -delete
find %{buildroot}%{_includedir}/%{name}/sources -type d -empty -delete

%endif

###########
## Files ##
###########

%if %{without bootstrap}

%files
%license COPYING3 COPYING.RUNTIME
%doc README* TODO AUTHORS
%{_libdir}/lib%{name}*.so.%{version}

%files devel
%{_GNAT_project_dir}/%{name}*.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}*.so

%files static
%{_libdir}/lib%{name}*.a

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/*.html
%{_pkgdocdir}/searchindex.js
%{_pkgdocdir}/_sources
%{_pkgdocdir}/_static
%{_pkgdocdir}/XMLAda.pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/.buildinfo
%exclude %{_pkgdocdir}/objects.inv

%else

%files sources
%{_includedir}/%{name}

%endif

###############
## Changelog ##
###############

%changelog
%autochangelog
