%global source0_hash 8d5275577c44f2bd87f6e05dd61971a71c0e56a9cbedf000bd38deadd8b6c1e6

Summary:         Utility to access BitLocker encrypted volumes
Name:            dislocker
Version:         0.7.3
Release:         24%{?dist}
License:         GPL-2.0-or-later
URL:             https://github.com/Aorimn/dislocker
Source0:         https://github.com/Aorimn/dislocker/archive/v%{version}/%{name}-%{version}.tar.gz
# Upstream changes since last release
Patch0:          https://github.com/Aorimn/dislocker/compare/v0.7.3...3e7aea196eaa176c38296a9bc75c0201df0a3679.patch#/dislocker-0.7.3-upstream-changes.patch
# Multibyte character support in passwords, see https://github.com/Aorimn/dislocker/pull/118
Patch1:          https://github.com/Aorimn/dislocker/pull/333.patch#/dislocker-0.7.3-multibyte-support.patch
Requires:        %{name}-libs%{?_isa} = %{version}-%{release}
Requires:        ruby(release)
Requires:        ruby(runtime_executable)
Requires(post):  %{?el8:/usr/sbin/}alternatives
Requires(preun): %{?el8:/usr/sbin/}alternatives
Provides:        %{_bindir}/%{name}
BuildRequires:   cmake
BuildRequires:   gcc
BuildRequires:   mbedtls-devel
BuildRequires:   ruby-devel
BuildRequires:   %{_bindir}/ruby

%description
Dislocker has been designed to read BitLocker encrypted partitions ("drives")
under a Linux system. The driver has the capability to read/write partitions
encrypted using Microsoft Windows Vista, 7, 8, 8.1 and 10 (AES-CBC, AES-XTS,
128 or 256 bits, with or without the Elephant diffuser, encrypted partitions);
BitLocker-To-Go encrypted partitions (USB/FAT32 partitions).

The file name where the BitLocker encrypted partition will be decrypted needs
to be given. This may take a long time, depending on the size of the encrypted
partition. But afterward, once the partition is decrypted, the access to the
NTFS partition will be faster than with FUSE. Another thing to think about is
the size of the disk (same size as the volume that is tried to be decrypted).
Nevertheless, once the partition is decrypted, the file can be mounted as any
NTFS partition and won't have any link to the original BitLocker partition.

%package libs
Summary:         Libraries for applications using dislocker

%description libs
The dislocker-libs package provides the essential shared libraries for any
dislocker client program or interface.

%package -n fuse-dislocker
Summary:         FUSE filesystem to access BitLocker encrypted volumes
Provides:        %{_bindir}/%{name}
Provides:        dislocker-fuse = %{version}-%{release}
Provides:        dislocker-fuse%{?_isa} = %{version}-%{release}
Requires:        %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post):  %{?el8:/usr/sbin/}alternatives
Requires(preun): %{?el8:/usr/sbin/}alternatives
BuildRequires:   fuse-devel

%description -n fuse-dislocker
Dislocker has been designed to read BitLocker encrypted partitions ("drives")
under a Linux system. The driver has the capability to read/write partitions
encrypted using Microsoft Windows Vista, 7, 8, 8.1 and 10 (AES-CBC, AES-XTS,
128 or 256 bits, with or without the Elephant diffuser, encrypted partitions);
BitLocker-To-Go encrypted partitions (USB/FAT32 partitions).

A mount point needs to be given to dislocker-fuse. Once keys are decrypted, a
file named 'dislocker-file' appears into this provided mount point. This file
is a virtual NTFS partition, it can be mounted as any NTFS partition and then
reading from it or writing to it is possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -D WARN_FLAGS="-Wall -Wno-error -Wextra"
%cmake_build

%install
%cmake_install

# Remove standard symlinks due to alternatives
rm -f $RPM_BUILD_ROOT{%{_bindir}/%{name},%{_mandir}/man1/%{name}.1*}

# Clean up files for later usage in documentation
for file in *.md; do mv -f $file ${file%.md}; done
for file in *.txt; do mv -f $file ${file%.txt}; done

%post
alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-file 60

%preun
if [ $1 -eq 0 ]; then
  alternatives --remove %{name} %{_bindir}/%{name}-file
fi

%ldconfig_scriptlets libs

%post -n fuse-dislocker
alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-fuse 80

%preun -n fuse-dislocker
if [ $1 -eq 0 ]; then
  alternatives --remove %{name} %{_bindir}/%{name}-fuse
fi

%files
%{_bindir}/%{name}-bek
%{_bindir}/%{name}-file
%{_bindir}/%{name}-find
%{_bindir}/%{name}-metadata
%{_mandir}/man1/%{name}-file.1*
%{_mandir}/man1/%{name}-find.1*

%files libs
%license LICENSE
%doc CHANGELOG README
%{_libdir}/libdislocker.so.*
# dislocker-find (ruby) fails without this symlink (#1583480)
%{_libdir}/libdislocker.so

%files -n fuse-dislocker
%{_bindir}/%{name}-fuse
%{_mandir}/man1/%{name}-fuse.1*

%changelog
%autochangelog
