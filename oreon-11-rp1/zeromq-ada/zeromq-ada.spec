%global source0_hash 84e3e011a214ac2ccd87e27c2e5a635bb8f58f562bc6cfc21549dc546309ca5a
%bcond check 0
%bcond_without generate
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
URL:            https://zeromq.org
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{upstream_shortcommit}.tar.gz
Patch:          %{name}-remove-unnecessary-languages.patch
Patch:          %{name}-add-gnatcoll-core-dependency-to-zmq-example.patch
Patch:          %{name}-skip-gnatpp-during-generate.patch
Patch:          %{name}-adjust-zmq-tests-project.patch
%if %{with generate}
%endif
%if %{with check}
%endif
Requires:       zeromq
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
The ZeroMQ lightweight messaging kernel is a library which extends the \
standard socket interfaces with features traditionally provided by specialized \
messaging middleware products. ZeroMQ sockets provide an abstraction of \
asynchronous message queues, multiple messaging patterns, message filtering \
(subscriptions), seamless access to multiple transport protocols and more.
# oreon:deps
BuildRequires:  aunit-devel
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-g++
BuildRequires:  gcc-gnat
BuildRequires:  gnatcoll-core-devel
BuildRequires:  gprbuild
BuildRequires:  make
BuildRequires:  python-unversioned-command
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  xmlada-devel
BuildRequires:  zeromq-devel
# /oreon:deps
%description %{common_description_en}

This package provides an Ada binding to the ZeroMQ library.

#################
## Subpackages ##
#################

%package devel
Summary:        Development package for the Ada binding for ZeroMQ
License:        MIT AND GPL-2.0-or-later WITH GNAT-exception
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

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

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

gprbuild %{GPRbuild_flags} -XLIBRARY_TYPE=relocatable -P zmq.gpr
%install
%{GPRinstall} -XLIBRARY_TYPE=relocatable -P zmq.gpr
ln --symbolic --force libzmqAda.so.%{upstream_version} \
   %{buildroot}%{_libdir}/libzmqAda.so
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps examples/zmq-examples*.ad* \
                         %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps examples/zmq-examples.gpr \
                         %{buildroot}%{_pkgdocdir}/examples
%if %{with check}
%global checkroot %{_builddir}/%{name}-%{version}/checkroot
mkdir %{checkroot}  # without --parents to not clobber any upstream directory
cp --recursive %{buildroot}/* %{checkroot}/
%endif
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/zmq.gpr
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

export PATH=%{checkroot}%{_bindir}:$PATH
export LD_LIBRARY_PATH=%{checkroot}%{_libdir}:$LD_LIBRARY_PATH
export GPR_PROJECT_PATH=%{checkroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH
cd tests
gprbuild %{GPRbuild_flags} -P zmq-tests.gpr -cargs -fPIE
bin/test_all
%endif
%files -f %{oreon_filedir}/main.list
%files -n zeromq-ada-devel -f %{oreon_filedir}/zeromq-ada-devel.list

%changelog

%autochangelog
