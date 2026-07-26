%global source0_hash 7ab150a16fa78ea76e9fd58ef88922c03eca2334c023b8d9bc94755fdde522c7

# This package builds a header-only lib, but has some testsuite to check
# the headers' function.  For this reason the main-pkg is build arched
# and produces a noarched subpkg, only.  There is no binary-compiled
# bits and therefore no debuginfo generated.
%global debug_package %{nil}

# Common summary and description.
%global common_sum  Portable and easy to integrate C directory and file reader
%global common_desc \
Lightweight, portable and easy to integrate C directory and file reader. \
TinyDir wraps dirent for POSIX and FindFirstFile for Windows.

Name:           tinydir
Version:        1.2.5
Release:        11%{?dist}
Summary:        %{common_sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cxong/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Testsuite
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
%{common_desc}

%package devel
Summary:        %{common_sum} (header-only)
Provides:       %{name}-static == %{version}-%{release}

BuildArch:      noarch

%description devel
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
# Make testsuite more verbose on failures.
export CTEST_OUTPUT_ON_FAILURE=1

for d in samples tests; do
  mkdir -p %{_target_platform}_${d}
  pushd %{_target_platform}_${d}
  # I'm intentionally not using the %%cmake-macro here.  This builds
  # no installed binaries, just the testsuite.  Building the tests
  # with system-flags enabled will lead to a bunch of errors during
  # compilation.
  cmake3 -DCMAKE_VERBOSE_MAKEFILE=ON ../${d}
  popd
  %make_build -C %{_target_platform}_${d}
done

%install
mkdir -p %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_includedir}

# Install headers.
install -pm 0644 %{name}.h %{buildroot}%{_includedir}

# Install pkg-config file.
cat << EOF > %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}

includedir=%{_includedir}

Name: %{name}
Version: %{version}
Description: %{common_sum}
EOF

# Clean-up for including samples in %%doc.
rm -f samples/{.gitignore,CMakeLists.txt}

%check
pushd %{_target_platform}_tests
ctest3
popd

%files devel
%license COPYING
%doc samples/ package.json README.md
%{_includedir}/%{name}.h
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
