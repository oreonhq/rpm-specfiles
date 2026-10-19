%global source0_hash e2785f5c0fcab0ad1ec02396e38b265c216c1e4096049347f039a16be5b7b82d
%bcond check 0
%global goipath         github.com/colinmarc/hdfs/v2
Version:                2.4.0
%gometa -f
%global common_description %{expand:
This is a native golang client for hdfs. It connects directly to the namenode
using the protocol buffers API.
It tries to be idiomatic by aping the stdlib os package, where possible, and
implements the interfaces from it, including os.FileInfo and os.PathError.}
%global golicenses      LICENSE.txt
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Native go client for HDFS
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/colinmarc/hdfs/archive/v%{version}/hdfs-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

export LDFLAGS="-X main.version=%{version} "
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
