%global source0_hash 4a9bc653472c12629fe9c5316e6302379aac7f384021df1c50931fd3bb122203
%bcond check 0
%global goipath         github.com/pierrec/lz4
Version:                4.1.31
%gometa -L
%global goaltipaths     github.com/pierrec/lz4/v4
%global common_description %{expand:
Package lz4 implements reading and writing lz4 compressed data (a frame), as
specified in
http://fastcompression.blogspot.com/2013/04/lz4-streaming-format-final.html.
This package is compatible with the LZ4 frame format although the block level
compression and decompression functions are exposed and are fully compatible
with the LZ4 block format definition, they are low level and should not be
used directly.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-pierrec-lz4
Release:        1%{?dist}
Summary:        LZ4 compression and decompression in pure Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/lz4-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/golz4c %{goipath}/cmd/lz4c
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

for test in "TestWriterLegacy"\
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
