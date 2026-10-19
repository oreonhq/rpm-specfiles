%global source0_hash 02045d58408d95f7412736e1e7ad9f934f495eaf72055321991eb1d1ed4667e7
Name:		cqrlog
Version:	3.1.0
Release:        1%{?dist}
Summary:        An amateur radio contact logging program
License:	GPL-2.0-only
URL:		http://www.cqrlog.com/
Source0:        https://github.com/ok2cqr/cqrlog/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         cqrlog-install.patch
Patch1:         cqrlog-desktop.patch
Patch2:         cqrlog-fpc-3.2.4.patch
ExclusiveArch:  %{fpc_arches}
Requires:	mariadb-server
Requires:       mariadb-libs
Requires:       hamlib 
Requires:       openssl
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  lazarus
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
CQRLOG is an advanced ham radio logger based on MySQL database. Provides radio
control based on hamlib libraries (currently support of 140+ radio types and 
models), DX cluster connection, QRZ callbook (web version), a grayliner, 
internal QSL manager database support and a most accurate country resolution 
algorithm based on country tables developed by OK1RR. CQRLOG is intended for 
daily general logging of HF, CW & SSB contacts and strongly focused on easy 
operation and maintenance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

chmod -x src/azidis3.pas
chmod -x src/gline2.pas
chmod -x src/odbec.pas
chmod -x src/aziloc.pas
chmod -x src/znacmech.pas
chmod -x tools/cqrlog-apparmor-fix
chmod -x voice_keyer/voice_keyer.sh

%build

make %{?_smp_mflags}
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/cqrlog.desktop
for size in 32 48 64 128 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
    mv images/icon/${size}x${size}/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
done
for file in $(find %{buildroot}%{_datadir}/%{name} -name "*.txt"); do
    sed -i 's/\r//' $file
done
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/CountryDel.tab
sed -i 's/\r//' %{buildroot}%{_datadir}/%{name}/ctyfiles/MASTER.SCP
iconv -f iso8859-1 -t utf-8 %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt > %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv && mv -f %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt.conv %{buildroot}%{_datadir}/%{name}/ctyfiles/eqsl.txt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
