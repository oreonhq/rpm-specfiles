%global source0_hash b1311e5e749917c6a26e59ab1deadf56ccb8f71cc105355f511323b36501f968
Name:           shigofumi
Version:        0.9
Release:        1%{?dist}
Summary:        Command line client for accessing the Czech Data Boxes
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-1.0-or-later WITH Autoconf-exception-generic AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP AND LicenseRef-Fedora-Public-Domain
URL:            http://xpisar.wz.cz/%{name}/
Source0:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
Patch0:         shigofumi-0.9-Fix-building-with-GCC-12.patch
Patch1:         shigofumi-0.9-Fix-two-use-after-frees-when-handling-XML-ISDS-docum.patch
Patch2:         shigofumi-0.9-Fix-building-with-libxml2-2.12.0.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libisds)
BuildRequires:  readline-devel
# /oreon:deps
%description
This is Shigofumi, an ISDS (Informační systém datových schránek / Data Box
Information System) client.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build

%configure \
    --disable-debug \
    --enable-doc \
    --enable-fatalwarnings \
    --enable-largefile \
    --enable-nls \
    --disable-rpath \
    --enable-xattr
%{make_build}
%install
%{make_install}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
