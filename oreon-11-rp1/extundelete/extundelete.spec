%global source0_hash a1f9dd61247056d36401ce5d6785e74d08a184340eebd3865c345ddaa93f19f4

Name:           extundelete
Version:        0.2.4
Release:        29%{?dist}
Summary:        Utility to recover deleted files from ext3 and ext4 filesystem

License:        GPL-2.0-or-later
URL:            https://extundelete.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         extundelete-0.2.4-i_size_high.patch

BuildRequires:  gcc-c++
BuildRequires:  e2fsprogs-devel >= 1.41
BuildRequires:  make

%description
extundelete is a utility that can recover deleted files from an ext3 or ext4
partition. extundelete uses the information stored in the partition's journal
to attempt to recover a file that has been deleted from the partition. There is
no guarantee that any particular file will be able to be undeleted, so always
try to have a good backup system in place, or at least put one in place after
recovering your files!

Important: A deleted file can most likely not be recovered on ext4 filesystems
when it has been created using the features "64bit" and/or "metadata_csum". As
extundelete is no longer maintained by upstream, the practical use is limited.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .i_size_high

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README
%{_bindir}/%{name}

%changelog
%autochangelog
