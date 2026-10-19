%global source0_hash afb4c4fe0058e34357dd749c904e574aeda62220a3870bd0a275e907a96c3c80
Name:           mock-centos-sig-configs
Version:        0.6.1
Release:        1%{?dist}
Summary:        Mock configs for CentOS SIGs
License:        MIT
URL:            https://pagure.io/centos-sig-hyperscale/mock-centos-sig-configs
Source0:        https://pagure.io/centos-sig-hyperscale/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       mock-core-configs
Enhances:       mock-core-configs
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
This package contains mock configs for various CentOS SIGs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
