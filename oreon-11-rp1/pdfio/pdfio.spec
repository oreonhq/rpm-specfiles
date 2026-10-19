%global source1_hash 7d4cd3f5347762a4efc65fd6763f0827018561739a97ac03f185f8f85999d717
%global source0_hash 2b9e1db7c4a72cbc896098a6682a1e51fc2bfb979f00bec8bb515ee79c338084
Name: pdfio
Version: 1.6.5
Release:        1%{?dist}
Summary:        C library for PDF I/O
License: Apache-2.0 WITH LLVM-exception AND Zlib AND GPL-2.0-or-later AND MIT-CMU AND BSD-3-Clause
URL: https://msweet.org/pdfio
Source0:        https://github.com/michaelrsweet/pdfio/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/michaelrsweet/pdfio/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2: msweet-pub.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
PDFIO is C library for reading and writing PDF files. It includes support
for reading and writing encrypted PDF files, accessing pages, objects,
and streams withing PDF file, working with PDF metadata etc.

%package devel
Summary: PDFIO development files and examples
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: google-roboto-fonts
Requires: google-roboto-mono-fonts
%description devel
The package contains development files for PDFIO library.

%package doc
Summary: PDFIO documentation
BuildArch: noarch
%description doc
The package contains HTML documentation and man page for PDFIO library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git

%build

%configure --libdir=%{_libdir} \
  --disable-static \
  --enable-shared \
  --enable-libpng
%make_build
%install
make install
rm %{buildroot}/%{_pkgdocdir}/{LICENSE,NOTICE}
cp -p %{buildroot}%{_pkgdocdir}/examples/code128-LICENSE.txt .
rm %{buildroot}%{_pkgdocdir}/examples/*LICENSE*
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -pr %{buildroot}%{_pkgdocdir}/examples/ %{buildroot}%{_docdir}/%{name}-devel
rm -rf %{buildroot}%{_pkgdocdir}/examples/
for font in Roboto-Bold.ttf Roboto-Italic.ttf Roboto-Regular.ttf
do
  ln -sf ../../../fonts/google-roboto/$font %{buildroot}%{_docdir}/%{name}-devel/examples/$font
done
ln -sf ../../../fonts/google-roboto-mono-fonts/RobotoMono-Regular.ttf %{buildroot}%{_docdir}/%{name}-devel/examples/RobotoMono-Regular.ttf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n pdfio-devel -f %{oreon_filedir}/pdfio-devel.list
%files -n pdfio-doc -f %{oreon_filedir}/pdfio-doc.list

%changelog

%autochangelog
