%global source0_hash 1bc027d683ba3694aae0664d341379cb29fd721d4761fe45c1c185ee0d46d255

Name:    compiz-bcop
Version: 0.8.18
Release: 15%{?dist}
Epoch:   1
Summary: Compiz option code generator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://gitlab.com/compiz/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildArch:   noarch

BuildRequires: gcc
BuildRequires: libxslt-devel
BuildRequires: automake
BuildRequires: make
Requires: pkgconfig
Requires: util-linux

%description
BCOP is a code generator that provides an easy way to handle
plugin options by generating parts of the plugin code directly
from the xml metadata file.
It is used for most of the Compiz Fusion plugins

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%{make_install}

%files
%doc COPYING NEWS AUTHORS
%{_bindir}/bcop
%{_datadir}/bcop/
%{_datadir}/pkgconfig/bcop.pc

%changelog
%autochangelog
