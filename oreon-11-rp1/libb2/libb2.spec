%global source0_hash 53626fddce753c454a3fea581cbbc7fe9bbcf0bc70416d48fdbbf5d87ef6c72e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libb2
Version: 0.98.1
Release: 1%{?dist}
Summary: BLAKE2 hash library
License: CC0-1.0
URL: https://github.com/BLAKE2/libb2
Source0: https://github.com/BLAKE2/libb2/releases/download/v%{version}/libb2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf%endif

%description
BLAKE2 hash library

%package devel
Summary: BLAKE2 hash library
Requires: libb2%{?_isa} = %{version}-%{release}

%description devel
BLAKE2 hash library

%prep
%oreon_sha256
%autosetup -n libb2-0.98.1 -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
