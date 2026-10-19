%global source0_hash 819064d9b219782e656cfb9710a1763d18e80b1afc66e146c04d2f88d502b79a
%bcond check 0
%global debug_package %{nil}
%ifarch aarch64 armv7hl i686 riscv64
%global gotestflags -short %{gotestflags}
%endif
%global goipath         github.com/klauspost/compress
Version:                1.20.1
%gometa -L
%global common_description %{expand:
This package is based on an optimized Deflate function, which is used by
gzip/zip/zlib packages.
It offers slightly better compression at lower compression settings, and up to
3x faster encoding at highest compression level.}
%global golicenses      LICENSE snappy/LICENSE snappy/xerial/LICENSE\\\
                        s2/LICENSE gzhttp/LICENSE
%global godocs          SECURITY.md README.md snappy/CONTRIBUTORS\\\
                        snappy/README.md snappy/AUTHORS\\\
                        snappy/xerial/README.md dict/README.md\\\
                        huff0/README.md s2/README.md gzhttp/README.md\\\
                        zstd/README.md fse/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Optimized Go Compression Packages
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/compress-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep -A

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
