%global source0_hash 6ad984aeed60d846d391c8563cbf76f227df5a32a3a923044368b054a26ea18b
%bcond check 0
%global goipath         github.com/fernet/fernet-go
%global commit          eff2850e60014b3643d850a51c69482d3a8352b1
%gometa
%global common_description %{expand:
Fernet takes a user-provided *message* (an arbitrary sequence of bytes), a key
(256 bits), and the current time, and produces a token, which contains the
message in a form that can't be read or altered without the key.}
%global golicenses      License
%global godocs          Readme
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Generate and verify HMAC-based authentication tokens
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/fernet-go-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
