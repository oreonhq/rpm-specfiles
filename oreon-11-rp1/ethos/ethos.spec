%global source0_hash 39a9a4cfe8a22bc07cb7b1c2e1632235d137d8cb9ee39be80660de7ac069bef6

Name:           ethos
Version:        0.2.2
Release:        %autorelease
Summary:        Flexible and efficient proof checker for SMT solvers

License:        BSD-3-Clause
URL:            https://github.com/cvc5/ethos
VCS:            git:%{url}.git
Source:         %{url}/archive/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
The Ethos checker is an efficient and extensible tool for checking proofs of
Satisfiability Modulo Theories (SMT) solvers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version} -p1

# We want to know about use of deprecated interfaces
sed -i '/Wno-deprecated/d' CMakeLists.txt

# Make sure the bundled copy of drat-trim is not used in the build
rm -fr contrib/drat_trim

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{_vpath_builddir}/src/ethos %{buildroot}%{_bindir}

%check
# Tests spuriously fail when run in parallel
%ctest -j1

%files
%doc AUTHORS NEWS.md README.md user_manual.md
%license COPYING
%{_bindir}/ethos

%changelog
%autochangelog
