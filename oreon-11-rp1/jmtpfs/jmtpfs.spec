%global source0_hash c0cacc4751c586a3b2b0fcd9c98dae4810a5d44f3eb9d2870868a15eeb696883

Summary:        FUSE and libmtp based filesystem for accessing MTP devices
Name:           jmtpfs
Version:        0.5
Release:        14%{?dist}
License:        GPL-3.0-only
URL:            https://github.com/JasonFerrara/jmtpfs/
Source0:        https://github.com/JasonFerrara/jmtpfs/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        jmtpfs.1
Patch0:         https://github.com/JasonFerrara/jmtpfs/commit/840db07c39d95415c493170bf6513db4cd46490b.patch#/jmtpfs-0.5-exception.patch
Requires:       %{_bindir}/fusermount
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  fuse-devel >= 2.6
BuildRequires:  file-devel
BuildRequires:  libmtp-devel >= 1.1.0

%description
jmtpfs is a FUSE and libmtp based filesystem for accessing MTP (Media
Transfer Protocol) devices. It was specifically designed for exchanging
files between Linux systems and newer Android devices that support MTP
but not USB Mass Storage.

The goal is to create a well behaved filesystem, allowing tools like
find and rsync to work as expected. MTP file types are set automatically
based on file type detection using libmagic. Setting the file appears to
be necessary for some Android apps, like Gallery, to be able to find and
use the files.

Since it is meant as an Android file transfer utility, the playlists and
other non-file based data are not supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .exception

%build
%configure
%make_build

%install
%make_install

install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
