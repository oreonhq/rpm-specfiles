%global source0_hash 217cfe4dd8bf851710c2e9e8d332a33ecd930452b4c12f3a53f242b5f549e045
Name:           toga2
Version:        4.0
Release:        1%{?dist}
Summary:        UCI chess engine based on Fruit
License:        GPL-2.0-only
URL:            http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66174
Source0:        https://www.mediafire.com/file/4c8m5lejoo7fi3d/TogaII40.zip
Source1:        toga2.6
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  sed
# /oreon:deps
%description
Toga II is a UCI chess engine based on Fruit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TogaII40
# Remove precompiled binaries
rm -r Windows
# Convert readme to UTF-8 and Unix end-of-line encodings
f=readme.txt
iconv --from=ISO-8859-1 --to=UTF-8 "${f}" > "${f}.utf8"
touch -r "${f}" "${f}.utf8"
mv "${f}.utf8" "${f}"
sed -i 's/\r$//' "${f}"

%build

pushd src
%{__cxx} -o toga2 %{optflags} *.cpp %{build_ldflags} -lm -lpthread
%install
mkdir -p %{buildroot}/%{_bindir}
cp -P src/toga2 %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man6
cp -P %SOURCE1 %{buildroot}/%{_mandir}/man6
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
