%global source0_hash a0731bb5a5216e16526aad9409ad8254bdb8697d7c78f71f85d7e82167d1a930
%bcond_without cupsd
%global _cups_serverbin %{_prefix}/lib/cups
%global commit 386eea385f4d672dded45abd602282a94e06e22c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           braille-printer-app
Epoch:          1
Version:        2.0~b0^386eea385f
Release:        11%{?dist}
Summary:        Braille printer application
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/OpenPrinting/braille-printer-app
Source0:        https://github.com/OpenPrinting/%{name}/archive/%{shortcommit}/%{name}-%{commit}.tar.gz
Patch001: 0001-configure.ac-Add-configure-option-for-musicxml-file-.patch
Obsoletes: cups-filters-braille < 2.0
Provides: cups-filters-braille = %{version}-%{release}
%if %{with cupsd}
Recommends: cups
%endif
%if %{with cupsd}
Requires: cups-filesystem
%endif
Requires: cups-filters
Requires: ImageMagick
Requires: liblouisutdml-utils
Requires: poppler-utils
Requires: unzip
Suggests: antiword
Suggests: inkscape
Suggests: liblouis-utils
Suggests: lynx
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  liblouis
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cups)
# /oreon:deps
%description
The printer application currently provides classic printer drivers -
backends, filters and PPDs - it will be migrated to full fledged printer
application in the future.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -S git

%build

./autogen.sh
%configure
%make_build
%check

make check
%install
%make_install
rm -f %{buildroot}%{_pkgdocdir}/{NOTICE,COPYING,LICENSE}
rm -f %{buildroot}%{_pkgdocdir}/{INSTALL,CHANGES-1.x.md,DEVELOPING.md,ABOUT-NLS}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
