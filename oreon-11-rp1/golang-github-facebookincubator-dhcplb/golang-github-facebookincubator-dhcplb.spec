%global source0_hash 56d1678aa856ee4e05e8c2f66ae04e152e7a8d07e8c8afaf7bf5f4d36146d2d7
%bcond check 0
%global goipath         github.com/facebookincubator/dhcplb
%global commit          c9f4bc7902fc2c2604433b87c0e8ace8255c601b
%gometa -f
%global common_description %{expand:
Dhcplb is Facebook's implementation of a load balancer for DHCP.}
%global golicenses      LICENSE
%global godocs          docs AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Facebook's implementation of a load balancer for DHCP
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/dhcplb-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       dhcplb
Summary:        Facebook's implementation of a load balancer for DHCP
BuildArch:      noarch

%description -n dhcplb
Facebook's implementation of a load balancer for DHCP

%description %{common_description}

%package -n     dhcplb
Summary:        Facebook's implementation of a load balancer for DHCP
%description -n dhcplb %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/dhcplb %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles dhcplb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n dhcplb -f %{oreon_filedir}/dhcplb.list

%changelog

%autochangelog
