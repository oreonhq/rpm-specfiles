%global source0_hash 13fd4db2936d03b73812a7bcc2a658e4dd29cc776a56c3670a7fc6f1a0ee8af8
Name:		putty
Version:	0.85
Release:        1%{?dist}
Summary:        SSH, Telnet and Rlogin client
License:	MIT
URL:		http://www.chiark.greenend.org.uk/~sgtatham/putty/
Source0:        http://the.earth.li/~sgtatham/putty/latest/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.svg
Source3:	uk.org.greenend.chiark.sgtatham.putty.metainfo.xml
Requires:	hicolor-icon-theme
Requires:	gdk-pixbuf2-modules-extra
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  halibut
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  perl-Digest-SHA
BuildRequires:  python3-devel
BuildRequires:  sed
# /oreon:deps
%description
Putty is a SSH, Telnet & Rlogin client - this time for Linux.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# fix python shebangs to use python3 (python bits aren't currently packaged)
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

%build

export CFLAGS="%{build_cflags} -DNOT_X_WINDOWS -Wno-error=unused-function"
%cmake
%cmake_build
make -C icons putty-48.png
%cmake_build -t doc
%install
%cmake_install
install -d html
install -pm 0644 doc/html/*.html html
desktop-file-install \
  --vendor "" \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
install -m644 -D -p icons/putty-48.png %{buildroot}%{_datadir}/pixmaps/putty.png
install -m644 -D -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/putty.svg
install -m644 -D -p %{SOURCE3} %{buildroot}%{_metainfodir}/uk.org.greenend.chiark.sgtatham.putty.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
