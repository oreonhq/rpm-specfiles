%global source0_hash a1bb836adb6a393f508307699b44af5f4e94c3cd720329e5e7bf9b89d926389c
%bcond check 0
%global goipath         github.com/mvo5/uboot-go
Version:                0.4
%global tag             0.4
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-mvo5-uboot-go-devel < 0-0.9
Obsoletes:      golang-github-mvo5-uboot-go-unit-test-devel < 0-0.9
}
%global common_description %{expand:
Small Go package/app to read/write uboot env files that contain crc32 + 1 byte
padding. Unlike fw_{set,print}env it does not needs a /etc/fw_env.config config
file..}
%global golicenses      COPYING
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Read uboot environment via Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/uboot-go-%{version}.tar.gz
%if %{with check}
%endif
Obsoletes:      golang-github-mvo5-uboot-go < 0-0.9
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/uboot-go %{goipath}
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
