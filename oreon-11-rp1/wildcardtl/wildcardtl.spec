%global source0_hash 5f463f591dc7e517cfb441dd790a1aeb255bee0b4ee6030855889ee5b8ab233b

Name:           wildcardtl
Summary:        Wildcard template library
Version:        1.0.0
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/wildcardtl
Source:         %{url}/archive/%{version}/wildcardtl-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  dos2unix

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}

%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library:
Provides:       wildcardtl-static = %{version}-%{release}

%description devel %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wildcardtl-%{version}
# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix

# Nothing to build

%install
install -d '%{buildroot}%{_includedir}'
cp -rvp include/wildcardtl '%{buildroot}%{_includedir}/'

%check
%set_build_flags
# Compile-and-link “smoke test”:
cat > smoke_test.cpp <<'EOF'
#include "wildcardtl/wildcard.hpp"
int main(int, char*[]) { return 0; }
EOF
${CXX} -I"${PWD}/include" ${CPPFLAGS} ${CXXFLAGS} -o smoke_test ${LDFLAGS} \
    smoke_test.cpp

%files devel
%license include/wildcardtl/licence_1_0.txt
%doc README.md

%{_includedir}/wildcardtl/

%changelog
%autochangelog
