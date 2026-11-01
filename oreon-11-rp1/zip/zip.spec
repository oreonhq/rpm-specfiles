%global source0_hash f0e8bb1f9b7eb0b01285495a2699df3a4b766784c1765a8f1aeedf63c0806369
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: zip
Version: 3.0
Release: 1%{?dist}
Summary: Archiver for .zip files
License: Info-ZIP
URL: https://infozip.sourceforge.net/Zip.html
Source0: https://downloads.sourceforge.net/infozip/zip30.tar.gz
Patch0: zip-3.0-exec-shield.patch
Patch1: zip-3.0-currdir.patch
Patch2: zip-3.0-time.patch
Patch3: man.patch
Patch4: zip-3.0-format-security.patch
Patch5: zipnote.patch
Patch6: zip-gnu89-build.patch
Patch7: buffer_overflow.patch
Patch8: zip-3.0-man-strip-extra.patch

Requires: unzip

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
BuildRequires: bzip2-devel
%endif

%description
zip creates PKZIP-compatible zip archives.

%prep
%oreon_sha256
%autosetup -n zip30 -p1

%build
%{_oreon_flags} make -f unix/Makefile \
  prefix=%{_prefix} \
  CFLAGS_NOOPT="-I. -DUNIX %{_oreon_cflags}" \
  generic_gcc

%install
make -f unix/Makefile \
  prefix=%{buildroot}%{_prefix} \
  MANDIR=%{buildroot}%{_mandir}/man1 \
  install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE
