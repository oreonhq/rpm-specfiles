%global source0_hash 7c3904b9f7ade215fac8815d87d43f8d65ba0dbd69fec16635b0ece459387139

%global dia_datadir %{_datadir}/dia
%global shapes CMOS

Name:           dia-%{shapes}
Version:        0.1
Release:        31%{?dist}
Summary:        Dia CMOS Shapes

License:        GPL-2.0-or-later
URL:            http://dia-installer.de/shapes/cmos/index_en.html
Source0:        http://dia-installer.de/shapes/cmos/cmos.zip

Requires:       dia
BuildArch:      noarch

%description
The following shapes are included in the package:
 * NMOS Transistor
 * PMOS Transistor
 * Ground
 * Vdd

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
