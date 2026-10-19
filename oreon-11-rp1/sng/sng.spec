%global source0_hash c9bdfb80f5a17db1aab9337baed64a8ebea5c0ddf82915c6887b8cfb87ece61e
Name:           sng
Version:        1.1.2
Release:        1%{?dist}
Summary:        Lossless editing of PNGs via a textual representation
License:        Zlib
URL:            https://sng.sourceforge.net/
Source0:        https://sourceforge.net/projects/sng/files/sng-%{version}.tar.xz
Requires:       rgb
# oreon:deps
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  rgb
BuildRequires:  rubygem-asciidoctor
BuildRequires:  zlib-devel
# /oreon:deps
%description
SNG (Scriptable Network Graphics) is a minilanguage designed specifically to
represent the entire contents of a PNG (Portable Network Graphics) file in an
editable form. Thus, SNGs representing elaborate graphics images and ancillary
chunk data can be readily generated or modified using only text tools.

SNG is implemented by a compiler/decompiler called sng that losslessly
translates between SNG and PNG.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Do not ignore specified linker flags
sed -r -i 's/LDFLAGS=/LDFLAGS+=/' Makefile

%build

%make_build
%install
%make_install prefix=%{_prefix}
%oreon_autofiles main

%check

./sng_regress *.png *.sng
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
