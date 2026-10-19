%global source0_hash f5e3efa4e739b80e87443b1b1124c79036ef7ed684d8d5f58f5ce4e5754516db
Summary:        Firmware for Epson flatbed scanners
Name:		iscan-firmware
Version:	20241112
Release:        1%{?dist}
License:	LicenseRef-Fedora-Firmware
URL:		http://download.ebz.epson.net/dsc/search/01/search/
BuildArch:	noarch
Source0:        iscan-plugin-gt-f500-1.0.0-1.c2.i386.rpm
Source1:    iscan-plugin-gt-9400-1.0.0-1.c2.i386.rpm
Source2:    iscan-plugin-gt-f520-1.0.0-1.c2.i386.rpm
Source3:    iscan-plugin-gt-f600-1.0.0-1.c2.i386.rpm
Source4:    iscan-plugin-gt-x750-2.1.2-1.x86_64.rpm
Source5:    iscan-plugin-gt-s600-2.1.2-1.x86_64.rpm
Source6:    iscan-plugin-gt-f670-2.1.2-1.x86_64.rpm
Source7:    iscan-plugin-gt-f700-2.1.2-1.x86_64.rpm
Source8:    iscan-plugin-gt-1500-2.2.0-1.x86_64.rpm
Source9:    esci-interpreter-gt-f720-0.1.1-2.x86_64.rpm
Source10:   iscan-plugin-gt-x770-2.1.2-1.i386.rpm
Requires:	linux-firmware
# oreon:deps

# /oreon:deps
%description
Firmware for the following Epson flatbed scanners:

* esfw32: Perfection 3170 PHOTO / GT-9400
* esfw41: Perfection 2480/2580 PHOTO / GT-F500/F550
* esfw43: Perfection 4180 PHOTO / GT-F600
* esfw52: Perfection 3490/3590 PHOTO / GT-F520/F570
* esfw54: Perfection 4490 PHOTO / GT-X750
* esfw66: Perfection V10/V100 PHOTO / GT-S600 / GT-F650
* esfw68: Perfection V350 PHOTO / GT-F700
* esfw7A: Perfection V200 PHOTO / GT-F670
* esfw7C: Perfection V500 PHOTO / GT-X770
* esfw86: GT-1500 / GT-D1000
* esfw8b: Perfection V30/V300 / GT-F720 / GT-S620

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -T
for f in \
    %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
    %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10}; do
    rpm2cpio $f | cpio -idm --no-absolute-filenames
done

find ./%{_docdir} -name "*txt" -exec mv {} . \;

for file in *.txt ; do
    iconv -f euc-jp -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/epson
install -pm644 .%{_datadir}/*/*.bin %{buildroot}%{_prefix}/lib/firmware/epson/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
