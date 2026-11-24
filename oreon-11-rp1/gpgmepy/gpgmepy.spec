# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 07e1265648ff51da238c9af7a18b3f1dc7b0c66b4f21a72f27c74b396cd3336d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           gpgmepy
Epoch:          1
Version:        2.0.0
Release:        1%{?dist}
Summary:        Python bindings for GPGME
License:        LGPL-2.1-or-later
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Patch0:         0001-Drop-Python-2-compatibility.patch
BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gpgme) >= %{version}

%description
Python bindings to the GPGME API of the GnuPG cryptography library.

%package -n python3-gpg
Summary:        Python bindings for GPGME

%description -n python3-gpg
Python bindings to the GPGME API of the GnuPG cryptography library.

%prep
%oreon_sha256
%autosetup -p1 -S gendiff

%generate_buildrequires
%pyproject_buildrequires

%build
%ifarch %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}
sed -i "s|^gpgme_h = ''|gpgme_h = '/usr/include/gpgme-%{__isa_bits}.h'|" setup.py.in
%endif
%configure
mv src gpg
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gpg

%check
ln -s build python3-gpg
cd tests
make check

%files -n python3-gpg -f %{pyproject_files}
%doc AUTHORS ChangeLog NEWS README
%license COPYING*

%changelog
%autochangelog
