%global source0_hash 4e1f53ebc517dc069d273f2248ecd43eb88a048098dbee97343091e8f43937d4

%define mainversion 2.0
%define extra 0.2.0

Name:           PySolFC-cardsets
Version:        3.0
Release:        6%{?dist}
Summary:        Various cardsets for PySolFC
License:        GPL-2.0-or-later
URL:            https://pysolfc.sourceforge.io/
Source0:        https://github.com/shlomif/PySolFC-Cardsets/archive/%{version}/PySolFC-Cardsets-%{version}.tar.gz
Source1:        https://github.com/shlomif/PySol-Extra-Mahjongg-Cardsets/archive/%{extra}/PySol-Extra-Mahjongg-Cardsets-%{extra}.tar.gz
BuildArch:      noarch

Requires:       PySolFC >= %{mainversion}

%description
This package contains extras cardsets for PySolFC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PySolFC-Cardsets-%{version} -a1

%build

%install
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/PySolFC
# remove cardsets included in PySolFC package (PySolFC-Cardsets--Minimal-3.0.0)
rm -rf cardset-2000 cardset-blaren-7x7 cardset-crystal-mahjongg cardset-dashavatara-ganjifa \
       cardset-dashavatara-ganjifa-xl cardset-dojouji-3x3 \ cardset-dondorf \
       cardset-gnome-mahjongg-1 cardset-hanafuda-200-years cardset-hexadeck \ cardset-hokusai-6x6 \
       cardset-knave-of-hearts-4x4 cardset-louie-mantia-hanafuda cardset-matching \
       cardset-matching-xl cardset-matrix cardset-mid-winter-eve-8x8 cardset-mughal-ganjifa \
       cardset-mughal-ganjifa-xl cardset-neo cardset-neo-hex cardset-neo-tarock \
       cardset-next-matrix cardset-oxymoron cardset-players-trumps-10x10 cardset-simple-ishido \
       cardset-simple-ishido-xl cardset-standard cardset-the-card-players-9x9 cardset-tuxedo \
       cardset-uni-mahjongg cardset-victoria-falls-5x5 cardset-vienna-2k

cp -a cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC
cp -a PySol-Extra-Mahjongg-Cardsets-0.2.0/Lost-Mahjongg-Cardsets/cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC

find $RPM_BUILD_ROOT%{_datadir}/PySolFC -type f -name 'COPYRIGHT' -exec chmod 0644 '{}' \;

%files
%{_datadir}/PySolFC/cardset-*

%changelog
%autochangelog
