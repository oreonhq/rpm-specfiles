%global source0_hash 26a08a3dc652b4a01125a6e87134364bf07a812cd0b7472683dff81d00454c4d
%bcond tests 0
%global gap_pkgname    curlinterface
%global gap_upname     curlInterface
%global gap_skip_check %[!%{?with_tests}]
%global giturl         https://github.com/gap-packages/curlInterface
Name:           gap-pkg-%{gap_pkgname}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Simple web access for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/curlInterface/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
# /oreon:deps
%description
This package provides a simple GAP wrapper around libcurl, to allow
downloading files over http, ftp and https.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Curl interface for GAP documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%build -p

%configure --with-gaproot=%{gap_archdir} --disable-silent-rules
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-curlinterface-doc -f %{oreon_filedir}/gap-pkg-curlinterface-doc.list

%changelog

%autochangelog
