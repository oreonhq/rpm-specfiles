%global source0_hash 9813cd5e885df9c481f07af02263e674021a42e2653003f11ff3e6a1f7ee44d9

%global dia_datadir %{_datadir}/dia
%global shapes electric2

Name:           dia-%{shapes}
Version:        0.1
Release:        31%{?dist}
Summary:        Dia Digital IC logic shapes

License:        GPL-2.0-or-later
URL:            http://dia-installer.de/shapes/electric2/index.html.en
Source0:        http://dia-installer.de/shapes/electric2/electric2.zip

Requires:       dia
BuildArch:      noarch

%description
The following shapes are included in the package:
 * CKT Breaker
 * Generator
 * Isolator
 * Transformer

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
