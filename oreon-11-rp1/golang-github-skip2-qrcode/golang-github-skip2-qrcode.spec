%global source0_hash 35460d655e1bef07615a38d47295bfa39d08310440d2b4a19cd5b0bedd2c8fd9
%bcond check 0
%global goipath         github.com/skip2/go-qrcode
%global commit          da1b6568686e89143e94f980a98bc2dbd5537f13
%gometa
%global common_description %{expand:
QR Code encoder (Go).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        QR Code encoder (Go)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-qrcode-%{commit}.tar.gz
Patch0001:      https://patch-diff.githubusercontent.com/raw/skip2/go-qrcode/pull/53.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0001 -p1

%build

for cmd in qrcode; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
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
