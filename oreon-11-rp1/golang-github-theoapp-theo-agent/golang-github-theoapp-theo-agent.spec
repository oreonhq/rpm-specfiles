%global source0_hash 53241b088be82ca2bac6ff62b28172173c6a39e61b4f037d01d83dfc9b81d78f
%bcond check 0
%global goipath         github.com/theoapp/theo-agent
Version:                0.15.0
%gometa -f
%global common_description %{expand:
theo-agent is the command line program used to fetch authorized_keys from a
Theo server.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Theo authorized keys manager agent
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/theo-agent-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%package -n       theo-agent
Summary:        Theo authorized keys manager agent
BuildArch:      noarch

%description -n theo-agent
Theo authorized keys manager agent

%description %{common_description}

%package -n     theo-agent
Summary:        Theo authorized keys manager agent
Recommends:     openssh-server
%description -n theo-agent %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

export LDFLAGS="-X %{goipath}/common.NAME=theo-agent -X %{goipath}/common.VERSION=%{version} -X %{goipath}/common.BUILT=$(date -u +%%Y-%%m-%%dT%%H:%%M:%%S%%z)"
%gobuild -o %{gobuilddir}/bin/theo-agent %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/theo-agent.conf
install -d -m 0755 %{buildroot}%{_sysconfdir}/theo-agent
%oreon_autofiles theo-agent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%pre

%sysusers_create_compat %{SOURCE1}
%files -f %{oreon_filedir}/main.list
%files -n theo-agent -f %{oreon_filedir}/theo-agent.list

%changelog

%autochangelog
