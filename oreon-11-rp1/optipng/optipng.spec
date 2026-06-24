%global source0_hash none

Name:           optipng
Version:        7.9.1
Release:        3%{?dist}
Summary:        PNG optimizer and converter

License:        zlib
URL:            http://optipng.sourceforge.net/
Source0:        http://downloads.sourceforge.net/optipng/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel libpng-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks
and corrections.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
for f in AUTHORS.txt doc/history.txt ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done

# Ensure system libs and headers are used; as of 0.6.3 pngxtern will use
# the bundled headers if present even with -with-system-*, causing failures.
rm -rf src/libpng src/zlib


%build
# TODO: switch to cmake
%set_build_flags
./configure -prefix=%{_prefix} -mandir=%{_mandir} \
    -with-system-zlib -with-system-libpng
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
chmod -c 755 $RPM_BUILD_ROOT%{_bindir}/optipng


%check
%__make test


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc AUTHORS.txt README.md doc/*
%{_bindir}/optipng
%{_mandir}/man1/optipng.1*


%changelog
%autochangelog

