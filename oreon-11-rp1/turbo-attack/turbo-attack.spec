%global source0_hash 8f8b2bd3b34dd131f34d5ec4d8acca2cdb238504677e444773a3479d4c25275b
%bcond check 0
%global goipath         github.com/mytechnotalent/turbo-attack
Version:                0.1.0
%global tag             0.1.0
%gometa -L -f
%global common_description %{expand:
A turbo traffic generator pentesting tool to generate random traffic with
random mac and ip addresses in addition to random sequence numbers to a
particular ip and port.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           turbo-attack
Release:        1%{?dist}
Summary:        A turbo traffic generator pentesting tool
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

# Fix wrong executable name in usage message
sed -i "s|turbo-attack_010_linux_arm64|turbo-attack|" $(find . -name "*.go")

%build

%gobuild -o %{gobuilddir}/bin/turbo-attack %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d routine -d sudo
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
