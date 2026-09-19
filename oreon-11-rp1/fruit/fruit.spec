%global source0_hash ad13f6099dc2acebf0112c36cc7d38fd4009316ad60ecc294c5e828380dcd2c0

Name:           fruit
Version:        2.1
Release:        13%{?dist}
Summary:        UCI chess engine

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://arctrix.com/nas/chess/fruit
Source0:        %{url}/fruit_21_linux.zip
Source1:        https://web.archive.org/web/20080117060815/http://wbec-ridderkerk.nl/html/download/fruit/Dann_Books.zip
Source2:        https://salsa.debian.org/debian/fruit/-/raw/debian/master/debian/fruit.6

# Accept go command without arguments
Patch0:         https://salsa.debian.org/debian/fruit/-/raw/debian/master/debian/patches/02-simple_go.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

Recommends:     %{name}-books

%description
Fruit is a chess engine that uses the UCI protocol.

%package books
Summary:        Opening books for %{name}
BuildArch:      noarch
Requires:       fruit

%description books
This package includes opening books for the Fruit chess engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fruit_21_linux -p1 -b 1
# Remove precompiled binary
rm fruit_21_static
# Convert docs to Unix end-of-line encodings
mv ../Dann_Books/Readme.txt .
sed -i 's/\r$//' readme.txt technical_10.txt Readme.txt
# Fix default opening book path
sed -i 's:book_small.bin:%{_datadir}/%{name}/book_small.bin:' src/option.cpp

%build
%make_build -C src \
  CXXFLAGS="%{optflags} -fstrict-aliasing" \
  LDFLAGS="%{build_ldflags} -lm"

%install
mkdir -p %{buildroot}/%{_bindir}
cp -P src/fruit %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -P book_small.bin %{buildroot}/%{_datadir}/%{name}
cp -PR ../Dann_Books %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_mandir}/man6
cp -P %SOURCE2 %{buildroot}/%{_mandir}/man6

%files
%license copying.txt
%doc readme.txt technical_10.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*

%files books
%license copying.txt
%doc Readme.txt
%{_datadir}/%{name}/*

%changelog
%autochangelog
