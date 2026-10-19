%global source0_hash 1e0a7cdf3f3e1256d2e00d66777addb92a6eaf7ac68f3b8bd56e0701850a8e96
Name:           gram_grep
Summary:        Search text using a grammar, lexer, or straight regex
Version:        0.10.2
Release:        1%{?dist}
License:        BSL-1.0
URL:            https://github.com/BenHanson/gram_grep
Source0:        https://github.com/BenHanson/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        gram_grep.1
Source2:        main-0.9.0.cpp
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  lexertl17-static
BuildRequires:  ninja-build
BuildRequires:  parsertl17-static
BuildRequires:  wildcardtl-static
# /oreon:deps
%description
Search text using a grammar, lexer, or straight regex. Chain searches for
greater refinement.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gram_grep-%{version}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate

# Remove include paths for unbundled header-only library dependencies
sed -r -i 's@^([[:blank:]]*)(include_directories.*"\.\./)@\1# \2@' \
    CMakeLists.txt

%conf
%cmake -GNinja

%build

%cmake_build
%install
install -t '%{buildroot}%{_bindir}' -p -D %{_vpath_builddir}/gram_grep
install -t '%{buildroot}%{_mandir}/man1' -p -D -m 0644 '%{SOURCE1}'
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/gram_grep --help >/dev/null
cp -p '%{SOURCE2}' _x.cpp
assert_same() {
  set -o nounset
  set -o errexit
  if [ "${1}" != "${2}" ]
  then
    cat 1>&2 <<EOF
==== Actual ====
${1}
==== Expected ====
${2}
EOF
    exit 1
  fi
}
expected='_x.cpp:15:#include <lexertl/memory_file.hpp>
_x.cpp:616:    lexertl::memory_file& mf,
_x.cpp:783:    lexertl::memory_file mf(pathname.c_str());
_x.cpp:1348:            lexertl::memory_file& mf ='
assert_same "$(set -o errexit
  %{buildroot}%{_bindir}/gram_grep -Hn -v \
      --flex-regexp "\/\/.*|\/\*(?s:.)*?\*\/" -F memory_file _x.cpp
)" "${expected}"
assert_same "$(set -o errexit
  %{buildroot}%{_bindir}/gram_grep -Hn --config=sample_configs/nosc.g _x.cpp
)" "${expected}"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
