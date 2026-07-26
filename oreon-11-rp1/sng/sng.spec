%global source0_hash c9bdfb80f5a17db1aab9337baed64a8ebea5c0ddf82915c6887b8cfb87ece61e

Name:           sng
Version:        1.1.1
Release:        %autorelease
Summary:        Lossless editing of PNGs via a textual representation

License:        Zlib
URL:            https://sng.sourceforge.net/
Source0:        https://sourceforge.net/projects/sng/files/sng-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  rgb
BuildRequires:  rubygem-asciidoctor

Requires:       rgb

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

%check
# Upstream has a test suite, but the test files are not packaged.
# Let's just check on the files that are in the tarball.
./sng_regress *.png *.sng

%files
%license COPYING
%doc NEWS.adoc README TODO
%doc %_mandir/man1/sng.1*
%_bindir/sng

%changelog
%autochangelog
