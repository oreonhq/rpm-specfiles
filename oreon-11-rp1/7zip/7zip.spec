%global source0_hash ed087f83ee789c1ea5f39c464c55a5c9d4008deb0efe900814f2df262b82c36e
%global make_opts DEBUG_BUILD=1 DISABLE_RAR=1 LOCAL_FLAGS="%{optflags}" -f makefile.gcc
%global obs_ver 16.03
Name:           7zip
Version:        26.03
Release:        1%{?dist}
Summary:        A file archiver
License:        LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://7-zip.org
Source0:        https://www.7-zip.org/a/7z2501-src.tar.xz#/%{name}-%{version}.tar.xz
Patch:          https://github.com/ip7z/7zip/pull/33.patch#/7z-dont-echo-password.diff
Patch:          7zip-find-so-in-libexec.diff
Provides:       p7zip-plugins = %{version}-%{release}
Obsoletes:      p7zip-plugins < %{obs_ver}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description

%package        reduced
Summary:        Standalone version of 7-Zip console that supports only 7z (reduced version)
%description    reduced

%package        standalone
Summary:        Standalone version of 7-Zip console that supports only some formats
Provides:       p7zip = %{version}-%{release}
Obsoletes:      p7zip < %{obs_ver}
%description    standalone

This version supports only 7z/xz/cab/zip/gzip/bzip2/tar.

%package        standalone-all
Summary:        Standalone version of 7-Zip console that supports all formats
%description    standalone-all

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
sed -i 's/\r$//' CPP/7zip/UI/Console/UserInputUtils.cpp CPP/7zip/UI/Common/ArchiveCommandLine.cpp
%autopatch -p1

rm -rf CPP/7zip/Archive/Rar
rm -f CPP/7zip/Compress/Rar* CPP/7zip/Crypto/Rar* DOC/unRarLicense.txt

# avoid failures due to new warnings in latest GCC
sed -i -e 's|-Werror||' CPP/7zip/7zip_gcc.mak
# from 7zip-find-so-in-libexec.diff
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
%oreon_autofiles 7zip-reduced usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles 7zip-standalone usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles 7zip-standalone-all usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n 7zip-reduced -f %{oreon_filedir}/7zip-reduced.list
%files -n 7zip-standalone -f %{oreon_filedir}/7zip-standalone.list
%files -n 7zip-standalone-all -f %{oreon_filedir}/7zip-standalone-all.list

%changelog

%autochangelog
