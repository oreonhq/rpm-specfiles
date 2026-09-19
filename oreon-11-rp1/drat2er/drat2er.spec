%global source0_hash 413b577afba5370060cf48a11839b9c48c13c3d5f793816bb8d353c9ecf7317a

# Upstream has not tagged any releases
%global commit  6dfd6684cac5d4838dc7e28dce920c8e074df106
%global date    20211228
%global forgeurl https://github.com/benjaminkiesl/drat2er

Name:           drat2er
Version:        0
Summary:        Proof transformer for propositional logic

%forgemeta

Release:        0.20%{?dist}
License:        MIT
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
# Unbundle the third-party libraries
Patch:          %{name}-unbundle.patch
# Build a shared library instead of a static library
Patch:          %{name}-shared.patch
# Fix a C++ assertion failure due to calling front() on an empty string
Patch:          %{name}-string-front.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  catch-devel
BuildRequires:  cli11-static
BuildRequires:  cmake
BuildRequires:  drat-trim-devel
BuildRequires:  drat-trim-tools
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make

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
# The project itself is MIT.
# The code added by cli11 is BSD-3-Clause.
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

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1 %{buildroot}%{_mandir}/man1

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0{,.*}

%files          devel
%{_includedir}/drat*.h
%{_libdir}/lib%{name}.so

%files          tools
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
