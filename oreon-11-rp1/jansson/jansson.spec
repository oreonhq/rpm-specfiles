%global source0_hash f9aa4b3ec8496fee69db94f06f3d76fd4a26b012ee9bf1e917078c2cd2841881
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: jansson
Version: 2.15.1
Release: 1%{?dist}
Summary: C library for encoding, decoding and manipulating JSON
License: MIT
URL: https://github.com/akheron/jansson
Source0: https://github.com/akheron/jansson/releases/download/v%{version}/jansson-%{version}.tar.bz2
Source1: jansson-%{version}.tar.bz2.asc
Source2: jansson-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf

%description
Jansson is a C library for encoding, decoding and manipulating JSON data.

%package devel
Summary: Development files for jansson
Requires: jansson%{?_isa} = %{version}-%{release}
Provides: pkgconfig(jansson)

%description devel
Headers and libraries for developing against jansson.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n jansson-%{version} -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
