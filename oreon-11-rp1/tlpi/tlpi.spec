%global source0_hash 7bb1155f6a90f382e18eaf961133d4f3b0583afd278416fba97406bdb0c606e2
Name:		tlpi
Version:	260523
Release:        1%{?dist}
Summary:        Utilities to display namespaces and control groups
License:	GPL-3.0-or-later
URL:		https://man7.org/tlpi/index.html
Source0:        https://man7.org/%{name}/code/download/%{name}-%{version}-dist.tar.gz
Patch:		Makefile.patch
Requires:	tlpi-licenses
%global examplesdir %_pkgdocdir/examples
# oreon:deps
BuildRequires:  gcc-go
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libxcrypt-devel
# /oreon:deps
%description
The book The Linux Programming Interface and training courses given by
man7.org are accompanied with a set of code examples. Some of these
examples are useful in their own right. This package includes the
following utilities.
- namespace_of	  Show the namespace memberships of one or more processes
		  in the context of the user or PID namespace
		  hierarchy. See the bundled source code for further
		  documentation.
- view_v2_cgroups Display one or more subtrees in the cgroups v2
		  hierarchy. The following info is displayed for each
		  cgroup: the cgroup type, the controllers enabled in
		  the cgroup, and the process and thread members of
		  the cgroup.
- ns_capable	  Test whether a process (identified by PID)
		  might--subject to LSM (Linux Security Module)
		  checks--have capabilities in a target namespace
		  (identified either by a /proc/PID/ns/xxx file or by
		  the PID of a process that is a member of a user
		  namespace).

		  Usage: ns_capable <source-pid> <namespace-file|target-pid>

In addition there are two small tools that implement special cases of
"namespace_of" usage. They could arguably be simpler to use in those
cases.
- pid_namespaces  Show the PID namespace hierarchy.
- userns_overview Display a hierarchical view of the user namespaces
		  on the system along with the member processes for
		  each namespace.

%package examples
Summary:	Example code from the tlpi package
BuildArch:	noarch
Requires:	tlpi-licenses
%description examples
The book The Linux Programming Interface and training courses given by
man7.org are accompanied with a set of code examples. This package
include these examples in source code form.

The package is probably mostly useful in conjunction with the book.

%package examples-bin
Summary:	Compiled examples from the tlpi package
Recommends:	tlpi-examples = %version-%release
Requires:	tlpi-licenses
%description examples-bin
The book The Linux Programming Interface and training courses given by
man7.org are accompanied with a set of code examples. This package
include the binaries built from these sources. They are installed with
a prefix "tlpi-<dir>" where "<dir>" corresponds to the directory in
the source tree.

The package is probably mostly useful in conjunction with the book.

%package licenses
Summary:	License files from tlpi source
BuildArch:	noarch
Requires:	tlpi-licenses
%description licenses
This package contains the license files from tlpi packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 0 -n tlpi-dist
# seccomp_control/deny_open only builds on x86_64 and aarch64
%ifnarch x86_64 aarch64
sed --in-place /seccomp_control_open/d seccomp/Makefile
%endif

%build

ls --format=single-column --directory [a-z]* > dirs_examples
find $(cat dirs_examples) -type f -printf '%h %f\n' > source_examples
%ifnarch aarch64 riscv64 s390x
%make_build INCLUDE_NONATOMIC_UINT64=true
%else
%make_build
%endif
gccgo -fPIE -pie -o pid_namespaces namespaces/pid_namespaces.go
gccgo -fPIE -pie -o namespaces_of namespaces/namespaces_of.go
gccgo -fPIE -pie -o userns_overview namespaces/userns_overview.go
gccgo -fPIE -pie -o view_v2_cgroups cgroups/view_v2_cgroups.go
%install
install -p -D --target-directory=%buildroot%_bindir \
	pid_namespaces namespaces_of userns_overview view_v2_cgroups \
	namespaces/ns_capable
while read dir file
do  install -p -D --target-directory=%buildroot%examplesdir/$dir \
	--mode=u=rw,go=r $dir/$file
done < source_examples
install -p --target-directory=%buildroot%examplesdir \
    --mode=u=rw,go=r BUILDING CHANGES Makefile Makefile.inc README
find $(cat dirs_examples) -type f -executable -printf '%h %f\n'| \
while read dir file
do  install -p $dir/$file %buildroot%_bindir/tlpi-${dir/\//-}-$file
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tlpi-examples -f %{oreon_filedir}/tlpi-examples.list
%files -n tlpi-examples-bin -f %{oreon_filedir}/tlpi-examples-bin.list
%files -n tlpi-licenses -f %{oreon_filedir}/tlpi-licenses.list

%changelog

%autochangelog
