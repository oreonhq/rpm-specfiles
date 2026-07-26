%global source0_hash b2f63f229274437a043c9454f18e82c46d8bcaefdf943305f4e9fcb7eec1a634

%global octpkg zmat

Name:           octave-%{octpkg}
Version:        0.9.8
Release:        19%{?dist}
Summary:        A portable data compression/decompression toolbox for MATLAB/Octave
# Automatically converted from old format: GPLv3+ or BSD - review is highly recommended.
License:        GPL-3.0-or-later OR LicenseRef-Callaway-BSD
URL:            https://github.com/fangq/zmat
Source0:        https://github.com/fangq/zmat/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Patch0:         zmat-0.9.8-Octave7.patch
BuildRequires:  make
BuildRequires:  octave-devel zlib gcc-c++

Requires:       octave zlib
Requires(post): octave
Requires(postun): octave

%description
ZMat is a portable mex function to enable zlib/gzip/lzma/lzip/lz4/lz4hc 
based data compression/decompression and base64 encoding/decoding support 
in MATLAB and GNU Octave. It is fast and compact, can process a large 
array within a fraction of a second. Among the 6 supported compression 
methods, lz4 is the fastest for compression/decompression; lzma is the 
slowest but has the highest compression ratio; zlib/gzip have the best 
balance between speed and compression time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{octpkg}-%{version} -S patch -p1

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: ZMat is a portable mex function to enable zlib/gzip/lzma/lzip/lz4/lz4hc 
 based data compression/decompression and base64 encoding/decoding support 
 in MATLAB and GNU Octave. It is fast and compact, can process a large 
 array within a fraction of a second. Among the 6 supported compression 
 methods, lz4 is the fastest for compression/decompression; lzma is the 
 slowest but has the highest compression ratio; zlib/gzip have the best 
 balance between speed and compression time.

Categories: Zip
EOF

cat > INDEX << EOF
zmat >> ZMat
ZMat
 zmat
 zipmat
EOF

mkdir -p inst/
mv *.m inst/

%build
cd src
make clean
make oct CFLAGS="%{optflags}"
cd ../
mv *.mex inst/
rm -rf src
%octave_pkg_build

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc example
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.mex
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
%autochangelog
