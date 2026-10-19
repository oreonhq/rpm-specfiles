%global source0_hash a2b7811f47b0ddb1f7b1d0aa456f7c1270da70708ce231c2fe054c7199eafa63
%global source1_hash a7f2e9fb89bce75d6aab7f642734b8d742d75563aec404a96468a15de6c92816
Summary:        The GNU disk partition manipulation program
Name:    parted
Version: 3.8
Release:        1%{?dist}
License: GPL-3.0-or-later
URL:     http://www.gnu.org/software/parted
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2: pubkey.phillip.susi
Source3: pubkey.brian.lane
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  check-devel
BuildRequires:  device-mapper-devel
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  libblkid-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-Digest-CRC
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  xfsprogs
# /oreon:deps
%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package devel
Summary:  Files for developing apps which will manipulate disk partitions
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
The GNU Parted library is a set of routines for hard disk partition
manipulation. If you want to develop programs that manipulate disk
partitions and filesystems using the routines provided by the GNU
Parted library, you need to install this package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git_am
# Needed when .am files are modified by a patch
autoreconf -v
iconv -f ISO-8859-1 -t UTF8 AUTHORS > tmp; touch -r AUTHORS tmp; mv tmp AUTHORS

%build

CFLAGS="$RPM_OPT_FLAGS -Wno-unused-but-set-variable"; export CFLAGS
%configure --disable-static --disable-gcc-warnings
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%{__rm} -rf %{buildroot}
%make_install
%{__rm} -rf %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}%{_infodir}/dir
%{__rm} -rf %{buildroot}%{_bindir}/label
%{__rm} -rf %{buildroot}%{_bindir}/disk
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$(pwd)/libparted/.libs:$(pwd)/libparted/fs/.libs
make check
%files -f %{oreon_filedir}/main.list
%files -n parted-devel -f %{oreon_filedir}/parted-devel.list

%changelog

%autochangelog
