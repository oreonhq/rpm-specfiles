%global source0_hash 3274808584a1c0a214da9fc9377b6a7eb257c9e0a735906c242744e8e9da7d18
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/klauspost/pgzip
Version:                1.2.7
%gometa
%global common_description %{expand:
Go parallel gzip compression/decompression. This is a fully gzip compatible drop
in replacement for "compress/gzip".
This will split compression into blocks that are compressed in parallel. This
can be useful for compressing big amounts of data. The output is a standard gzip
file.
The gzip decompression is modified so it decompresses ahead of the current
reader. This means that reads will be non-blocking if the decompressor can keep
ahead of your code reading from it. CRC calculation also takes place in a
separate goroutine.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go parallel gzip (de)compression
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pgzip-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/klauspost/compress/flate)
BuildRequires:  golang(github.com/klauspost/compress/gzip)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
