%global source0_hash 0c8ee6c48c37a910bd06605685655a34435a7bb5c786b1b8b6a9a1dea9ca31e2

%bcond_without docs

%global forgeurl https://github.com/ddinu/observable
%global commit ae3a59cc65c1cb65d27827adc4c1ef5a37298cb7
%forgemeta

%global common_description %{expand:
Observable provides generic observable objects for C++. Write declarative,
reactive expressions or just implement the observer pattern.}

%global debug_package %{nil}

Name:           observable
Version:        0
Release:        %autorelease
Summary:        Generic observable objects and reactive expressions for C++

License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         observable-use-system-catch.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  catch2-devel
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
%endif

%description
%{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{common_description}

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}

%description    doc
This package contains documentation for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# remove bundled version of catch
rm -r vendor

%build
%cmake
%cmake_build
%if %{with docs}
doxygen docs/doxygen
sphinx-build-3 docs/sphinx doc
rm -r doc/.doctrees
%endif

%install
# manually install the headers as the cmake install isn't useful
mkdir -p %{buildroot}%{_includedir}/observable
cp -pr observable/include/observable/* %{buildroot}%{_includedir}/observable/

%check
%ctest

%files devel
%license LICENSE.txt
%doc README.rst
%{_includedir}/observable

%if %{with docs}
%files doc
%license LICENSE.txt
%doc doc html
%endif

%changelog
%autochangelog
