%global source0_hash 413b577afba5370060cf48a11839b9c48c13c3d5f793816bb8d353c9ecf7317a
%global commit  6dfd6684cac5d4838dc7e28dce920c8e074df106
%global date    20211228
%global forgeurl https://github.com/benjaminkiesl/drat2er
Name:           drat2er
Version:        0
Summary:        Proof transformer for propositional logic
%forgemeta
Release:        1%{?dist}
License:        MIT
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{name}-unbundle.patch
Patch:          %{name}-shared.patch
Patch:          %{name}-string-front.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  cli11-static
BuildRequires:  cmake
BuildRequires:  drat-trim-devel
BuildRequires:  drat-trim-tools
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
# /oreon:deps
%description
Drat2er is a tool for transforming proofs that are usually produced by SAT
solvers.  It takes as input a propositional formula (specified in the DIMACS
format) together with a DRAT proof (DRAT is the current standard format for
proofs in SAT solving), and outputs an extended-resolution proof of the
formula in either the TRACECHECK or the DRAT format.  The details of this
proof transformation are described in the paper "Extended Resolution Simulates
DRAT" (IJCAR 2018).  Note that if drat2er is given as input a DRUP proof, then
it transforms this DRUP proof into an ordinary resolution proof.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Headers files and library links for developing applications that use %{name}.

%package        tools
License:        MIT AND BSD-3-Clause
Summary:        Command line interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
This package contains a command line interface to %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p0

# Do not use the bundled libraries
rm -fr third-party

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/%{_lib}
help2man --version-string=%{date} -N -o %{name}.1 \
  -n 'Proof transformer for propositional logic' %{_vpath_builddir}/bin/%{name}
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%files -f %{oreon_filedir}/main.list
%files -n drat2er-devel -f %{oreon_filedir}/drat2er-devel.list
%files -n drat2er-tools -f %{oreon_filedir}/drat2er-tools.list

%changelog

%autochangelog
