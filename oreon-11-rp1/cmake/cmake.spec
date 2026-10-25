%global source0_hash 643f04182b7ba323ab31f526f785134fb79cba3188a852206ef0473fee282a15
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cmake
Version: 4.1.2
Release: 1%{?dist}
Summary: CMake build system
License: BSD-3-Clause
URL: https://cmake.org/
Source0: https://github.com/Kitware/CMake/releases/download/v%{version}/cmake-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: libuv-devel
BuildRequires: patchelf
%endif

%description
CMake is a build system.

%prep
%oreon_sha256
%autosetup -p1

%build
export CFLAGS="%{_oreon_cflags}"
export CXXFLAGS="%{_oreon_cflags}"
export LDFLAGS="%{_oreon_ldflags}"
./bootstrap --prefix=%{_prefix} --parallel=%{_smp_build_ncpus} --system-libuv -- -DCMAKE_USE_OPENSSL=ON -DCMAKE_SKIP_RPATH=ON
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist
tmp=$(mktemp)
while IFS= read -r line; do
  case "$line" in
    \"*\") printf '%%s\n' "$line" ;;
    *\ *) printf '"%%s"\n' "$line" ;;
    *) printf '%%s\n' "$line" ;;
  esac
done < %{_builddir}/%{name}.files > "$tmp"
mv "$tmp" %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license LICENSE.rst
