%global source0_hash afb4c4fe0058e34357dd749c904e574aeda62220a3870bd0a275e907a96c3c80

Name:           mock-centos-sig-configs
Version:        0.6.1
Release:        %autorelease
Summary:        Mock configs for CentOS SIGs

License:        MIT
URL:            https://pagure.io/centos-sig-hyperscale/mock-centos-sig-configs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
Requires:       mock-core-configs
Enhances:       mock-core-configs

BuildArch:      noarch

%description
This package contains mock configs for various CentOS SIGs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%make_install

%files
%license LICENSE
%doc README.md
%defattr(0644, root, mock)
%config(noreplace) %{_sysconfdir}/mock/*.cfg
%config(noreplace) %{_sysconfdir}/mock/templates/*.tpl

%changelog
%autochangelog
