%global source0_hash 652a3761df241927df921759299fac13e9c73bae6092fdd5406fd84dfecae5ba

%global gitversion 9db45842

Name:           lv2-mdaEPiano
Version:        0
Release:        0.34.git%{gitversion}%{?dist}
Summary:        A port of the MDA EPiano VST plugin to LV2

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/rekado/%{name}
Source0:        %{name}-%{version}-git%{gitversion}.tar.bz2
# check out specific git revision sh lv2-mdaEPiano-snapshot.sh %%gitversion
Source1:        lv2-mdaEPiano-snapshot.sh

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  lv2-c++-tools-static
Requires:       lv2

%description
A port of the popular MDA EPiano VST plugin to LV2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
sed -i -e 's|-O $(WARNINGS)|$(CFLAGS)|'  src/Makefile

# Fix encoding issues
for file in LICENSE README.md; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
cd src
make PREFIX=%{_prefix} CFLAGS="%optflags" %{?_smp_mflags}

%install
cd src
make install INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/lv2-mdaEPiano.lv2

%changelog
%autochangelog
