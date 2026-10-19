%global source0_hash f5990542bbfb632a18e664bb956d1dfa35b20945881c617af641a9ee8cfbc47b
Name:		daa2iso
Summary:        Program for converting DAA files to ISO
Version:	0.1.7e
Release:        1%{?dist}
License:	GPL-2.0-or-later
Source0:        http://aluigi.altervista.org/mytoolz/daa2iso.zip
URL:		http://aluigi.altervista.org/mytoolz.htm
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
DAA2ISO is an open source command-line/GUI tool for converting single and 
multipart DAA images to the original ISO format.

The DAA image (Direct Access Archive) in fact is just a compressed
CD/DVD ISO which can be created through the commercial program
PowerISO.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}
sed -i -e 's|\r||g' daa2iso.txt

%build

cd src/
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p src/daa2iso $RPM_BUILD_ROOT%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
