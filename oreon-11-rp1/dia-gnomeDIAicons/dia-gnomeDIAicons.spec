%global source0_hash 96fcd19e368b67dc26e985ae445c72f28be6ff5f484d13bb320fceeccb5dfbf6

Name:           dia-gnomeDIAicons
Version:        0.1
Release:        29%{?dist}
Summary:        GNOME-based network icon shapes for the Dia diagram editor
# https://web.archive.org/web/20240520111753/https://gnomediaicons.sourceforge.net/
License:        GPL-3.0-only
URL:            https://gnomediaicons.sourceforge.net/
Source0:        https://gnomediaicons.sourceforge.net/files/rib-network-v%{version}.tar.gz
BuildArch:      noarch
Requires:       dia

%description
Network icon shapes, based on GNOME Gorilla's theme, for the Dia
diagram editor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c diaicons

%build

%install
mkdir -p %{buildroot}%{_datadir}/dia/{shapes/RIB-Network,sheets}/
install -p -m 0644 shapes/RIB-Network/* %{buildroot}%{_datadir}/dia/shapes/RIB-Network/
install -p -m 0644 sheets/rib_network.sheet %{buildroot}%{_datadir}/dia/sheets/rib_network.sheet

%files
%{_datadir}/dia/shapes/RIB-Network/
%{_datadir}/dia/sheets/rib_network.sheet

%changelog
%autochangelog
