%global source0_hash 71132a3fb71e68245b8f2ac4e9e97137d3e5c02f415636eb508ae607bc01add7
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gettext
Version: 1.0
Release: 1%{?dist}
Summary: Translation tools and runtime for GNU gettext
License: GPL-3.0-or-later AND LGPL-2.1-or-later
URL: https://www.gnu.org/software/gettext/
Source0: https://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
Source1: gettext-%{version}.tar.xz.sig
Source2: gettext-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: libxml2-devel
BuildRequires: libunistring-devel
BuildRequires: ncurses-devel
BuildRequires: patchelf

%description
GNU gettext provides tools for writing and handling translated messages,
including msgfmt, xgettext, msgmerge, autopoint and the libintl macros.

%package devel
Summary: Development files for gettext
Requires: gettext%{?_isa} = %{version}-%{release}
Provides: gettext-libs = %{version}-%{release}
Provides: gettext-autopoint = %{version}-%{release}

%description devel
Headers, libraries and pkg-config files for building against gettext.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n gettext-%{version} -p1

%build
%oreon_configure --disable-static --disable-java --disable-csharp --disable-openmp --without-emacs --without-git --disable-rpath
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_datadir}/doc/gettext %{buildroot}%{_datadir}/doc/libtextstyle %{buildroot}%{_datadir}/doc/libasprintf
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
