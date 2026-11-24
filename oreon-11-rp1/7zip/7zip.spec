# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ef27b9c0d328dc3d44e0e74006247e4b9dd91665b2f93f35c8a873bc9068559c
%global source1_hash f999f0deb5822e2cf282e0caf00df21e3f32c8d8dd03100d26f3bfdf599a351b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond github_source 0

%global make_opts DEBUG_BUILD=1 DISABLE_RAR=1 LOCAL_FLAGS="%{optflags}" -f makefile.gcc
%global obs_ver 16.03
 
Name:           7zip
Version:        26.06
Release:        %{autorelease}
Summary:        A file archiver

License:        LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://7-zip.org
%if %{with github_source}
Source0:        https://github.com/ip7z/7zip/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.zst
Source2:        strip-rar-support.sh
%else
Source0:        %{name}-%{version}.tar.zst
Source1:        strip-rar-support.sh
%endif
Patch0:         7z-dont-echo-password.diff
Patch1:         7zip-find-so-in-libexec.diff

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  make

Provides:       p7zip-plugins = %{version}-%{release}
Obsoletes:      p7zip-plugins < %{obs_ver}

%global _description %{expand:
7-Zip is a file archiver with a high compression ratio. The main features
of 7-Zip are:

* High compression ratio in 7z format with LZMA and LZMA2 compression
* Supported formats:
  * Packing / unpacking: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM
  * Unpacking only: AR, ARJ, CAB, CHM, CPIO, CramFS, DMG, EXT, FAT,
    GPT, HFS, IHEX, ISO, LZH, LZMA, MBR, MSI, NSIS, NTFS, QCOW2,
    RPM, SquashFS, UDF, UEFI, VDI, VHD, VMDK, WIM, XAR and Z.
* For ZIP and GZIP formats, 7-Zip provides a compression ratio that is
  2-10 % better than the ratio provided by PKZip and WinZip
* Strong AES-256 encryption in 7z and ZIP formats
* Powerful command line version}

%description %{_description}

%package        reduced
Summary:        Standalone version of 7-Zip console that supports only 7z (reduced version)

%description    reduced %{_description}

%package        standalone
Summary:        Standalone version of 7-Zip console that supports only some formats
Provides:       p7zip = %{version}-%{release}
Obsoletes:      p7zip < %{obs_ver}

%description    standalone %{_description}

This version supports only 7z/xz/cab/zip/gzip/bzip2/tar.

%package        standalone-all
Summary:        Standalone version of 7-Zip console that supports all formats

%description    standalone-all %{_description}

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1

sed -i -e 's|-Werror||' CPP/7zip/7zip_gcc.mak
sed -i -e 's|__Z7_PREFIX__|%{_prefix}|g' CPP/7zip/UI/Common/ArchiveCommandLine.cpp

%build
%make_build %make_opts -C CPP/7zip/Bundles/Format7zF/

%make_build %make_opts LOCAL_FLAGS="%{optflags} -DZ7_EXTERNAL_CODECS" -C CPP/7zip/UI/Console/

%make_build %make_opts -C CPP/7zip/Bundles/Alone/

%make_build %make_opts -C CPP/7zip/Bundles/Alone7z/

%make_build %make_opts -C CPP/7zip/Bundles/Alone2/

%install
install -Dpm 755 ./CPP/7zip/UI/Console/_o/7z %{buildroot}%{_bindir}/7z
install -Dpm 755 ./CPP/7zip/Bundles/Format7zF/_o/7z.so %{buildroot}%{_libexecdir}/%{name}/7z.so
install -Dpm 755 ./CPP/7zip/Bundles/Alone/_o/7za %{buildroot}%{_bindir}/7za
install -Dpm 755 ./CPP/7zip/Bundles/Alone7z/_o/7zr %{buildroot}%{_bindir}/7zr
install -Dpm 755 ./CPP/7zip/Bundles/Alone2/_o/7zz %{buildroot}%{_bindir}/7zz

%files
%license DOC/License.txt DOC/copying.txt
%doc DOC/readme.txt DOC/7zC.txt DOC/7zFormat.txt DOC/lzma.txt 
%{_bindir}/7z
%{_libexecdir}/%{name}/

%files reduced
%license DOC/License.txt DOC/copying.txt
%{_bindir}/7zr

%files standalone
%license DOC/License.txt DOC/copying.txt
%{_bindir}/7za

%files standalone-all
%license DOC/License.txt DOC/copying.txt
%{_bindir}/7zz

%changelog
%autochangelog
