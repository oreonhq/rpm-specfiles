%global source0_hash c61d4909747b7404bda9341aa042766435452cb8f5563eb1ab2d0ca1da9cb7d1

Name:           sysreporter
Version:        3.0.4
Release:        20%{?dist}
Summary:        Basic system reporter with emailing
License:        MIT
URL:            https://github.com/onesimus-systems/sysreporter
Source0:        https://github.com/onesimus-systems/sysreporter/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
Requires: sysstat

%description
Basic system reporter with emailing

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sysreporter-3.0.4

%build

%install
%__make install DESTDIR="%{buildroot}" prefix="/usr"

%files
%license LICENSE.md
%doc README.md
%{_bindir}/sysreport
%config(noreplace) %{_sysconfdir}/%name
%{_mandir}/*

%changelog
%autochangelog
