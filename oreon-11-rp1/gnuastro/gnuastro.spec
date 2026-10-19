%global source2_hash 81ff537e2dcfcffcb436bfbdffad22ac7d0d15e8c43a3e356ad1eeac0323415a
%global source1_hash b81b34595f9f29baf6989cdc35be3b8db351ffaf823ce5c8c87412d4d5e48e27
%global source0_hash c4e6401eee5d81619b82d8d18a6447851b36e0754118ebf5bdfac7a03194f981
Name: gnuastro
Version: 0.24
Release:        1%{?dist}
Summary:        GNU Astronomy Utilities
License: GPL-3.0-or-later AND FSFAP AND GFDL-1.3-or-later
URL: https://www.gnu.org/software/gnuastro/
Source0:        https://ftp.gnu.org/gnu/gnuastro/%{name}-%{version}.tar.gz
Source1: https://ftp.gnu.org/gnu/gnuastro/%{name}-%{version}.tar.gz.sig
Source2: https://akhlaghi.org/public-pgp-key.txt
Patch0: gnuastro-dont-override-cflags.patch
Patch1: gnuastro-skip-test.patch
Patch2: gnuastro-i686.patch
Patch3: gnuastro-skip-test2.patch
ExcludeArch: %{ix86}
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  cfitsio-devel
BuildRequires:  curl
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  gnulib-devel
BuildRequires:  gpgverify
BuildRequires:  gsl-devel
BuildRequires:  libgit2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  lzip
BuildRequires:  make-devel
BuildRequires:  wcslib-devel
# /oreon:deps
%description
GNU Astronomy Utilities (Gnuastro) is an official GNU package consisting 
of various programs and library functions for the manipulation and 
analysis of astronomical data. All the programs share the same basic 
command-line user interface for the comfort of both the users and developers. 

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
License: GFDL-1.3-or-later
Summary: Documentation files for %{name}
BuildArch: noarch
%description doc
This %{name}-doc package contains the full documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

export CPATH="/usr/include/cfitsio"
%configure --disable-static --disable-rpath
%make_build
%install
export CPATH="/usr/include/cfitsio"
%make_install 
test -f %{buildroot}/%{_infodir}/dir && rm %{buildroot}/%{_infodir}/dir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/%{name}/astscript-fits-view.desktop
export CPATH="/usr/include/cfitsio"
make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n gnuastro-devel -f %{oreon_filedir}/gnuastro-devel.list
%files -n gnuastro-doc -f %{oreon_filedir}/gnuastro-doc.list

%changelog

%autochangelog
