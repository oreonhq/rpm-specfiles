%global source0_hash 946b05c75e877de8aea71b5bf0af74f79b392064793fda7322e4895073e7cf6a
%global gap_pkgname crypting
%global giturl      https://github.com/gap-packages/crypting
Name:           gap-pkg-%{gap_pkgname}
Version:        0.10.7
Release:        1%{?dist}
Summary:        Hashes and Crypto in GAP
License:        BSD-3-Clause
URL:            https://gap-packages.github.io/crypting/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
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
# /oreon:deps
%description
This package implements some cryptographic primitives.  At the moment this is
a custom implementation of SHA256 and HMAC, which is needed to sign messages
in the Jupyter kernel.

Bindings to a full crypto library are a possibility for the future, and
pull-requests (after discussion) are appreciated.

%package doc
License:        BSD-3-Clause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
BuildArch:      noarch
Summary:        Crypting documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build -p

./configure %{gap_archdir}
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-crypting-doc -f %{oreon_filedir}/gap-pkg-crypting-doc.list

%changelog

%autochangelog
