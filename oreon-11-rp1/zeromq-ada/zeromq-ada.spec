%global source0_hash 84e3e011a214ac2ccd87e27c2e5a635bb8f58f562bc6cfc21549dc546309ca5a

# The test suite is normally run. It can be disabled with "--without=check".
%bcond check 0

# The low-level bindings are normally regenerated. Regeneration can be disabled
# with "--without=generate".
%bcond_without generate

# Upstream source information.
%global upstream_owner        persan
%global upstream_name         zeromq-Ada
%global upstream_version      4.1.5
%global upstream_commit_date  20251117
%global upstream_commit       c9a0e984b673ee61cbf86819c300d7d54f563fea
%global upstream_shortcommit  %(c=%{upstream_commit}; echo ${c:0:7})

Name:           zeromq-ada
Version:        %{upstream_version}^git%{upstream_commit_date}.%{upstream_shortcommit}
Release:        2%{?dist}
Summary:        Ada binding for ZeroMQ

License:        MIT
# According to the upstream commit history, the license of this library was
# changed to MIT on Apr 8, 2021 (upstream commit 651ca44).

URL:            https://zeromq.org
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{upstream_shortcommit}.tar.gz

# [Fedora-specific] Remove Python and Makefile languages from the ZMQ
#   GPRbuild-file. Both languages are used only during the development of the
#   bindings/library and are of no relevance to the user of the bindings.
Patch:          %{name}-remove-unnecessary-languages.patch

# [Fedora-specific] Indicate that the examples depend on GNATcoll Core.
Patch:          %{name}-add-gnatcoll-core-dependency-to-zmq-example.patch

# [Fedora-specific] The gnatpp tool, a source code formatter tool which is part
#   of the now obsolete ASIS-toolset, is not available in Fedora.
Patch:          %{name}-skip-gnatpp-during-generate.patch

# [Fedora-specific] Update the GPRbuild project for building the test suite.
#   Note that we want to run the test suite against the Ada bindings installed
#   in the buildroot and must therefore remove any reference to packages that
#   are only defined in the ZMQ project in the source tree.
#
#   - Remove the `helpers' project; the dependency isn't used by any test.
#   - Update the dependency from GNATcoll to GNATcoll Core.
#   - Remove the compiler switches. They're inherited from the ZMQ project in
#     the source tree. When building the testsuite, we'll use the switches of
#     Fedora instead.
#   - Remove the `Ide' package. The package is inherited from the the ZMQ
#     project in the source tree and isn't needed when packaging the library.
#
Patch:          %{name}-adjust-zmq-tests-project.patch

BuildRequires:  gcc-gnat gprbuild
BuildRequires:  fedora-gnat-project-common
BuildRequires:  zeromq-devel
%if %{with generate}
BuildRequires:  make gcc-g++ sed
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command
%endif
%if %{with check}
BuildRequires:  aunit-devel
BuildRequires:  gnatcoll-core-devel
BuildRequires:  xmlada-devel
%endif

Requires:       zeromq

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
The ZeroMQ lightweight messaging kernel is a library which extends the \
standard socket interfaces with features traditionally provided by specialized \
messaging middleware products. ZeroMQ sockets provide an abstraction of \
asynchronous message queues, multiple messaging patterns, message filtering \
(subscriptions), seamless access to multiple transport protocols and more.

%description %{common_description_en}

This package provides an Ada binding to the ZeroMQ library.

#################
## Subpackages ##
#################

%package devel
Summary:        Development package for the Ada binding for ZeroMQ
License:        MIT AND GPL-2.0-or-later WITH GNAT-exception
# The license is MIT except for:
# - libzmq.gpr.in : GPLv2+ with GNAT runtime exception
# - zmq.gpr.inst  : GPLv2+ with GNAT runtime exception
# - zmq.gpr       : GPLv2+ with GNAT runtime exception
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       zeromq-devel

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the Ada binding for ZeroMQ. It also contains some
code examples.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

# Work with the GPRbuild-project to be used by users of the Ada bindings.
rm examples/zmq-examples.gpr
cp --preserve=timestamp examples/zmq-examples.gpr.inst \
                        examples/zmq-examples.gpr

# libzmq.gpr is needed by zmq.gpr.
cp libzmq.gpr.in libzmq.gpr

# Regenerate the low-level bindings.
%if %{with generate}
make generate
%endif

###########
## Build ##
###########

%build

# Build the library.
gprbuild %{GPRbuild_flags} -XLIBRARY_TYPE=relocatable -P zmq.gpr

#############
## Install ##
#############

%install

# Install the library.
%{GPRinstall} -XLIBRARY_TYPE=relocatable -P zmq.gpr

# Fix up the symlink.
ln --symbolic --force libzmqAda.so.%{upstream_version} \
   %{buildroot}%{_libdir}/libzmqAda.so

# Copy the examples.
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps examples/zmq-examples*.ad* \
                         %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps examples/zmq-examples.gpr \
                         %{buildroot}%{_pkgdocdir}/examples

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
    %{buildroot}%{_GNAT_project_dir}/zmq.gpr
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

cd tests

# Build the test suite.
gprbuild %{GPRbuild_flags} -P zmq-tests.gpr -cargs -fPIE

# Run the test suite.
bin/test_all

%endif

###########
## Files ##
###########

%files
%license COPYING
%{_libdir}/libzmqAda.so.%{upstream_version}

%files devel
%{_GNAT_project_dir}/zmq.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/libzmqAda.so
%{_pkgdocdir}/examples

###############
## Changelog ##
###############

%changelog
%autochangelog
