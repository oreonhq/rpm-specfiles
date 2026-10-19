%global source0_hash 512c927e8c969132db5d60c1628e1bb241cc960785ead86ab94f15e64048c804
%bcond check 0
%global goipath         github.com/etcd-io/gofail
%global commit          ad7f989257ca7de90de65657c9748a3108b1460f
%gometa
%global common_description %{expand:
Failpoints for Go.}
%global golicenses      LICENSE NOTICE
%global godocs          examples README.md code-of-conduct.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Failpoints for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gofail-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/gofail %{goipath}
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
