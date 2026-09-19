%global source0_hash 5af7fa42b39987938b40d2ac716a01325e8a3b0b8e75e2503b1ca7531e287d97

%global debug_package %{nil}
%global middle_release 1

%bcond check 0
%bcond_with doc

ExclusiveArch: %{power64} x86_64 aarch64

%if 0%{?middle_release}
%global  commit      bb2eebb2de8a556661c00ba3c5b4c33b7c2c7a25
%global  date        .20250414git
%global  shortcommit %(c=%{commit}; echo ${c:0:7})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif

Name:      sdsl-lite
Summary:   SDSL v3 - Succinct Data Structure Library
Version:   3.0.3
Release:   6%{date}%{shortcommit}%{?dist}
License:   BSD-3-Clause
URL:       https://github.com/xxsds/%{name}
Source0:   https://github.com/xxsds/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: gcc, gcc-c++
BuildRequires: cmake
BuildRequires: cereal-devel >= 1.3.2
BuildRequires: gtest-devel >= 1.13.0
BuildRequires: texlive-endnotes

Patch0: %{name}-unbundle_libraries.patch

%description
The Succinct Data Structure Library (SDSL) is a powerful and flexible C++11
library implementing succinct data structures.
In total, the library contains the highlights of 40 research publications.
Succinct data structures can represent an object (such as a bitvector or a tree)
in space close to the information-theoretic lower bound of the object while
supporting operations of the original object efficiently.
The theoretical time complexity of an operation performed on the classical
data structure and the equivalent succinct data structure are
(most of the time) identical.

%package devel
Summary: SDSL v3 - Succinct Data Structure Library
Requires: cmake >= 3.13
Requires: cereal-devel%{?_isa} >= 1.3.2
Obsoletes: %{name}-doc < 0:3.0.3-6

%description devel
Developer files for SDSL 3, in the form for C header files.

%if %{with doc}
%package doc
Summary: SDSL v3 HTML/Latex documentation
BuildRequires: doxygen
BuildArch: noarch

%description doc
SDSL v3 HTML/Latex documentation.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sdsl-lite-%{commit} -N

%patch -P 0 -p1 -b .backup

%build
%cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_BUILD_TYPE:STRING=Release \
       -DSDSL_HEADER_TEST:BOOL=OFF -DGENERATE_DOC:BOOL=OFF -DUSE_LIBCPP:BOOL=OFF -DSDSL_CEREAL=1 \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build

%install
mkdir -p %{buildroot}%{_prefix}
cp -a include %{buildroot}%{_prefix}/

rm -f %{buildroot}%{_includedir}/sdsl/.gitignore

%if %{with check}
%check
# Test excluded by upstream
%ctest -- -E 'k2-treap-test_k2-0.1.0.0'
%endif

%if %{with doc}
%files doc
%doc %__cmake_builddir/extras/docs/html
%doc %__cmake_builddir/extras/docs/latex
%endif

%files devel
%license LICENSE
%{_includedir}/sdsl/

%changelog
%autochangelog
