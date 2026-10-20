%global source0_hash 4ce24038fd4221e0d13bc1a2de7a4db56e90b92b3bf75321f6c14be73f65de4b
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xz
Version: 5.8.4
Release: 1%{?dist}
Summary: XZ Utils
License: 0BSD AND GPL-3.0-or-later
URL: https://tukaani.org/xz/
Source0: https://github.com/tukaani-project/xz/releases/download/v%{version}/xz-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
XZ Utils provide a general-purpose data-compression library plus command-line tools. The native file format is the .xz format, but also the legacy .lzma format is supported. The .xz format supports multiple compression algorithms, which are called "filters" in the context of XZ Utils. The primary filter is currently LZMA2. With typical files, XZ Utils create about 30 % smaller files than gzip.

%package devel
Summary: XZ Utils
Requires: xz%{?_isa} = %{version}-%{release}
Provides: pkgconfig(liblzma)

%description devel
XZ Utils provide a general-purpose data-compression library plus command-line tools. The native file format is the .xz format, but also the legacy .lzma format is supported. The .xz format supports multiple compression algorithms, which are called "filters" in the context of XZ Utils. The primary filter is currently LZMA2. With typical files, XZ Utils create about 30 % smaller files than gzip.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
