%global source0_hash bf7531efb8f9d33f2b25b2ef2cbdf082a3a9dc8388acd99d0152552dbf717bff
%bcond check 1
%global goipath         github.com/cloudflare/redoctober
%global commit          6a74ccc611f655e1ee9a648062a6ececfb6f2bb8
%gometa
%global common_description %{expand:
Red October is a software-based two-man rule style encryption and decryption
server.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go server for two-man rule style file encryption and decryption
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/redoctober-%{commit}.tar.gz
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

%gobuild -o %{gobuilddir}/bin/redoctober %{goipath}
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
