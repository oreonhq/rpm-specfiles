%global source0_hash 07beb4244df92246559c53c4d7574a9e8f3f12fb0d452185e96009c8483104cf

%global dia_datadir %{_datadir}/dia
%global shapes Digital

Name:           dia-%{shapes}
Version:        0.1
Release:        31%{?dist}
Summary:        Dia Digital IC logic shapes

License:        GPL-2.0-or-later
URL:            http://dia-installer.de/shapes/digital/index_en.html
Source0:        http://dia-installer.de/shapes/digital/digital.zip

Requires:       dia
BuildArch:      noarch

%description
The following shapes are included in the package:
 * Buffer
 * Inverter
 * AND
 * NAND
 * OR
 * NOR
 * XOR
 * XNOR
 * Multiplexer/Demultiplexer
 * Adder/Subtractor/Multiplier/Divider
 * Register
 * Connection Point

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{dia_datadir}/sheets
cp -p sheets/%{shapes}.sheet %{buildroot}%{dia_datadir}/sheets
cp -pr shapes %{buildroot}%{dia_datadir}

%files
%doc COPYING
%{dia_datadir}/sheets/%{shapes}.sheet
%{dia_datadir}/shapes/%{shapes}/

%changelog
%autochangelog
