%global source0_hash 86a79994cd32d8629d7eb5fe8f3a8e57daed3c64ead1c8fe84838451c0869533
%bcond check 0
%global goipath         github.com/vbatts/tar-split
Version:                0.11.2
%gometa
%global common_description %{expand:
Pristinely disassembling a tar archive, and stashing needed raw bytes and
offsets to reassemble a validating original archive.}
%global golicenses      LICENSE
%global godocs          README.md README-tar-split.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Checksum-reproducible tar archives (utility/library)
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/tar-split-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv cmd/tar-split/README.md README-tar-split.md

%build

%gobuild -o %{gobuilddir}/bin/tar-split %{goipath}/cmd/tar-split
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
