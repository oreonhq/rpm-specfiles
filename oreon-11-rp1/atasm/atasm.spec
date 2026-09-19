%global source0_hash c3ae8ea1f824e0ee65e123b33982572277207d1749bcd04da3af8f06af977db5

Name:           atasm
Version:        1.30
Release:        4%{?dist}
Summary:        6502 cross-assembler

License:        GPL-2.0-or-later
URL:            https://github.com/CycoPH/atasm
Source0:        %{url}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  make

%description
ATasm is a 6502 command-line cross-assembler that is compatible with the
original Mac/65 macro-assembler released by OSS software.  Code
development can now be performed using "modern" editors and compiles
with lightning speed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
pushd src
%make_build CFLAGS="%{build_cflags} -DZLIB_CAPABLE -DUNIX" L="%{build_ldflags} -lz -lm"
sed -e 's|\%\%DOCDIR\%\%|%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}|g' %{name}.1.in > %{name}.1
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

pushd src
install -p -m 755 %{name} %{buildroot}%{_bindir}
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1
popd

%check
pushd tests
make test
popd

%files
%license LICENSE
%doc VERSION.TXT README.md docs/atasm.blurb docs/atasm.pdf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
